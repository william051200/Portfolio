import json
from typing import Dict, Any


class FileReader:
    @staticmethod
    def read_json_file(file_path: str) -> Dict[str, Any]:
        """Read and parse a JSON file.

        Args:
            file_path (str): Path to the JSON file

        Returns:
            Dict[str, Any]: Parsed JSON data as a dictionary

        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON in file {file_path}: {str(e)}", e.doc, e.pos)
