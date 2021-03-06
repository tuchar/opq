#include <zmqpp/socket.hpp>
#include <zmqpp/message.hpp>
#include "DataHandler.h"
#include "MongoDriver.h"
#include "util.h"
#include "opq.pb.h"

using namespace std;

DataHandler::DataHandler(Config &c, zmqpp::context &ctx) : _ctx(ctx), _config(c) {
}

void DataHandler::handle_data_loop() {

    //Socket for talking to Mauka
    auto backend_pub = zmqpp::socket(_ctx, zmqpp::socket_type::pub);
    backend_pub.connect(_config.backend_interface_pub);
    MongoDriver mongo(_config.mongo_uri);
    //Socket that pulls data from boxes.
    auto box_pull = zmqpp::socket{_ctx, zmqpp::socket_type::pull};
    auto server_cert = load_certificate(_config.private_cert);
    box_pull.set(zmqpp::socket_option::curve_server, true);
    box_pull.set(zmqpp::socket_option::curve_secret_key, server_cert.second);
    box_pull.set(zmqpp::socket_option::zap_domain, "global");
    box_pull.bind(_config.box_interface_pull);
    _done = false;
    while (!_done) {
        //Receive a data message
        zmqpp::message zm;
        box_pull.receive(zm);

        //Deserialize
        auto serialized_resp = zm.get(0);
        opq::proto::RequestDataMessage header;
        header.ParseFromString(serialized_resp);

        //Get the boxID and the event number
        auto boxid = header.boxid();
        auto sequence_number = header.sequence_number();
        if(header.type() == header.RESP) {
            std::vector<opq::proto::DataMessage> messages;
            std::cout << "Recieved " << zm.parts() << endl;
            //Push every part of the message except for the header to redis.
            for (size_t i = 1; i < zm.parts(); i++) {
                opq::proto::DataMessage m;
                m.ParseFromString(zm.get(i));
                messages.push_back(m);
            }
            mongo.append_data_to_event(messages, sequence_number);
        }
    }

}
