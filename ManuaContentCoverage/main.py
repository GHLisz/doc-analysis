import os
from doc import Doc
from entry_comparer import EntryComparer

def main():
    doc_full_name = sys.argv[1]
    doc_full_name = doc_full_name.decode('gbk')
    doc_name = os.path.basename(doc_full_name)
    result_path = r'E:\V8AutoTest\SAK\Results\ResultFiles'
    result_file = result_path + '\\' + doc_name + '.txt'

    doc = Doc()
    ec = EntryComparer(doc.manual_content_entries, doc.toc_entries)
    if ec.compare():
        result = 'True' # + '\n' + 'No memory leaks detected.'
    else:
        result = 'False' # + '\n' + 'WARNING: Visual Leak Detector detected memory leaks!'


    import codecs
    f = codecs.open(result_file, 'w', 'utf_8_sig')
    f.write(result + '\n')
    f.write('diff_entries: \n')
    for entry in ec.diff_info():
        f.write(str(entry) + '\n')
    f.write('TOC_entries: \n')
    for entry in ec.test_entries:
        f.write(str(entry) + '\n')
    f.write('MC_entries: \n')
    for entry in ec.base_entries:
        f.write(str(entry) + '\n')
    f.close()

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    main()

