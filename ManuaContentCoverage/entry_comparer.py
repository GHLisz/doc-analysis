class EntryComparer:
    def __init__(self, base_entries, test_entries):
        self.base_entries = base_entries
        self.test_entries = test_entries

    @staticmethod
    def is_entry_intersect(base_entry, test_entry):
        intersection = set(base_entry.paragraph_list) \
                       & set(test_entry.paragraph_list)
        return len(intersection) > 0

    # need revision
    def compare(self, base_entries, test_entries):
        # return true if base_entries contains all test_entries
        return all(self.is_entry_intersect(base_entry, test_entry)
                   for test_entry in test_entries
                   for base_entry in base_entries)
