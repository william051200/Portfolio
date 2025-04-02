from processors.combo_processor import ComboProcessor


class FormattedProcessor(ComboProcessor):
    def __init__(self, config_file, delimiter_config):
        super().__init__(config_file)
        self.delimiter_config = delimiter_config

    def format_dict(self, d):
        if isinstance(d, dict):
            items = []
            for key, value in d.items():
                formatted_value = self.format_dict(value)
                items.append(
                    f"{key}{self.delimiter_config.key_value_separator}{formatted_value}"
                )
            return f"{self.delimiter_config.object_start}{self.delimiter_config.object_separator.join(items)}{self.delimiter_config.object_end}"
        elif isinstance(d, list):
            items = [self.format_dict(item) for item in d]
            return f"{self.delimiter_config.array_start}{self.delimiter_config.array_separator.join(items)}{self.delimiter_config.array_end}"
        return str(d)

    def format_result(self, result, prefix, suffix):
        if isinstance(result, (dict, list)):
            formatted_result = self.format_dict(result)
            return f"{prefix}{formatted_result}{suffix}"
        return f"{prefix}{result}{suffix}"

    def process_combo(self, combo_name):
        config = self.configs[combo_name]
        result = super().process_combo(combo_name)

        if config.prefix is None and config.suffix is None:
            return result

        return self.format_result(result, config.prefix, config.suffix)
