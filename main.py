from doc import Doc

class Foo:
    def __init__(self, s=None):
        self.s = s
        self.e = None
        print "init"

    def __str__(self):
        return str(self.s)

    def p(self, a):
        print str(a)
        return True

    @staticmethod
    def is_entry_intersect(base_entry, test_entry):
        return base_entry == test_entry

    # need revision
    def compare(self, base_entries, test_entries):
        # return true if base_entries contains all test_entries
        return all(self.is_entry_intersect(base_entry, test_entry)
                   for test_entry in test_entries
                   for base_entry in base_entries)



if __name__ == '__main__':
    # import sys
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    #
    # doc = Doc()
    # doc.stuff_entries()
    a = [1,2]
    b = [1,2,4]
    func = Foo().compare
    print func(b, a)

