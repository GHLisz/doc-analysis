import unittest


class ResultBuilder:
    def __init__(self, doc_name, raw_sentence_data, raw_para_data, result_path):
        self.doc_name = str(doc_name)
        self.raw_sentence_data = raw_sentence_data
        self.raw_para_data = raw_para_data
        self.result_path = str(result_path)

        self.general_result_file = self.result_path + '\general_' + self.doc_name + '.txt'
        self.sentence_result_file = self.result_path + '\sentence_' + self.doc_name + '.txt'
        self.paragraph_result_file = self.result_path + '\paragraph_' + self.doc_name + '.txt'


    def save_all_result(self):
        save_general_result = self.save_result_abs(self.general_result_file,
                                                   self.raw_para_data,
                                                   self.get_general_results_by_key)
        save_sent_result = self.save_result_abs(self.sentence_result_file,
                                                self.raw_sentence_data,
                                                self.get_sent_para_results_by_key,
                                                'S')
        save_para_result = self.save_result_abs(self.paragraph_result_file,
                                                self.raw_para_data,
                                                self.get_sent_para_results_by_key,
                                                'P')
        return all([save_general_result, save_sent_result, save_para_result])

    @staticmethod
    def save_result_abs(filename, raw_data, get_by_key, key_prefix='k'):
        import codecs
        f = codecs.open(filename, 'w', 'utf_8_sig')
        for key in raw_data.keys():
            r = get_by_key(key, raw_data, key_prefix)
            for entry in r:
                line = '|'.join(entry)
                f.write(line + '\n')
        f.close()
        return True

    def get_sent_para_results_by_key(self, key, raw_data, key_prefix='k'):
        prop_list = raw_data[key]
        hashed_prop_list = [";".join([str(i) for i in p]) for p in prop_list]
        occurrence = self.count_occurrence(hashed_prop_list)
        ordered_value = self.order_dic_by_value(occurrence)

        style_id, level = key
        idx = 1
        return_val = []
        for v in ordered_value:
            props, cnt = v
            return_val.append(map(str, [self.doc_name,
                                        style_id,
                                        level,
                                        (key_prefix + str(idx)),
                                        props,
                                        cnt]))
            idx += 1
        return return_val


    def get_general_results_by_key(self, key, raw_data=None, key_prefix='k'):
        para_prop_list = self.raw_para_data[key]
        sent_prop_list = self.raw_sentence_data[key]
        hashed_para_prop_list = [";".join([str(i) for i in para]) for para in para_prop_list]
        hashed_sent_prop_list = [";".join([str(i) for i in sent]) for sent in sent_prop_list]
        para_prop_set = set(hashed_para_prop_list)
        sent_prop_set = set(hashed_sent_prop_list)

        style_id, level = key
        sent_prop_homogeneity = 1 if len(sent_prop_set) == 1 else 0
        para_prop_homogeneity = 1 if len(para_prop_set) == 1 else 0
        sent_count = len(sent_prop_list)
        para_count = len(para_prop_list)

        sent_stat = self.lst_to_stat(hashed_sent_prop_list, 5, 'S')
        para_stat = self.lst_to_stat(hashed_para_prop_list, 5, 'P')

        return [map(str, [self.doc_name,
                         style_id,
                         level,
                         sent_prop_homogeneity,
                         para_prop_homogeneity,
                         sent_count,
                         para_count,
                         sent_stat,
                         para_stat,])]


    def lst_to_stat(self, lst, n, key_prefix='k'):
        occurrence = self.count_occurrence(lst)
        ordered_value = self.order_dic_by_value(occurrence)
        fmted = self.fmt_first_n_stat(ordered_value, n, key_prefix)
        return fmted

    @staticmethod
    def count_occurrence(lst):
        lst = list(lst)
        return dict((i, lst.count(i)) for i in set(lst))

    @staticmethod
    def order_dic_by_value(dic):
        return sorted(dic.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def fmt_first_n_stat(lst_of_kv_pair, n, key_prefix):
        new_lst_of_kv_pair = []
        total = reduce(lambda accum, item: accum+item[1], lst_of_kv_pair, 0)
        key_index = 1
        for k, v in lst_of_kv_pair:
            key_literal = key_prefix + str(key_index)
            percentage = '%.4f'%(v / float(total))
            new_lst_of_kv_pair.append((key_literal, percentage))
            key_index += 1

        to_fmt = new_lst_of_kv_pair[:n] if len(new_lst_of_kv_pair) > n else new_lst_of_kv_pair
        out_str = ';'.join([str(pair[0])+':'+str(pair[1]) for pair in to_fmt])
        return out_str


class ResultBuilderTestCase(unittest.TestCase):
    def setUp(self):
        doc_name = "1.doc"
        raw_sentence_data = {(1, 2):[['bi', 1, False], ['b', 3, True], ['b', 3, True], ['i', 3, True], ['i', 5, True], ['i', 6, True], ['i', 7, True]],
                             (3, 5):[['i', 5, True]],}
        raw_para_data = {(1, 2):[['bi', 1, False], ['bi', 1, False], ['bi', 1, False], ['bi', 1, False]],
                             (3, 5):[['i', 5, True]],}
        self.rb = ResultBuilder(doc_name, raw_sentence_data, raw_para_data, 'D:/TMP/')

    def test_get_sent_para_results_by_key(self):
        para_r = self.rb.get_sent_para_results_by_key((1, 2), self.rb.raw_para_data)
        self.assertEqual(para_r, [['1.doc', '1', '2', 'k1', 'bi;1;False', '4']])
        sent_r = self.rb.get_sent_para_results_by_key((1, 2), self.rb.raw_sentence_data)
        self.assertEqual(sent_r, [['1.doc', '1', '2', 'k1', 'b;3;True', '2'],
                                  ['1.doc', '1', '2', 'k2', 'i;6;True', '1'],
                                  ['1.doc', '1', '2', 'k3', 'i;3;True', '1'],
                                  ['1.doc', '1', '2', 'k4', 'bi;1;False', '1'],
                                  ['1.doc', '1', '2', 'k5', 'i;7;True', '1'],
                                  ['1.doc', '1', '2', 'k6', 'i;5;True', '1']])

    def test_get_general_results_by_key(self):
        s = self.rb.get_general_results_by_key((1, 2))
        self.assertEqual(s, [['1.doc', '1', '2', '0', '1', '7', '4', 'S1:0.2857;S2:0.1429;S3:0.1429;S4:0.1429;S5:0.1429', 'P1:1.0000']])

    def test_order_dic_by_value(self):
        a = {'c':1, 'a':2, 'b':3}
        b = ResultBuilder.order_dic_by_value(a)
        self.assertEqual(b, [('b', 3), ('a', 2), ('c', 1)])

    def test_fmt_first_n_stat(self):
        a = [('b', 3), ('a', 2), ('c', 1), (1, 0), (True, 19)]
        b = ResultBuilder.fmt_first_n_stat(a, 3, 'p')
        self.assertEqual(b,  'p1:0.1200;p2:0.0800;p3:0.0400')

    def test_count_occurrence(self):
        a = ['a', 'b', 'a', 'c', 'c', 'a']
        b = ResultBuilder.count_occurrence(a)
        self.assertEqual(b, {'a': 3, 'c': 2, 'b': 1})

    def test_lst_to_stat(self):
        func = ResultBuilder(None, None, None, None).lst_to_stat
        a = ['a', 'b', 'a', 'c', 'c', 'a']
        b = func(a, 2, 'p')
        self.assertEqual(b, 'p1:0.5000;p2:0.3333')

    def test_save_all_result(self):
        r = self.rb.save_all_result()


if __name__ == '__main__':
    unittest.main()
