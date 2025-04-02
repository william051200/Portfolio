from models.class_e import Class_E


class Class_C:
    def __init__(self):
        self._class_e = Class_E()

    @property
    def class_e(self):
        return self._class_e

    def get_number(self):
        return "2"

    def get_end(self):
        return "end"

    def get_formatter_mapping(self):
        return {
            "get_end": self.get_end,
            "class_e": self.class_e.get_formatter_mapping(),
        }

    def get_all(self):
        return {
            "get_end": self.get_end(),
            "class_e": self.class_e.get_all(),
        }
