from processors.formatted_processor import FormattedProcessor

processor = FormattedProcessor("data.json")
print("combo1", processor.process_combo("combo1"))
print("combo2", processor.process_combo("combo2"))
print("combo3", processor.process_combo("combo3"))
print("combo4", processor.process_combo("combo4"))
print("combo5", processor.process_combo("combo5"))
print("combo6", processor.process_combo("combo6"))
print("combo7", processor.process_combo("combo7"))
print("combo8", processor.process_combo("combo8"))
print("-------------------------------------------------")
print("all", processor.process_all_combos())
