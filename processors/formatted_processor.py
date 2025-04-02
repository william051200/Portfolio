from processors.field_processor import FieldProcessor


class FormattedProcessor(FieldProcessor):
    def __init__(self, formatter, delimiter_config):
        super().__init__(formatter)  # Pass formatter instead of field_list
        self._delimiter_config = delimiter_config

    @property
    def delimiter_config(self):
        return self._delimiter_config

    @delimiter_config.setter
    def delimiter_config(self, value):
        self._delimiter_config = value

    def _simplify_value(self, value):
        """Simplify a value by extracting the part after colon if present"""
        if isinstance(value, str) and ":" in value:
            return value.split(":")[1]
        return value

    def _format_object(self, obj, simplified):
        """Format a dictionary object"""
        items = []
        for key, value in obj.items():
            if simplified:
                # Only append the simplified value
                formatted_value = self._simplify_value(
                    self.format_dict(value, simplified)
                )
                items.append(formatted_value)
            else:
                formatted_value = self.format_dict(value, simplified)
                items.append(
                    f"{key}{self.delimiter_config.key_value_separator}{formatted_value}"
                )

        return (
            f"{self.delimiter_config.object_start}"
            f"{self.delimiter_config.object_separator.join(items)}"
            f"{self.delimiter_config.object_end}"
        )

    def _format_array(self, arr, simplified):
        """Format a list object"""
        items = [self.format_dict(item, simplified) for item in arr]
        return (
            f"{self.delimiter_config.array_start}"
            f"{self.delimiter_config.array_separator.join(items)}"
            f"{self.delimiter_config.array_end}"
        )

    def format_dict(self, d, simplified=False):
        """Format any data structure according to delimiter config"""
        if isinstance(d, dict):
            return self._format_object(d, simplified)
        elif isinstance(d, list):
            return self._format_array(d, simplified)

        if simplified:
            return self._simplify_value(str(d))
        return str(d)

    def process_field_by_index(self, index):
        """Process a field by its index and apply formatting"""
        field = self.formatter.get_field(index)  # Use formatter instead of field_list
        result = super().process_field_by_index(index)

        if field.prefix is None and field.suffix is None:
            return result

        formatted_result = (
            self.format_dict(result, field.simplified)
            if isinstance(result, (dict, list))
            else result
        )
        return f"{field.prefix}{formatted_result}{field.suffix}"

    def process_all_fields(self):
        """Process all fields in the formatter"""
        return [self.process_field_by_index(i) for i in range(self.formatter.count)]
