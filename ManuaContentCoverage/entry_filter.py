class EntryFilter:
    def __init__(self, entries):
        self.entries = entries
        self.min_3_outline_level = self.get_min_3_outline_level()
        self.entries = self.filter_entries(self.entries)

    def get_min_3_outline_level(self):
        outline_levels = [e.min_outline_level for e in self.entries]
        outline_levels.sort()
        return outline_levels[0:3]

    def is_valid_entry(self, entry):
        # the following will fail:
        # paragraph outline level is 10
        # paragraph text contains no chinese characters
        # paragraph outline level not in first 3
        return entry.paragraph_list \
               and entry.outline_level_list \
               and (entry.min_outline_level < 10)\
               and (entry.min_outline_level in self.min_3_outline_level)

    def filter_entries(self, entries):
        return [entry for entry in entries if self.is_valid_entry(entry)]
