import json
from models.delimiter_config import DelimiterConfig


class DelimiterReader:
    @staticmethod
    def read_config(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            delimiters = data["delimiters"]
            return DelimiterConfig(
                array_start=delimiters["array_start"],
                array_end=delimiters["array_end"],
                array_separator=delimiters["array_separator"],
                object_start=delimiters["object_start"],
                object_end=delimiters["object_end"],
                object_separator=delimiters["object_separator"],
                key_value_separator=delimiters["key_value_separator"],
            )
