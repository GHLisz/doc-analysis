#coding=utf-8
import os
import sys
from mclog import MCLog
from doc import Doc
from result_builder import ResultBuilder


def main():
    doc_full_name = sys.argv[1]
    doc_full_name = doc_full_name.decode('gbk')
    doc_name = os.path.basename(doc_full_name)
    result_path = r'E:\V8AutoTest\SAK\Results\ResultFile'

    range_list_of_level = MCLog("E:/V8AutoTest/log.txt").range_list_of_level
    doc = Doc(range_list_of_level)
    rb = ResultBuilder(doc_name, doc.raw_sentence_data, doc.raw_para_data,result_path)
    rb.save_all_result()


def verify():
    range_list_of_level = MCLog("D:\Downloads\log.txt").range_list_of_level
    print range_list_of_level
    doc = Doc(range_list_of_level)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    main()
    # verify()
