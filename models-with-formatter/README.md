# Models With Formatter

An advanced Python module that combines field retrieval with sophisticated formatting capabilities. This module extends the field mapping functionality to include customizable output formatting, delimiters, and text processing options.

## Features

- Configurable field formatting with prefix and suffix support
- Custom delimiter configuration for arrays and objects
- Multiple formatter configurations support
- Simplified output options
- Flexible field path navigation

## Class Structure

Enhances the base class hierarchy with formatting capabilities:

```
Class_A
├── class_b (Class_B)
│   ├── class_c (Class_C)
│   │   └── class_e (Class_E)
│   └── class_d[] (Array of Class_D)
│       └── class_e (Class_E)
```

## Configuration

### Field Data Configuration

```json
{
  "id": 1,
  "name": "Example Formatter",
  "field_data": [
    {
      "path": ["get_result"],
      "prefix": "Result: ",
      "suffix": " (processed)",
      "simplified": true
    }
  ]
}
```

### Output Configuration

```json
{
  "delimiters": {
    "array_start": "[",
    "array_end": "]",
    "array_separator": ",",
    "object_start": "{",
    "object_end": "}",
    "object_separator": ",",
    "key_value_separator": ":",
    "result_separator": "/"
  }
}
```

## Usage

```python
from models.class_a import Class_A
from utils.dummy_generator import DummyGenerator
from utils.config_processor import ConfigProcessor
from utils.field_processor import FieldProcessor
from utils.file_reader import FileReader
from processors.formatted_processor import FormattedProcessor
from models.value_processor import ValueProcessor

# Initialize dummy classes
    class_a = DummyGenerator.generate_dummy_classes()

    # Read and process delimiter configuration files
    delimiter_config_json = FileReader.read_json_file('delimiter_config.json')
    delimiter_config = ConfigProcessor.create_delimiter_config(
        delimiter_config_json
    )

    # Initialize the ValueProcessor singleton
    ValueProcessor.initialize(delimiter_config)

    # Read and process field data files
    field_data_json = FileReader.read_json_file('field_data.json')
    field_data_list = FieldProcessor.create_field_data_list(field_data_json)

    # Get field data with ID 2
    field_data = field_data_list.get_field_data_by_id(2)

    # Create formatted processor
    processor = FormattedProcessor(field_data, delimiter_config, class_a)

    # Process and format the results
    formatted_results = processor.process_field_lines()
```

## Implementation Details

### Core Components

- `models/`: Enhanced class definitions with formatting support
- `processors/`: Field processing and formatting logic
- `utils/`: Configuration and helper utilities
- `enums/`: Type definitions and constants

### Key Features

- **Formatter Configuration**: Define multiple formatter profiles
- **Delimiter Customization**: Customize output format and structure
- **Text Processing**: Add prefixes and suffixes to field values
- **Simplified Output**: Option for simplified data representation

## Example Output

```python
# Example formatted output
[
    'C1-{number/{2/end/{E}}/{array/{E}/{E}}/{array/{E}/{E}}}',
    'C2-{number/{2/end/{E}}/{array/{E}/{E}}/{array/{E}/{E}}}'
]
```

This module provides the most comprehensive field processing capabilities, combining field selection with advanced formatting options for flexible output generation.
