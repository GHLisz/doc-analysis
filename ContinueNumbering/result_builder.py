#coding=utf-8
import unittest


class ResultBuilder:
    def __init__(self, doc_name, raw_sentence_data, raw_para_data, result_path):
        self.doc_name = str(doc_name)
        self.raw_sentence_data = raw_sentence_data
        self.raw_para_data = raw_para_data
        self.result_path = str(result_path)

        self.general_result_file = self.result_path + u'\总体_' + self.doc_name + '.txt'
        self.sentence_result_file = self.result_path + u'\句属性_' + self.doc_name + '.txt'
        self.paragraph_result_file = self.result_path + u'\段属性_' + self.doc_name + '.txt'
        self.sentence_text_result_file = self.result_path + u'\含文本句属性_' + self.doc_name + '.txt'
        self.paragraph_text_result_file = self.result_path + u'\含文本段属性_' + self.doc_name + '.txt'

    def save_all_result(self):
        save_general_result = self.save_result_abs(self.general_result_file,
                                                   self.raw_para_data,
                                                   self.get_general_results_by_key,
                                                   'k',
                                                   [u'文档名',
                                                    u'样式id',
                                                    u'级别（1-9）',
                                                    u'句属性相同',
                                                    u'段属性相同',
                                                    u'该级别句总数',
                                                    u'该级别段总数',
                                                    u'第一种句占比',
                                                    u'第二种句占比',
                                                    u'第三种句占比',
                                                    u'第四种句占比',
                                                    u'第五种段占比',
                                                    u'第一种段占比',
                                                    u'第二种段占比',
                                                    u'第三种段占比',
                                                    u'第四种段占比',
                                                    u'第五种段占比',])
        save_sent_result = self.save_result_abs(self.sentence_result_file,
                                                self.raw_sentence_data,
                                                self.get_sent_para_results_by_key,
                                                'S',
                                                [u'文档名',
                                                 u'样式id',
                                                 u'级别（1-9）',
                                                 u'句（段）属性类型id',
                                                 u'中文字体',
                                                 u'西文字体',
                                                 u'复杂文种',
                                                 u'复杂文种 - 粗体',
                                                 u'复杂文种 - 斜体',
                                                 u'复杂文种 - 字号',
                                                 u'粗体',
                                                 u'斜体',
                                                 u'字号',
                                                 u'下划线',
                                                 u'着重号',
                                                 u'删除线',
                                                 u'双删除线',
                                                 u'上标',
                                                 u'下标',
                                                 u'小型大写字母',
                                                 u'全部大写字符',
                                                 u'隐藏文字',
                                                 u'字符间距 - 缩放',
                                                 u'字符间距 - 间距',
                                                 u'字符间距 - 位置',
                                                 u'本类型的句（段）数量',])
        save_para_result = self.save_result_abs(self.paragraph_result_file,
                                                self.raw_para_data,
                                                self.get_sent_para_results_by_key,
                                                'P',
                                                [u'文档名',
                                                 u'样式id',
                                                 u'级别（1-9）',
                                                 u'句（段）属性类型id',
                                                 u'制表位个数',
                                                 u'制表位位置',
                                                 u'制表位对齐方式',
                                                 u'制表位前导符',
                                                 u'对齐方式',
                                                 u'大纲级别',
                                                 u'方向',
                                                 u'左缩进',
                                                 u'右缩进',
                                                 u'文本之前（后）',
                                                 u'首行缩进',
                                                 u'首行缩进',
                                                 u'段前间距',
                                                 u'段前间距',
                                                 u'段后间距',
                                                 u'段后间距',
                                                 u'行距',
                                                 u'行距',
                                                 u'孤行控制',
                                                 u'与下段同页',
                                                 u'段中不分页',
                                                 u'分页',
                                                 u'按中文习惯控制首尾字符',
                                                 u'允许西文在单词中间换行',
                                                 u'允许标点溢出边界',
                                                 u'允许行首标点压缩',
                                                 u'自动调整中文和西文的间距',
                                                 u'文本对齐方式',
                                                 u'本类型的句（段）数量',])
        save_sent_text_result = self.save_result_abs(self.sentence_text_result_file,
                                                self.raw_sentence_data,
                                                self.get_sent_para_results_with_text_by_key,
                                                'S',
                                                [u'文档名',
                                                 u'样式id',
                                                 u'级别（1-9）',
                                                 u'句（段）属性类型id',
                                                 u'文本',
                                                 u'中文字体',
                                                 u'西文字体',
                                                 u'复杂文种',
                                                 u'复杂文种 - 粗体',
                                                 u'复杂文种 - 斜体',
                                                 u'复杂文种 - 字号',
                                                 u'粗体',
                                                 u'斜体',
                                                 u'字号',
                                                 u'下划线',
                                                 u'着重号',
                                                 u'删除线',
                                                 u'双删除线',
                                                 u'上标',
                                                 u'下标',
                                                 u'小型大写字母',
                                                 u'全部大写字符',
                                                 u'隐藏文字',
                                                 u'字符间距 - 缩放',
                                                 u'字符间距 - 间距',
                                                 u'字符间距 - 位置',])
        save_para_text_result = self.save_result_abs(self.paragraph_text_result_file,
                                                self.raw_para_data,
                                                self.get_sent_para_results_with_text_by_key,
                                                'P',
                                                [u'文档名',
                                                 u'样式id',
                                                 u'级别（1-9）',
                                                 u'句（段）属性类型id',
                                                 u'文本',
                                                 u'制表位个数',
                                                 u'制表位位置',
                                                 u'制表位对齐方式',
                                                 u'制表位前导符',
                                                 u'对齐方式',
                                                 u'大纲级别',
                                                 u'方向',
                                                 u'左缩进',
                                                 u'右缩进',
                                                 u'文本之前（后）',
                                                 u'首行缩进',
                                                 u'首行缩进',
                                                 u'段前间距',
                                                 u'段前间距',
                                                 u'段后间距',
                                                 u'段后间距',
                                                 u'行距',
                                                 u'行距',
                                                 u'孤行控制',
                                                 u'与下段同页',
                                                 u'段中不分页',
                                                 u'分页',
                                                 u'按中文习惯控制首尾字符',
                                                 u'允许西文在单词中间换行',
                                                 u'允许标点溢出边界',
                                                 u'允许行首标点压缩',
                                                 u'自动调整中文和西文的间距',
                                                 u'文本对齐方式',])
        return all([save_general_result, save_sent_result, save_para_result, save_sent_text_result, save_para_text_result])

    def get_sent_para_results_with_text_by_key(self, key, raw_data, key_prefix='k'):
        prop_list = [pair[1] for pair in raw_data[key]]
        hashed_prop_list = [tuple(p) for p in prop_list]
        occurrence = self.count_occurrence(hashed_prop_list)
        ordered_value = self.order_dic_by_value(occurrence)

        idx, ordered_value_repr = 1, []
        for v in ordered_value:
            props, cnt = v
            ordered_value_repr.append((props, key_prefix + str(idx)))
            idx += 1

        style_id, level = key
        return_val = []

        for pair in raw_data[key]:
            pair_text, pair_props = pair
            hashed_pair_props = tuple(pair_props) # ";".join([str(i) for i in pair_props])

            id_repr = ''
            for k, v in ordered_value_repr:
                if k == hashed_pair_props:
                    id_repr = v
                    break

            return_val.append(map(str, flatten([self.doc_name,
                                        style_id,
                                        level,
                                        id_repr,
                                        pair_text,
                                        hashed_pair_props])))
        return return_val

    def get_sent_para_results_by_key(self, key, raw_data, key_prefix='k'):
        # _, prop_list = raw_data[key]
        prop_list = [pair[1] for pair in raw_data[key]]
        hashed_prop_list = [tuple(p) for p in prop_list]
        occurrence = self.count_occurrence(hashed_prop_list)
        ordered_value = self.order_dic_by_value(occurrence)

        style_id, level = key
        idx = 1
        return_val = []
        for v in ordered_value:
            props, cnt = v
            return_val.append(map(str, flatten([self.doc_name,
                                        style_id,
                                        level,
                                        (key_prefix + str(idx)),
                                        props,
                                        cnt])))
            idx += 1
        return return_val

    def get_general_results_by_key(self, key, raw_data=None, key_prefix='k'):
        para_prop_list = [pair[1] for pair in self.raw_para_data[key]]
        sent_prop_list = [pair[1] for pair in self.raw_sentence_data[key]]
        hashed_para_prop_list = [tuple(para) for para in para_prop_list]
        hashed_sent_prop_list = [tuple(sent) for sent in sent_prop_list]
        para_prop_set = set(hashed_para_prop_list)
        sent_prop_set = set(hashed_sent_prop_list)

        style_id, level = key
        sent_prop_homogeneity = 1 if len(sent_prop_set) == 1 else 0
        para_prop_homogeneity = 1 if len(para_prop_set) == 1 else 0
        sent_count = len(sent_prop_list)
        para_count = len(para_prop_list)

        sent_stat = self.lst_to_stat(hashed_sent_prop_list, 5, 'S')
        para_stat = self.lst_to_stat(hashed_para_prop_list, 5, 'P')

        return [map(str, flatten([self.doc_name,
                         style_id,
                         level,
                         sent_prop_homogeneity,
                         para_prop_homogeneity,
                         sent_count,
                         para_count,
                         sent_stat,
                         para_stat,]))]

    def lst_to_stat(self, lst, n, key_prefix='k'):
        occurrence = self.count_occurrence(lst)
        ordered_value = self.order_dic_by_value(occurrence)
        fmted = self.fmt_first_n_stat(ordered_value, n, key_prefix)
        return fmted

    @staticmethod
    def save_result_abs(filename, raw_data, get_by_key, key_prefix='k', head_line=[]):
        import sys
        import csv
        reload(sys)
        sys.setdefaultencoding("utf-8")

        f = open(filename, 'wb')
        writer = csv.writer(f)
        writer.writerow(head_line)
        for key in raw_data.keys():
            r = get_by_key(key, raw_data, key_prefix)
            for entry in r:
                writer.writerow(entry)
        f.close()
        return True

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
            percentage = '%.2f%%' % ((v / float(total)) * 100)
            new_lst_of_kv_pair.append((key_literal, percentage))
            key_index += 1

        to_fmt = new_lst_of_kv_pair[:n] if len(new_lst_of_kv_pair) > n else new_lst_of_kv_pair
        for _ in range(n - len(to_fmt)):
            to_fmt.append(('', ''))
        out_str = [str(pair[1]) for pair in to_fmt]
        return out_str


def flatten(items, flatten_types=(list, set, tuple)):
    if not isinstance(items, flatten_types):
        return [items]
    result = []
    for item in items:
        result.extend(flatten(item))
    return result


class ResultBuilderTestCase(unittest.TestCase):
    def setUp(self):
        doc_name = "1.doc"
        raw_sentence_data = {(1, 2):[('a', ['bi', 1, False]), ('b', ['b', 3, True]), ('a', ['b', 3, True]), ('c', ['i', 3, True]), ('ee', ['i', 5, True]), ('dfe', ['i', 6, True]), ('a', ['i', 7, True])],
                             (3, 5):[('g', ['i', 5, True])],}
        raw_para_data = {(1, 2):[('a', ['bi', 1, False]), ('text', ['bi', 1, False]), ('a', ['bi', 1, False]), ('a', ['bi', 1, False])],
                             (3, 5):[('h', ['i', 5, True])],}
        self.rb = ResultBuilder(doc_name, raw_sentence_data, raw_para_data, 'D:/TMP/')

    def test_get_sent_para_results_by_key(self):
        para_r = self.rb.get_sent_para_results_by_key((1, 2), self.rb.raw_para_data)
        self.assertEqual(para_r,  [['1.doc', '1', '2', 'k1', 'bi', '1', 'False', '4']])
        sent_r = self.rb.get_sent_para_results_by_key((1, 2), self.rb.raw_sentence_data)
        self.assertEqual(sent_r, [['1.doc', '1', '2', 'k1', 'b', '3', 'True', '2'],
                                  ['1.doc', '1', '2', 'k2', 'i', '7', 'True', '1'],
                                  ['1.doc', '1', '2', 'k3', 'i', '3', 'True', '1'],
                                  ['1.doc', '1', '2', 'k4', 'bi', '1', 'False', '1'],
                                  ['1.doc', '1', '2', 'k5', 'i', '6', 'True', '1'],
                                  ['1.doc', '1', '2', 'k6', 'i', '5', 'True', '1']])

    def test_get_general_results_by_key(self):
        s = self.rb.get_general_results_by_key((1, 2))
        self.assertEqual(s, [['1.doc', '1', '2', '0', '1', '7', '4', '28.57%', '14.29%', '14.29%', '14.29%', '14.29%', '100.00%', '', '', '', '']])

    def test_order_dic_by_value(self):
        a = {'c':1, 'a':2, 'b':3}
        b = ResultBuilder.order_dic_by_value(a)
        self.assertEqual(b, [('b', 3), ('a', 2), ('c', 1)])

    def test_fmt_first_n_stat(self):
        a = [('b', 3), ('a', 2), ('c', 1), (1, 0), (True, 19)]
        b = ResultBuilder.fmt_first_n_stat(a, 3, 'p')
        self.assertEqual(b,  ['12.00%', '8.00%', '4.00%'])

    def test_count_occurrence(self):
        a = ['a', 'b', 'a', 'c', 'c', 'a']
        b = ResultBuilder.count_occurrence(a)
        self.assertEqual(b, {'a': 3, 'c': 2, 'b': 1})

    def test_lst_to_stat(self):
        func = ResultBuilder(None, None, None, None).lst_to_stat
        a = ['a', 'b', 'a', 'c', 'c', 'a']
        b = func(a, 2, 'p')
        # self.assertEqual(b, 'p1:0.5000;p2:0.3333')
        self.assertEqual(b, ['50.00%', '33.33%'])

    def test_save_all_result(self):
        r = self.rb.save_all_result()

    def test_flatten(self):
        a = ['123', ('233', 'ab'), True]
        self.assertEqual(flatten(a), ['123', '233', 'ab', True])


if __name__ == '__main__':
    unittest.main()
