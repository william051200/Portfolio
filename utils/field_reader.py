import json
from models.field_config import FieldConfig
from models.field_list import FieldList


class FieldReader:
    @staticmethod
    def read_fields(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            configs = {}
            for index, field_data in enumerate(data):
                configs[f"field{index + 1}"] = FieldConfig(
                    path=field_data["path"],
                    prefix=field_data.get("prefix"),
                    suffix=field_data.get("suffix"),
                    simplified=field_data.get("simplified"),
                )
            return FieldList(configs)
