from processors.formatted_processor import FormattedProcessor
from utils.delimiter_reader import DelimiterReader
from utils.field_reader import FieldReader

delimiter_config = DelimiterReader.read_config("output_config.json")
field_list = FieldReader.read_fields("field_data.json")
processor = FormattedProcessor(field_list, delimiter_config)

# # Process each field dynamically
# for i in range(field_list.count):
#     print(f"field{i+1}", processor.process_field_by_index(i))

# print("-------------------------------------------------")
result = processor.process_all_fields()
# Use the configurable separator from delimiter_config
print(delimiter_config.result_separator.join(result))

# print("all", processor.process_all_fields())
