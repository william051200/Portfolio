class Class_E:
    def get_E(self):
        return "E"

    def get_formatter_mapping(self):
        return {
            "get_E": self.get_E,
        }

    def get_all(self):
        return {
            "get_E": self.get_E(),
        }
