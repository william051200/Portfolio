from processors.combo_processor import ComboProcessor


class FormattedProcessor(ComboProcessor):
    def format_result(self, result, prefix, suffix):
        if isinstance(result, list):
            return f"{prefix}{', '.join(map(str, result))}{suffix}"
        return f"{prefix}{result}{suffix}"

    def process_combo(self, combo_name):
        config = self.configs[combo_name]
        result = super().process_combo(combo_name)

        if config.prefix is None and config.suffix is None:
            return result

        return self.format_result(result, config.prefix, config.suffix)
