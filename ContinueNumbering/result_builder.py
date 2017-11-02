import unittest


class ResultBuilder:
    def __init__(self, doc_name, raw_sentence_data, raw_para_data):
        self.doc_name = doc_name
        self.raw_sentence_data = raw_sentence_data
        self.raw_para_data = raw_para_data
        # self.raw_sentence_data_by_key = {}
        # self.raw_para_data_by_key = {}

    def get_general_result_by_key(self, key):
        para_prop_list = self.raw_para_data[key]
        sent_prop_list = self.raw_sentence_data[key]
        hashed_para_prop_list = (";".join([str(i) for i in para]) for para in para_prop_list)
        hashed_sent_prop_list = (";".join([str(i) for i in sent]) for sent in sent_prop_list)
        para_prop_set = set(hashed_para_prop_list)
        sent_prop_set = set(hashed_sent_prop_list)

        style_id = key[0]
        level = key[1]
        sent_prop_homogeneity = 1 if len(sent_prop_set) == 1 else 0
        para_prop_homogeneity = 1 if len(para_prop_set) == 1 else 0
        sent_count = len(sent_prop_list)
        para_count = len(para_prop_list)

        para_stat = {}
        for kind in para_prop_set:
            pass

        return map(str, [self.doc_name,
                         style_id,
                         level,
                         sent_prop_homogeneity,
                         para_prop_homogeneity,
                         sent_count,
                         para_count,])


    def restructure_data_by_key(self):
        for k, v in self.raw_sentence_data:
            pass



class ResultBuilderTestCase(unittest.TestCase):
    def test_get_general_result_by_key(self):
        doc_name = "1.doc"
        raw_sentence_data = {(1, 2):[['bi', 1, False], ['b', 3, True], ['b', 3, True]],
                             (3, 5):[['i', 5, True]],}
        raw_para_data = {(1, 2):[['bi', 1, False], ['bi', 1, False], ['bi', 1, False], ['bi', 1, False]],
                             (3, 5):[['i', 5, True]],}
        rb = ResultBuilder(doc_name, raw_sentence_data, raw_para_data)
        s = rb.get_general_result_by_key((1, 2))
        self.assertEqual(s, ['1.doc', '1', '2', '0', '1', '3', '4'])

if __name__ == '__main__':
    unittest.main()
