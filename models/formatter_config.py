from models.field_config import FieldConfig


class FormatterConfig:
    def __init__(self, formatter_id, name, field_data):
        self._id = formatter_id
        self._name = name
        self._field_configs = [
            FieldConfig(
                path=field["path"],
                prefix=field.get("prefix"),
                suffix=field.get("suffix"),
                simplified=field.get("simplified", False),
            )
            for field in field_data
        ]

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def field_configs(self):
        return self._field_configs

    @field_configs.setter
    def field_configs(self, value):
        self._field_configs = value

    @property
    def count(self):
        return len(self._field_configs)

    def get_field(self, index):
        return self._field_configs[index]
