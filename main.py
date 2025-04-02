from processors.formatted_processor import FormattedProcessor
from utils.delimiter_reader import DelimiterReader

delimiter_config = DelimiterReader.read_config("output_config.json")
processor = FormattedProcessor("data.json", delimiter_config)
print("field1", processor.process_field("field1"))
print("field2", processor.process_field("field2"))
print("field3", processor.process_field("field3"))
print("field4", processor.process_field("field4"))
print("field5", processor.process_field("field5"))
print("field6", processor.process_field("field6"))
print("field7", processor.process_field("field7"))
print("field8", processor.process_field("field8"))
print("-------------------------------------------------")
print("all", processor.process_all_fields())
