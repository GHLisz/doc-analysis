#coding=utf-8

import unittest


class CharSetUtil:
    def __init__(self):
        self.CHINESE_UNICODE_SET = [[0x4E00, 0x9FA5], [0x9FA6, 0x9FCB], [0x3400, 0x4DB5], [0x20000, 0x2A6D6],
                                   [0x2A700, 0x2B734], [0x2B740, 0x2B81D], [0x2F00, 0x2FD5], [0x2E80, 0x2EF3],
                                   [0xF900, 0xFAD9], [0x2F800, 0x2FA1D], [0xE815, 0xE86F], [0xE400, 0xE5E8],
                                   [0xE600, 0xE6CF], [0x31C0, 0x31E3], [0x2FF0, 0x2FFB], [0x3105, 0x3120],
                                   [0x31A0, 0x31BA], [0x3007, 0x3007]]

    def is_cn_char(self, character):
        return any(start <= ord(character) <= end for start, end in self.CHINESE_UNICODE_SET)

    def contains_cn(self, string):
        return any(self.is_cn_char(character) for character in string)


class CharSetUtilTestCase(unittest.TestCase):
    def test_is_cn_char(self):
        u = CharSetUtil()
        self.assertTrue(u.is_cn_char(u"山"))
        self.assertFalse(u.is_cn_char("a"))

    def test_contains_cn(self):
        u = CharSetUtil()
        self.assertTrue(u.contains_cn(u'eff6水g'))
        self.assertFalse(u.contains_cn(u'678ie'))

if __name__ == '__main__':
    unittest.main()
