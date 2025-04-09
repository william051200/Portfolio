from utils.dummy_generator import generate_dummy_classes

class_a = generate_dummy_classes()
# result = class_a.get_value(['b111'])
# result = class_a.get_value(['b111', 'get_number'])
result = class_a.get_value(['b111', 'c111'])
result = class_a.get_value(['b111', 'c111', 'get_number'])
print('result', result)
