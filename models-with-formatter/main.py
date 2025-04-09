from utils.dummy_generator import generate_dummy_classes
from utils.config_processor import ConfigProcessor
from utils.field_processor import FieldProcessor
from utils.file_reader import FileReader
from processors.formatted_processor import FormattedProcessor
from models.value_processor import ValueProcessor


def main():
    # Initialize dummy classes
    class_a = generate_dummy_classes()

    # Read and process configuration files
    config_json = FileReader.read_json_file('output_config.json')
    delimiter_config = ConfigProcessor.create_delimiter_config(config_json)

    # Initialize the ValueProcessor singleton
    ValueProcessor.initialize(delimiter_config)

    # Process field data
    field_data_list = FieldProcessor.process_field_data('field_data.json')

    # Get field data with ID 2
    field_data = field_data_list.get_field_data_by_id(2)
    if not field_data:
        print("Field data with ID 2 not found")
        return

    # Create formatted processor
    processor = FormattedProcessor(field_data, delimiter_config, class_a)

    # Process and format the results
    formatted_results = processor.process_field_lines()

    # Print the formatted results
    print(f"Processing field data: {field_data.name}")
    for result in formatted_results:
        print(f"Formatted result: {result}")


if __name__ == "__main__":
    main()
