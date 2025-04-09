from utils.dummy_generator import DummyGenerator

# Generate dummy data
class_a = DummyGenerator.generate_dummy_classes()

# Get all fields
all_fields = class_a.get_all_members()

# Access specific fields
result = class_a.get_result
count = class_a.get_count()

print(all_fields)
