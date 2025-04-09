from utils.dummy_generator import DummyGenerator

# Generate dummy data
class_a = DummyGenerator.generate_dummy_classes()

class_a_value = class_a.get_value([])

# Get specific fields
result = class_a.get_value(['get_result'])
c111 = class_a.get_value(['b111', 'c111'])
