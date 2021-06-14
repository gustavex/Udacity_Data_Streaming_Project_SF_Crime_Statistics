from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        """Generate data from input json file"""
        with open(self.input_file) as f:
            data = json.load(f)
            for line in data:
                message = self.json_dict_to_binary(line)
                # TODO send the correct data
                self.send(self.topic,message)
                time.sleep(0.01)

    # TODO fill this in to return the json dictionary to binary
    def json_dict_to_binary(self, json_dict):
        """Convert dictionary to json format and utf-8 encoding"""
        json_dump = json.dumps(json_dict)
        return json_dump.encode('utf-8')        