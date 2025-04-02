import json
from models.field_config import FieldConfig
from models.formatter_config import FormatterConfig


class FieldReader:
    @staticmethod
    def read_formatters(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return [
                FormatterConfig(
                    formatter_id=formatter["id"],
                    name=formatter["name"],
                    field_data=formatter["field_data"],
                )
                for formatter in data
            ]

    @staticmethod
    def get_formatter_by_name(formatters, name):
        for formatter in formatters:
            if formatter.name == name:
                return formatter
        raise ValueError(f"Formatter with name '{name}' not found")

    @staticmethod
    def get_formatter_by_id(formatters, formatter_id):
        for formatter in formatters:
            if formatter.id == formatter_id:
                return formatter
        raise ValueError(f"Formatter with ID '{formatter_id}' not found")
