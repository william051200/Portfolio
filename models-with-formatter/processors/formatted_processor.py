from typing import Any, List, Optional
from models.field_data import FieldData
from models.delimiter_config import DelimiterConfig


class FormattedProcessor:
    def __init__(self, field_data: FieldData, delimiter_config: DelimiterConfig, root_class: Any):
        self._field_data = field_data
        self._delimiter_config = delimiter_config
        self._root_class = root_class

    def _format_value(self, value: Any) -> str:
        """Format a value according to its type and the delimiter configuration."""
        if isinstance(value, dict):
            return self._format_dict(value)
        elif isinstance(value, list):
            return self._format_list(value)
        return str(value)

    def _format_dict(self, d: dict) -> str:
        """Format a dictionary using the configured delimiters."""
        # items = [f"{k}{self._delimiter_config.key_value_separator}{self._format_value(v)}"
        #          for k, v in d.items()]
        items = [f"{self._format_value(v)}" for k, v in d.items()]
        return f"{self._delimiter_config.object_start}{self._delimiter_config.object_separator.join(items)}{self._delimiter_config.object_end}"

    def _format_list(self, lst: list) -> str:
        """Format a list using the configured delimiters."""
        items = [self._format_value(item) for item in lst]
        return f"{self._delimiter_config.array_start}{self._delimiter_config.array_separator.join(items)}{self._delimiter_config.array_end}"

    def process_field_lines(self) -> List[str]:
        """Process all field lines and return formatted results."""
        results = []
        for line in self._field_data.field_lines:
            value = self._root_class.get_value(line.path)
            formatted_value = self._format_value(value)
            if line.prefix or line.suffix:
                formatted_value = f"{line.prefix or ''}{formatted_value}{line.suffix or ''}"
            results.append(formatted_value)
        return results
