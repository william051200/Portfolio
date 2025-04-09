from models.class_a import Class_A
from models.class_b import Class_B
from models.class_c import Class_C
from models.class_d import Class_D
from models.class_e import Class_E


class DummyGenerator:
    @staticmethod
    def generate_dummy_classes():
        # Initialize classes with fixed IDs
        class_e1 = Class_E()
        class_e1._id = "e111"
        class_e1.initialize_mappings()

        class_e2 = Class_E()
        class_e2._id = "e222"
        class_e2.initialize_mappings()

        class_e3 = Class_E()
        class_e3._id = "e333"
        class_e3.initialize_mappings()

        class_e4 = Class_E()
        class_e4._id = "e444"
        class_e4.initialize_mappings()

        class_c = Class_C()
        class_c._id = "c111"
        class_c._class_e = class_e1
        class_c.initialize_mappings()

        class_d1 = Class_D()
        class_d1._id = "d111"
        class_d1._class_e = [class_e2, class_e3]
        class_d1.initialize_mappings()

        class_d2 = Class_D()
        class_d2._id = "d222"
        class_d2._class_e = [class_e3, class_e4]
        class_d2.initialize_mappings()

        class_b = Class_B()
        class_b._id = "b111"
        class_b._class_c = class_c
        class_b._class_d = [class_d1, class_d2]
        class_b.initialize_mappings()

        class_a = Class_A()
        class_a._id = "a111"
        class_a._class_b = class_b
        class_a.initialize_mappings()

        return class_a
