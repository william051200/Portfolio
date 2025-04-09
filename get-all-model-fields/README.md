# Get All Model Fields

A Python module for retrieving and processing all fields from a hierarchical class structure. This module provides a basic implementation for traversing through nested class instances and collecting their field values.

## Features

- Automatic field discovery and extraction from nested class structures
- Support for handling multiple class types (Class_A through Class_E)
- Basic field value retrieval without formatting
- Comprehensive class hierarchy traversal

## Class Structure

The module works with the following class hierarchy:

```
Class_A
├── class_b (Class_B)
│   ├── class_c (Class_C)
│   │   └── class_e (Class_E)
│   └── class_d[] (Array of Class_D)
│       └── class_e (Class_E)
```

## Usage

```python
from models.class_a import Class_A
from utils.dummy_generator import DummyGenerator

# Generate dummy data
class_a = DummyGenerator.generate_dummy_classes()

# Get all fields
all_fields = class_a.get_all_members()

# Access specific fields
result = class_a.get_result
count = class_a.get_count()
```

## Implementation Details

### Core Components

- `models/`: Contains the class definitions (Class_A through Class_E)
- `utils/`: Contains helper utilities including the dummy data generator
- `main.py`: Example implementation and usage demonstration

### Key Methods

Each class implements the following methods:

- `get_all_members()`: Returns a dictionary containing all fields and their values
- Class-specific getter methods (e.g., `get_result`, `get_count()`, etc.)

## Example Output

```python
# Example output from get_all_members()
{
  'class_b': {
    'class_c': {
      'class_e': {
        'get_E': 'E'
      },
      'get_end': 'end',
      'get_number': '2'
    },
    'class_d': [
      {
        'class_e': [
          {
            'get_E': 'E'
          }
        ],
        'get_array': 'array'
      }
    ],
    'get_number': 'number',
    'get_xyz': 'xyz'
  },
  'get_abc': 'abc',
  'get_count': 'count',
  'get_result': 'result',
  'get_tail': 'tail'
}
```

This module serves as the foundation for more advanced field processing implementations in the project.
