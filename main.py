from processors.formatted_processor import FormattedProcessor
from utils.delimiter_reader import DelimiterReader
from utils.field_reader import FieldReader

# Read configurations
delimiter_config = DelimiterReader.read_config("output_config.json")
formatters = FieldReader.read_formatters("field_data.json")

# # Get formatter by name
# formatter_name = "Formatter One"
# formatter_by_name = FieldReader.get_formatter_by_name(formatters, formatter_name)

# # Create processor with the selected formatter
# processor = FormattedProcessor(formatter_by_name, delimiter_config)

# Get formatter by ID
formatter_id = 2
formatter_by_id = FieldReader.get_formatter_by_id(formatters, formatter_id)

# Create processor with the selected formatter
processor = FormattedProcessor(formatter_by_id, delimiter_config)

# Process all fields
result = processor.process_all_fields()

# Output the result using the configured separator
print(delimiter_config.result_separator.join(result))
