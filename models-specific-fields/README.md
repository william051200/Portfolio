# Models Specific Fields

A Python module that extends the base field retrieval functionality to support specific field selection and mapping. This module allows you to retrieve targeted fields from the class hierarchy using predefined paths.

## Features

- Selective field retrieval based on specified paths
- Support for field mapping and type conversion
- Enhanced control over field access patterns
- Configurable field selection strategies

## Class Structure

Builds upon the base class hierarchy with additional mapping functionality:

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
from utils.dummy_generator import DummyGenerator

# Generate dummy data
class_a = DummyGenerator.generate_dummy_classes()

class_a_value = class_a.get_value([])

# Get specific fields
result = class_a.get_value(['get_result'])
c111 = class_a.get_value(['b111', 'c111'])
```

## Implementation Details

### Core Components

- `models/`: Enhanced class definitions with mapping support
- `utils/`: Utility functions for field processing
- `enums/`: Mapping type definitions and configurations
- `main.py`: Example implementation and usage patterns

### Key Features

- **Field Mapping**: Define custom paths to specific fields
- **Type Conversion**: Support for automatic type conversion
- **Array Handling**: Special handling for array-type fields
- **Nested Access**: Deep access to nested class structures

## Example Output

```python
# Example output from get_mapped_fields()
{
  'get_count': 'count',
  'get_result': 'result',
  'b111': {
    'get_number': 'number',
    'c111': {
      'get_number': '2',
      'get_end': 'end',
      'e111': {
        'get_E': 'E'
      }
    },
    'd111': {
      'get_array': 'array',
      'e222': {
        'get_E': 'E'
      },
      'e333': {
        'get_E': 'E'
      }
    },
    'd222': {
      'get_array': 'array',
      'e333': {
        'get_E': 'E'
      },
      'e444': {
        'get_E': 'E'
      }
    }
  }
}
```

This module provides a more targeted approach to field retrieval, allowing for specific field selection and custom mapping strategies.
