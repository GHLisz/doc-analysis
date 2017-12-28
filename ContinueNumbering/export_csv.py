#coding=utf-8
import os

def concat_path_list_to_csv2(path_list, csv_path):
    import sys
    import csv
    reload(sys)
    sys.setdefaultencoding("utf-8")

    header_saved = False
    csvfile = open(csv_path, 'wb')
    writer = csv.writer(csvfile)

    for idx, fname in enumerate(path_list):
        f = open(fname, 'rb')
        is_first_line = True
        reader = csv.reader(f)
        try:
            for line in reader:
                if is_first_line:
                    is_first_line = False
                    if not header_saved:
                        writer.writerow(line)
                        header_saved = True
                else:
                    if line[1] == '0':
                        continue
                    line[1] = str(idx+1) + line[1].rjust(4, '0')
                    writer.writerow(line)
        except:
            continue
        f.close()
    csvfile.close()


def concat_path_list_to_csv(path_list, csv_path):
    import codecs

    header_saved = False
    csvfile = codecs.open(csv_path, 'w', 'utf_8_sig')
    for fname in path_list:
        f = codecs.open(fname, 'r', 'utf_8_sig')
        try:
            header = next(f)
            if not header_saved:
                csvfile.write(header)
                header_saved = True
            for line in f:
                # filter out style id 0
                if line.split(',')[1] == '0':
                    continue
                # filter out style id 0
                csvfile.write(line)
        except:
            continue
        f.close()
    csvfile.close()


def make_all_files():
    # txt_dir = ur'D:\TMP\新建文件夹\测试'
    txt_dir = ur'D:\TMP\新建文件夹\1017950_1187092\ResultFile'

    dic = {u'总体_': [],
           u'句属性_': [],
           u'段属性_': [],
           u'含文本句属性_': [],
           u'含文本段属性_': [], }

    for dirpath, dirnames, filenames in os.walk(txt_dir):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            for k, v in dic.items():
                if file.startswith(k):
                    dic[k].append(fullpath)

    for k, v in dic.items():
        v.sort()
        file_str =  txt_dir + '\\' + u'全部样张_' + k[:-1]+'.csv'
        concat_path_list_to_csv2(v[:500], file_str)
        if u'含文本' in file_str:
            dedupe_text_csv(file_str)

    print(dic)


def dedupe_text_csv(file_path):
    import sys
    import csv
    reload(sys)
    sys.setdefaultencoding("utf-8")
    from collections import defaultdict

    content = defaultdict(list)
    new_path = file_path + u'_仅有问题的.csv'

    of = open(file_path, 'rb')
    reader = csv.reader(of)
    for line in reader:
        content[line[1]].append(line)
    of.close()
    of = open(file_path, 'rb')
    reader = csv.reader(of)
    for row in reader:
        header = row
        break
    of.close()

    for k, v in content.items():
        cate_set = set(line[3] for line in v)
        if len(cate_set) == 1:
            content.pop(k)

    nf = open(new_path, 'wb')
    writer = csv.writer(nf)
    writer.writerow(header)
    for k, v in content.items():
        for line in v:
            writer.writerow(line)

    nf.close()


# dedupe_text_csv(ur"D:\TMP\新建文件夹\1017950_1187092\ResultFile\有TOC500_含文本段属性.csv")
make_all_files()
