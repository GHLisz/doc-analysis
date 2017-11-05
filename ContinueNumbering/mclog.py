#coding=utf-8
import unittest


class MCLog:
    def __init__(self, log_path = "d:/tmp/log.txt"):
        # require a running wps instance
        self.log_path = log_path
        self.get_mclog(self.log_path)
        self.range_list_of_level = self.parse_mclog(self.parse_mclog_line, self.log_path)


    @staticmethod
    def get_mclog(log_path):
        import xmlrpclib
        wps_app = xmlrpclib.ServerProxy(u"http://127.0.0.1:60000")
        r = wps_app.ExportManualContentLog(log_path)
        return True

    @staticmethod
    def parse_mclog(parse_mclog_line, log_path):
        f = open(log_path)
        level_range_pair_list = [parse_mclog_line(line) for line in f.readlines()]

        from collections import defaultdict
        range_list_of_level = defaultdict(list)
        for style_id, level, begin, end, contains_numbering in level_range_pair_list:
            if contains_numbering:
                range_list_of_level[(style_id, level)].append((begin, end))

        return range_list_of_level

    @staticmethod
    def parse_mclog_line(line_str):
        l = line_str.split('|')
        style_id = str(l[-4])
        level = int(l[2])
        range_begin = int(l[-2])
        range_end = int(l[-1])
        contains_numbering = False if l[4] == '0' else True
        return [style_id, level, range_begin, range_end, contains_numbering]



class MCLogTestCase(unittest.TestCase):
    def test_parse_mclog_line(self):
        r = MCLog.parse_mclog_line(u"12|元糖糖糖|1|1|0|230|1|0|1|0|440|0|0|0|336|341")
        self.assertEqual(r, ['0', 1, 336, 341, False])
        r = MCLog.parse_mclog_line("10|Afsdafdrtasrg、、|2|0.9997|1|230|15|65|1|0|440|0|0|0|319|335")
        self.assertEqual(r, ['0', 2, 319, 335, True])

    def test_parse_mclog(self):
        dic = MCLog.parse_mclog(MCLog.parse_mclog_line, "d:/tmp/log.txt")
        print dic


if __name__ == '__main__':
    # main()
    unittest.main()
