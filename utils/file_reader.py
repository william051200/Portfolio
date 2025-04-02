import json
from models.field_config import FieldConfig


class JsonReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            configs = {}
            for field_name, field_data in data.items():
                config = FieldConfig(
                    name=field_name,
                    path=field_data["path"],
                    prefix=field_data.get("prefix"),
                    suffix=field_data.get("suffix"),
                )
                configs[field_name] = config
            return configs
