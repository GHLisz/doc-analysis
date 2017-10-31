#coding=utf-8
import os
import sys
from mclog import MCLog
from doc import Doc


def main():
    doc_name = sys.argv[1]
    doc_name = doc_name.decode('gbk')
    file_name = os.path.basename(doc_name)
    result_file_path = r'E:\V8AutoTest\SAK\Results\ResultFile' + "\\" + file_name + '.txt'

    range_list_of_level = MCLog("E:/V8AutoTest/log.txt").range_list_of_level
    doc = Doc()
    doc.save_result(range_list_of_level,
                    doc_name.replace(r"E:\V8AutoTest\SAK\cases" + '\\', ''),
                    result_file_path)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    main()
