"""
This module contains the measurement plugin which stores triggering message measurements
"""

import typing

import mongo.mongo
import plugins.base


def run_plugin(config: typing.Dict):
    """Runs this plugin using the given configuration

    :param config: Configuration dictionary
    """
    plugins.base.run_plugin(MeasurementPlugin, config)


class MeasurementPlugin(plugins.base.MaukaPlugin):
    """
    This class contains the measurement plugin which stores triggering message measurements
    """
    def __init__(self, config: typing.Dict):
        """ Initializes this plugin

        :param config: Configuration dictionary
        """
        super().__init__(config, ["measurement"], "MeasurementPlugin")

        self.sample_every = int(self.config_get("plugins.MeasurementPlugin.sample_every"))
        """Of all the triggering messages, how often should we sample values from the stream"""

        self.measurements_collection = self.mongo_client.db[mongo.mongo.Collection.MEASUREMENTS]
        """Mongo OPQ measurements collection"""

        self.device_id_to_sample_cnt = {}
        """For each device, store how many samples its received"""

        self.init_measurements_collection()

    def init_measurements_collection(self):
        """
        Make sure proper indexes are setup for measurements
        """
        self.measurements_collection.create_index("device_id")
        self.measurements_collection.create_index("timestamp_ms")

    def on_message(self, topic, message):
        """Subscribed messages occur async

        Messages are stored in mongo based on the sampling rate

        :param topic: The topic that this message is associated with
        :param message: The message
        """
        measurement = plugins.base.protobuf_decode_measurement(message)
        device_id = measurement.id

        if device_id not in self.device_id_to_sample_cnt:
            self.device_id_to_sample_cnt[device_id] = 0

        if self.device_id_to_sample_cnt[device_id] == (self.sample_every - 1):
            self.device_id_to_sample_cnt[device_id] = 0
            measurement = {
                "device_id": device_id,
                "timestamp_ms": measurement.time,
                "frequency": measurement.frequency,
                "voltage": measurement.rms
            }
            self.measurements_collection.insert_one(measurement)

        self.device_id_to_sample_cnt[device_id] += 1
