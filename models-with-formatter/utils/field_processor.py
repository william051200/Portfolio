from typing import List
from models.field_data import FieldData
from models.field_line import FieldLine
from models.field_data_list import FieldDataList
from .file_reader import FileReader


class FieldProcessor:
    @staticmethod
    def process_field_data(file_path: str) -> FieldDataList:
        """Process field data from JSON file into FieldDataList object.

        Args:
            file_path (str): Path to the field data JSON file

        Returns:
            FieldDataList: Processed FieldDataList object containing all field data
        """
        # Read JSON file
        json_data = FileReader.read_json_file(file_path)

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
