# 🔧 Formatter System

A flexible Python system for processing and formatting nested class data with configurable paths and formatting options, including multiple formatter configurations.

## ⚙️ Configuration

### Field Data Configuration

The system uses a JSON configuration file (`field_data.json`) to define formatters and their processing fields:

```json
[
  {
    "id": 1,
    "name": "Formatter One",
    "field_data": [
      {
        "path": ["get_result"],
        "prefix": "A",
        "suffix": "B",
        "simplified": true
      }
    ]
  }
]
```

#### Field Data Configuration Properties

| Property     | Type    | Description                         |
| ------------ | ------- | ----------------------------------- |
| `id`         | Integer | Unique identifier for the formatter |
| `name`       | String  | Name of the formatter configuration |
| `field_data` | Array   | Array of field configurations       |

| Property     | Type    | Description                               |
| ------------ | ------- | ----------------------------------------- |
| `path`       | Array   | Steps to navigate through class hierarchy |
| `prefix`     | String  | Text to prepend to result (optional)      |
| `suffix`     | String  | Text to append to result (optional)       |
| `simplified` | Boolean | Flag to enable simplified output          |

### Output Data Configuration

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
    "result_separator": "/"
  }
}
```

#### Output Configuration Properties

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
# Read configurations
delimiter_config = DelimiterReader.read_config("output_config.json")
formatters = FieldReader.read_formatters("field_data.json")

# Get formatter by ID
formatter_id = 2
formatter = FieldReader.get_formatter_by_id(formatters, formatter_id)

# Or get formatter by name
formatter_name = "Formatter One"
formatter = FieldReader.get_formatter_by_name(formatters, formatter_name)

# Process fields
processor = FormattedProcessor(formatter, delimiter_config)
result = processor.process_all_fields()
```

## 🔍 Available Fields

Each formatter can define its own set of fields with custom paths, prefixes, and suffixes. Common field paths include:

| Path                        | Description                       |
| --------------------------- | --------------------------------- |
| `["get_result"]`            | Direct access to Class_A's result |
| `["get_count"]`             | Direct access to Class_A's count  |
| `["class_b", "get_number"]` | Access Class_B's number           |
| `["class_b", "class_c"]`    | Access Class_B's Class_C instance |
| `["class_b", "class_d"]`    | Access Class_D array              |

## License

This project is licensed under the MIT License.
