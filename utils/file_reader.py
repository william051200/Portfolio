import json
from models.combo_config import ComboConfig


class JsonReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        configs = {}
        for combo_name, combo_data in data.items():
            config = ComboConfig(
                name=combo_name,
                path=combo_data["path"],
                prefix=combo_data.get("prefix"),
                suffix=combo_data.get("suffix"),
            )
            configs[combo_name] = config

        return configs
