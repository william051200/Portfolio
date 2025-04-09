from typing import Dict, Any
from models.delimiter_config import DelimiterConfig


class ConfigProcessor:
    @staticmethod
    def create_delimiter_config(json_data: Dict[str, Any]) -> DelimiterConfig:
        """Convert JSON data into a DelimiterConfig instance.

        Args:
            json_data (Dict[str, Any]): The parsed JSON data containing delimiter configurations

        Returns:
            DelimiterConfig: A configured DelimiterConfig instance

        Raises:
            KeyError: If required delimiter configurations are missing
        """
        try:
            delimiters = json_data['delimiters']
            config = DelimiterConfig()

            config.array_start = delimiters['array_start']
            config.array_end = delimiters['array_end']
            config.array_separator = delimiters['array_separator']
            config.object_start = delimiters['object_start']
            config.object_end = delimiters['object_end']
            config.object_separator = delimiters['object_separator']
            config.key_value_separator = delimiters['key_value_separator']
            config.result_separator = delimiters['result_separator']

            return config
        except KeyError as e:
            raise KeyError(
                f"Missing required delimiter configuration: {str(e)}")
