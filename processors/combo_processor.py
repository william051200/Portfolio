from processors.base_processor import BaseProcessor
from models.class_a import Class_A


class ComboProcessor(BaseProcessor):
    def __init__(self, config_file):
        super().__init__(config_file)
        self.root_class = Class_A()

    def get_all_values(self, obj):
        if isinstance(obj, list):
            return [self.get_all_values(item) for item in obj]

        if hasattr(obj, "get_all"):
            return obj.get_all()

        if callable(obj):
            return obj()

        return obj

    def process_combo(self, combo_name):
        if combo_name not in self.configs:
            raise ValueError(f"Combo {combo_name} not found")

        config = self.configs[combo_name]
        result = self.root_class

        for step in config.path:
            if isinstance(result, list):
                result = [getattr(item, step) for item in result]
            else:
                result = getattr(result, step)

        return self.get_all_values(result)
