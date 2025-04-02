# 🔧 Formatter System

A flexible Python system for processing and formatting nested class data with configurable paths and formatting options, including a simplified output feature.

## ⚙️ Configuration

The system uses a JSON configuration file (`field_data.json`) to define processing fields:

```json
{
  "path": ["get_result"],
  "prefix": "Result: ",
  "suffix": " (from Class A)",
  "simplified": false
}
```

### Field Data Configuration Properties

| Property     | Type    | Description                               |
| ------------ | ------- | ----------------------------------------- |
| `path`       | Array   | Steps to navigate through class hierarchy |
| `prefix`     | String  | Text to prepend to result (optional)      |
| `suffix`     | String  | Text to append to result (optional)       |
| `simplified` | Boolean | Flag to enable simplified output          |

The system uses an output configuration file (`output_config.json`) to define delimiters for formatting results. This includes settings for arrays, objects, and the result separator.

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
    "result_separator": "/" // Configurable separator for joining results
  }
}
```

### Output Configuration Properties

| Property              | Type   | Description                                  |
| --------------------- | ------ | -------------------------------------------- |
| `array_start`         | String | Delimiter for the start of an array          |
| `array_end`           | String | Delimiter for the end of an array            |
| `array_separator`     | String | Separator between array elements             |
| `object_start`        | String | Delimiter for the start of an object         |
| `object_end`          | String | Delimiter for the end of an object           |
| `object_separator`    | String | Separator between object properties          |
| `key_value_separator` | String | Separator between keys and values            |
| `result_separator`    | String | Separator used to join results in the output |

## 🏗️ Architecture

### Core Components

- **Models**: Class definitions and data structures
- **Processors**: Processing and formatting logic
- **Utils**: Helper functions and utilities

### Processor Types

1. `FieldProcessor`

   - Navigates class hierarchy
   - Processes nested structures
   - Handles array operations

2. `FormattedProcessor`
   - Adds text formatting
   - Applies prefix/suffix
   - Formats final output
   - Handles simplified output

## 📊 Class Structure

### Class_A

```python
class Class_A:
    # Properties
    class_b: Class_B        # Instance of Class_B
    get_result: str         # Returns "result"

    # Methods
    get_count() → str      # Returns "count"
    get_all() → dict       # Returns all values
```

### Class_B

```python
class Class_B:
    # Properties
    class_c: Class_C        # Instance of Class_C
    class_d: List[Class_D]  # Array of Class_D instances

    # Methods
    get_number() → str     # Returns "number"
    get_all() → dict       # Returns all values
```

### Class_C

```python
class Class_C:
    # Properties
    class_e: Class_E        # Instance of Class_E

    # Methods
    get_end() → str       # Returns "end"
    get_all() → dict      # Returns all values
```

### Class_D

```python
class Class_D:
    # Properties
    class_e: Class_E        # Instance of Class_E

    # Methods
    get_array() → str     # Returns "array"
    get_all() → dict      # Returns all values
```

### Class_E

```python
class Class_E:
    # Methods
    get_E() → str        # Returns "E"
    get_all() → dict     # Returns all values
```

## 💻 Usage Examples

```python
# Basic Usage
from processors.formatted_processor import FormattedProcessor
from utils.delimiter_reader import DelimiterReader
from utils.field_reader import FieldReader

delimiter_config = DelimiterReader.read_config("output_config.json")
field_list = FieldReader.read_fields("field_data.json")
processor = FormattedProcessor(field_list, delimiter_config)

# # Process each field dynamically
for i in range(field_list.count):
  result = processor.process_field_by_index(i)

# Batch Processing
all_results = processor.process_all_fields()
delimiter_config.result_separator.join(all_results)
```

## 🔍 Available Fields

| Field    | Path                                   | Description                       |
| -------- | -------------------------------------- | --------------------------------- |
| `field1` | `["get_result"]`                       | Direct access to Class_A's result |
| `field2` | `["get_count"]`                        | Direct access to Class_A's count  |
| `field3` | `["class_b", "get_number"]`            | Access Class_B's number           |
| `field4` | `["class_b", "class_c"]`               | Access Class_B's Class_C instance |
| `field5` | `["class_b", "class_c", "get_number"]` | Access Class_C's number           |
| `field6` | `["class_b", "class_d"]`               | Access Class_D array              |
| `field7` | `["class_b", "class_d", "get_array"]`  | Get arrays from Class_D instances |
| `field8` | `["class_b"]`                          | Access Class_B instance           |

## License

This project is licensed under the MIT License.
