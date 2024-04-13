import json
import logging
from pyjavaproperties import Properties


# Wrapper functionality for the Message Bundle
class Messages:

    def __init__(self, path):
        self.bundle = Properties()
        self.bundle.load(open(path))
        self.log = logging.getLogger(__name__)

    def load(self, key):
        message = self.load_with_params(key, None)
        return message

    def load_with_params(self, key, parameters):
        message = self.bundle[key]
        if message is None:
            self.log.debug(f"[load_with_params] Unable to find message for key [{key}]")
            return ''
        else:
            if isinstance(parameters, list):
                for index in range(len(parameters)):
                    message = message.replace('{' + str(index) + '}', parameters[index])
            message = message.replace("\\n", "\n")
            return message

    def load_all(self):
        all_messages = {}
        for key in self.bundle.propertyNames():
            all_messages[key] = self.bundle[key]
        return json.dumps(all_messages)