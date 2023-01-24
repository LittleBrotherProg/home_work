import os, fnmatch
if os.path.isfile(r'unification.txt'):
    os.remove(r'unification.txt')
else:
    listOfFiles = os.listdir('.')  
    pattern = "*.txt"  
    txt_file = []
    count_line = {}
    sort_dict = {}
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                txt_file.append(entry)
                with open(entry, 'r', encoding='UTF-8') as f:
                    file = f.readlines()
                    count_line[entry] = len(file)
                    sorted_keys = sorted(count_line, key=count_line.get)
    for w in sorted_keys:
        sort_dict[w] = count_line[w]
    with open(r'unification.txt', "w", encoding='UTF-8') as g:
        for numb_lines in sort_dict.keys():
            with open(numb_lines, 'r', encoding='UTF-8') as file:
                lines = file.readlines()
                print(numb_lines)
                print(int(len(lines)))
                for line in range(int(len(lines))):
                    print("Строка номер", line + 1, "файла номер", numb_lines[0])
                    g.write(lines[int(line)])


