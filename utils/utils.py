import json
import random


class Utils:

    @classmethod
    def get_radon_chars(cls, length):
        sample_string = 'abcdefghijklmnopqrstuvxzyw'  # define the specific string
        # define the condition for random string
        result = ''.join((random.choice(sample_string)) for x in range(length))

    @classmethod
    def get_radon_numbers(cls, length):
        sample_string = '1234567890'  # define the specific string
        # define the condition for random string
        result = ''.join((random.choice(sample_string)) for x in range(length))

    @classmethod
    def read_json_config_file(cls):
        # Read the file
        with open('config.json') as config_file:
            config = json.load(config_file)
        return config

    @classmethod
    def read_enviroment_key_json(cls, key):
        with open('config.json') as config_file:
            config = json.load(config_file)
            enviroment = config["enviroment"]
            result = config[enviroment][key]
        return result

    @classmethod
    def get_json_in_response(cls, response):
        try:
            response_body = response.json()
        except json.decoder.JSONDecodeError:
            response_body = ""
        return response_body

    @classmethod
    def convert_into_list(cls, result, description):
        results = []
        columns = [column[0] for column in description]
        for row in result:
            results.append(dict(zip(columns, row)))
        return results

    @classmethod
    def read_file(cls, path):
        return open(path, "r").read()

    @classmethod
    def convert_object_into_json(cls, payload):
        return json.dumps(payload, default=lambda x: x.__dict__)
