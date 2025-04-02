from models.class_e import Class_E


class Class_D:
    def __init__(self):
        self._class_e = [Class_E(), Class_E()]

    @property
    def class_e(self):
        return self._class_e

    def get_array(self):
        return "array"

    def get_formatter_mapping(self):
        return {
            "get_array": self.get_array,
            "class_e": [e.get_formatter_mapping() for e in self.class_e],
        }

    def get_all(self):
        return {
            "get_array": self.get_array(),
            "class_e": [e.get_all() for e in self.class_e],
        }
