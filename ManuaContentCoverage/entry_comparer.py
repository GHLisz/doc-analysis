class EntryComparer:
    def __init__(self, base_entries, test_entries):
        # base entries: MC, test_entries: TOC
        self.base_entries = base_entries
        self.test_entries = test_entries

    @staticmethod
    def is_entry_intersect(base_entry, test_entry):
        intersection = set(base_entry.paragraph_list) \
                       & set(test_entry.paragraph_list)
        return len(intersection) > 0

    # need revision
    def compare(self):
        # return true if base_entries contains all test_entries
        is_test_entry_contained = [any(self.is_entry_intersect(entry, base_entry) for base_entry in self.base_entries)
                                   for entry in self.test_entries if entry.paragraph_list]
        return all(is_test_entry_contained)

    def diff_info(self):
        result = []
        for test_entry in self.test_entries:
            if test_entry.paragraph_list:
                if not any(self.is_entry_intersect(test_entry, base_entry) for base_entry in self.base_entries):
                    result.append(test_entry)
        return result
