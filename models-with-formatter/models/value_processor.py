from typing import Any, Dict, List, Union
from enums.mapping_type import MappingType
from models.delimiter_config import DelimiterConfig

class ValueProcessor:
    _instance = None
    _delimiter_config = None

    def __init__(self):
        if ValueProcessor._instance is not None:
            raise Exception("ValueProcessor is a singleton class. Use get_instance() to access it.")

    @classmethod
    def initialize(cls, delimiter_config: DelimiterConfig) -> None:
        """Initialize the ValueProcessor with delimiter configuration."""
        if cls._instance is None:
            cls._instance = cls()
            cls._delimiter_config = delimiter_config

    @classmethod
    def get_instance(cls) -> 'ValueProcessor':
        """Get the singleton instance of ValueProcessor."""
        if cls._instance is None:
            raise Exception("ValueProcessor not initialized. Call initialize() first.")
        return cls._instance

    @property
    def delimiter_config(self) -> DelimiterConfig:
        return self._delimiter_config

    def process_function_mapping(self, value: Any) -> Any:
        """Process a function mapping by executing the function."""
        return value()

    def process_property_mapping(self, value: Any, instance) -> Any:
        """Process a property mapping by getting its value."""
        if isinstance(value, property):
            return value.fget(instance)
        return value

    def process_child_mapping(self, child) -> Dict[str, Any]:
        """Process a child object's mappings recursively."""
        child_result = {}
        for name, mapping in child._mapping_manager.get_mapping().items():
            mapping_type = mapping["type"]
            value = mapping["value"]

            if mapping_type == MappingType.FUNCTION:
                child_result[name] = self.process_function_mapping(value)
            elif mapping_type == MappingType.PROPERTY:
                child_result[name] = self.process_property_mapping(value, child)
            else:  # CHILD type
                child_result[name] = value.get_value([])
        return child_result

    def process_mapping(self, mapping_type: MappingType, value: Any, instance) -> Any:
        """Process a single mapping based on its type."""
        if mapping_type == MappingType.FUNCTION:
            return self.process_function_mapping(value)
        elif mapping_type == MappingType.PROPERTY:
            return self.process_property_mapping(value, instance)
        else:  # CHILD type
            return self.process_child_mapping(value)

    def to_string(self, value: Any) -> str:
        """Convert a value to string using the configured delimiters."""
        if isinstance(value, dict):
            items = []
            for k, v in value.items():
                item_str = f"{k}{self.delimiter_config.key_value_separator}{self.to_string(v)}"
                items.append(item_str)
            return f"{self.delimiter_config.object_start}{self.delimiter_config.object_separator.join(items)}{self.delimiter_config.object_end}"
        elif isinstance(value, list):
            items = [self.to_string(item) for item in value]
            return f"{self.delimiter_config.array_start}{self.delimiter_config.array_separator.join(items)}{self.delimiter_config.array_end}"
        else:
            return str(value)