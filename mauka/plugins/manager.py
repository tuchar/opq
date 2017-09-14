import json
import logging
import multiprocessing
import os
import sys
import typing

import zmq

_logger = logging.getLogger("app")
logging.basicConfig(
    format="[%(levelname)s][%(asctime)s][{} %(filename)s:%(lineno)s - %(funcName)s() ] %(message)s".format(
        os.getpid()))
_logger.setLevel(logging.DEBUG)


class PluginManager:
    def __init__(self, config: typing.Dict):
        self.config = config
        self.name_to_plugin_class = {}

        self.name_to_process = {}
        self.name_to_exit_event = {}
        self.name_to_enabled = {}

    def register_plugin(self, plugin_class, enabled: bool = True):
        name = plugin_class.NAME
        self.name_to_plugin_class[name] = plugin_class
        self.name_to_enabled[name] = enabled

    def run_plugin(self, plugin_name: str):
        if plugin_name not in self.name_to_plugin_class:
            _logger.error("Plugin {} DNE".format(plugin_name))
            return

        if not self.name_to_enabled[plugin_name]:
            _logger.error("Can not run disabled plugin")

        def _run_plugin(plugin_class, config: typing.Dict, exit_event: multiprocessing.Event):
            """Inner function that acts as target to multiprocess constructor"""
            plugin_instance = plugin_class(config, exit_event)
            plugin_instance._run()

        plugin_class = self.name_to_plugin_class[plugin_name]
        exit_event = multiprocessing.Event()
        process = multiprocessing.Process(target=_run_plugin, args=(plugin_class, self.config, exit_event))
        process.start()
        self.name_to_process[plugin_name] = process
        self.name_to_exit_event[plugin_name] = exit_event

    def ls(self):
        resp = ""
        for name in sorted(self.name_to_plugin_class):
            enabled = self.name_to_enabled[name]
            process = self.name_to_process[name] if name in self.name_to_process else "N/A"
            process_pid = process.pid if process != "N/A" else "N/A"
            exit_event = self.name_to_exit_event[name].is_set() if name in self.name_to_exit_event else "N/A"

            resp += "name: {} enabled: {} process: {}[{}] exit_event: {}\n".format(name, enabled, process, process_pid, exit_event)

        return resp

    def run_all_plugins(self):
        _logger.info("Starting all plugins")
        for name in self.name_to_plugin_class:
            if self.name_to_enabled[name]:
                self.run_plugin(name)

    def handle_tcp_request(self, request: str) -> str:
        if request == "ls":
            return self.ls()
        else:
            return "Unknown cmd {}".format(request)

    def start_tcp_server(self):
        _logger.info("Starting plugin manager TCP server")
        zmq_context = zmq.Context()
        zmq_reply_socket = zmq_context.socket(zmq.REP)
        zmq_reply_socket.bind(self.config["zmq.mauka.plugin.management.rep.interface"])

        while True:
            request = zmq_reply_socket.recv_string()
            zmq_reply_socket.send_string(self.handle_tcp_request(request))


def send_recv(cmd: str, config: typing.Dict) -> str:
    zmq_context = zmq.Context()
    zmq_request_socket = zmq_context.socket(zmq.REQ)
    zmq_request_socket.connect(config["zmq.mauka.plugin.management.req.interface"])
    zmq_request_socket.send_string(cmd)
    return zmq_request_socket.recv_string()


def run_cli(config: typing.Dict):
    prompt = "opq-mauka> "
    i = input(prompt)
    while i != "exit":
        print(send_recv(i, config))
        i = input(prompt)


def usage():
    pass


def load_config(path: str) -> typing.Dict:
    """Loads a configuration file from the file system

    :param path: Path of configuration file
    :return: Configuration dictionary
    """
    _logger.info("Loading configuration from {}".format(path))
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError as e:
        _logger.error(e)
        usage()
        exit(0)


if __name__ == "__main__":
    config_path = sys.argv[1]
    config = load_config(config_path)
    run_cli(config)
