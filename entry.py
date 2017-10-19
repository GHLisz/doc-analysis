import unittest


class Entry:
    def __init__(self, bookmark_name=None):
        self.bookmark_name = bookmark_name
        self.paragraph_list = []
        self.outline_level_list = []
        self.min_outline_level = 11

    def append_paragraph_outline_level(self, pair):
        para_num, outline_level = pair
        if para_num not in self.paragraph_list:
            self.paragraph_list.append(para_num)
            self.outline_level_list.append(outline_level)

            if self.min_outline_level > outline_level:
                self.min_outline_level = outline_level

    def __str__(self):
        r = "Entry object @ " + \
            self.bookmark_name + ';' + \
            str(self.paragraph_list) + ';' + \
            str(self.outline_level_list) + ';' + \
            str(self.min_outline_level)
        return r


class EntryTestCase(unittest.TestCase):
    def test_str(self):
        pass

if __name__ == '__main__':
    unittest.main()

