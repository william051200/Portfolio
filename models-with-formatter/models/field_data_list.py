from typing import List, Optional
from .field_data import FieldData

class FieldDataList:
    def __init__(self, field_data_list: List[FieldData]):
        self._field_data_list = field_data_list

    @property
    def field_data_list(self) -> List[FieldData]:
        return self._field_data_list

    @field_data_list.setter
    def field_data_list(self, value: List[FieldData]) -> None:
        self._field_data_list = value

    def get_field_data_by_id(self, id: int) -> Optional[FieldData]:
        """Get field data by its ID.

        Args:
            id (int): The ID of the field data to retrieve

        Returns:
            Optional[FieldData]: The field data with the specified ID, or None if not found
        """
        for field_data in self._field_data_list:
            if field_data.id == id:
                return field_data
        return None
