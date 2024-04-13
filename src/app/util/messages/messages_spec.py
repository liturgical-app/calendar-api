from from_root import from_root
from src.app.util.messages.messages import Messages


class MessagesSpec:

    subject = Messages(from_root("resources", "test", "messages.properties"))

    def should_return_message_for_given_key_when_it_exists(self):
        message = self.subject.load("key0")
        assert message == "value0"

    def should_return_empty_string_for_given_key_that_does_not_exist(self):
        message = self.subject.load("key-1")
        assert message == ""

    def should_include_placeholders_for_key_loaded_without_params(self):
        message = self.subject.load("key1")
        assert message == "value1 {0}"

    def should_replace_placeholders_for_key_loaded_with_params(self):
        message = self.subject.load_with_params("key1", ["Hello there!"])
        assert message == "value1 Hello there!"

    def should_replace_newline_chars(self):
        message = self.subject.load("key2-newline")
        assert message == "Watch out for that ledge!\n\n\nAhhhhhhhh!"