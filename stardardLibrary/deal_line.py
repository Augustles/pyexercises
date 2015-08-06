# coding=utf-8

def change_line(path):
    import os,re
    os.chdir(path)
    d = []
    for file in os.listdir(path):
        if file.endswith('.js'):
            d.append(file)
    for x in d:
        n = x + '.bak'
        # 写入到新的文件中,对line进行修改
        with open(x,'r') as r, open(n,'w') as w:
            for line in r:
                if re.findall(r'^[0-9]+\.\w+', line):
                    i = line.index('.')
                    n_line = line[0:i+1] + ' '+line[i+1:]
                    w.write(n_line)
                else:
                    w.write(line)
    # 删除匹配到'.js'文件
    for x in d:
        print(x)
        os.remove(x)
    # 重命名.bak
    for y in os.listdir(path):
        if y.endswith('.bak'):
            new_file = y[:-6]+'md'
            print new_file
            os.rename(y, new_file)

change_line(r'C:\\Users\\ieware\\stackoverflow')
