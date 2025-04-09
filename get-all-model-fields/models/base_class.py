import uuid
from typing import Any, Dict, List, Union, Callable


class BaseClass:
    def __init__(self):
        self._id = str(uuid.uuid4())

    @property
    def id(self) -> str:
        return self._id

    def get_all_members(self):
        """Get all properties and functions of the class"""
        result = {
            'simple': {},      # For simple types (str, int, float, bool)
            'objects': {},     # For objects with get_all_members
            'other': {},       # For objects without get_all_members
        }
        members = {}

        skip_methods = {
            'get_all_members',
            'get_formatter_mapping',
            'get_all',
            'get_by_key',
            'id'
        }

        for attr_name in dir(self):
            if attr_name.startswith('_') or attr_name in skip_methods:
                continue

            attr = getattr(self.__class__, attr_name)

            if isinstance(attr, property):
                value = attr.fget(self)

                # Handle list values
                if isinstance(value, list):
                    if not value:  # Empty list
                        # result['simple'][attr_name] = [value]
                        members[attr_name] = [value]
                    elif isinstance(value[0], (str, int, float, bool)):
                        # result['simple'][attr_name] = [value]
                        members[attr_name] = [value]
                    elif hasattr(value[0], 'get_all_members'):
                        # result['objects'][attr_name] = \
                        #     [item.get_all_members() for item in value]
                        members[attr_name] = \
                            [item.get_all_members() for item in value]
                    else:
                        # result['other'][attr_name] = \
                        #     [str(item) for item in value]
                        members[attr_name] = \
                            [str(item) for item in value]
                # Handle non-list values
                else:
                    if isinstance(value, (str, int, float, bool)):
                        # result['simple'][attr_name] = value
                        members[attr_name] = value
                    elif hasattr(value, 'get_all_members'):
                        # result['objects'][attr_name] = value.get_all_members()
                        members[attr_name] = value.get_all_members()
                    elif value is not None:  # Skip None values
                        # result['other'][attr_name] = str(value)
                        members[attr_name] = str(value)
            # Handle functions
            elif callable(attr) and not isinstance(attr, type):
                try:
                    value = attr(self)

                    # Handle function returning list
                    if isinstance(value, list):
                        if not value:  # Empty list
                            members[attr_name] = [value]
                        elif isinstance(value[0], (str, int, float, bool)):
                            members[attr_name] = [value]
                        elif hasattr(value[0], 'get_all_members'):
                            members[attr_name] = [item.get_all_members()
                                                  for item in value]
                        else:
                            members[attr_name] = [str(item) for item in value]

                    # Handle non-list return values
                    else:
                        if isinstance(value, (str, int, float, bool)):
                            members[attr_name] = value
                        elif hasattr(value, 'get_all_members'):
                            members[attr_name] = value.get_all_members()
                        elif value is not None:  # Skip None values
                            members[attr_name] = str(value)
                except Exception as e:
                    members[attr_name] = f"Error executing: {str(e)}"

        # return result
        return members
