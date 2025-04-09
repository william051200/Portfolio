from typing import Dict, Any
from models.field_data import FieldData
from models.field_line import FieldLine
from models.field_data_list import FieldDataList
from .file_reader import FileReader


class FieldProcessor:
    @staticmethod
    def create_field_data_list(json_data: Dict[str, Any]) -> FieldDataList:
        """Convert JSON data into a FieldDataList instance.

        Args:
            json_data (Dict[str, Any]): The parsed JSON data containing field data value

        Returns:
            FieldDataList: Processed FieldDataList object containing all field data
        """
        field_data_list = []

        # Process each field data entry
        for data in json_data:
            # Process field lines
            field_lines = [
                FieldLine(
                    path=line['path'],
                    prefix=line['prefix'],
                    suffix=line['suffix']
                )
                for line in data['field_line']
            ]

            # Create FieldData object
            field_data = FieldData(
                id=data['id'],
                name=data['name'],
                field_lines=field_lines
            )

            field_data_list.append(field_data)

        return FieldDataList(field_data_list)
