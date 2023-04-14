from pprint import pprint
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def format_list(string):
    full_line = ''
    for index_string in range(0, 8):
        try:
          line = string[index_string]
          if line == '':
              continue
          if index_string == 0:
              if len(line.split(' ')) == 1:
                if len(string[1].split(" ")) == 1: 
                  line = line + ";" + string[1] + ";" +  string[2]
                  string.pop(2)
                  string.pop(1)
                elif len(string[1].split(" ")) == 2:
                  line = line + ";" + string[1].replace(' ', ";")
                  string.pop(1)
              line = (line.replace(" ", ";")) + ";"
              full_line = full_line + line
          elif len(line) == 3 or len(line) == 6:
            line = line + ';'
            full_line = full_line + line
          elif len(line) >= 35:
            if len(full_line.split(';')[-2]) == 3 or len(full_line.split(';')[-2]) == 6:
              line = line + ';'
            else:
               line = ';' + line
            full_line = full_line + line
          elif line[0] == '+' or line[0] == '7' or line[0] == '8':
            if line[0] == "8":
               line = line.replace("8", "+7", 1)
            elif line[0] == '7':
               line = line.replace("7", "+7", 1)
            line = line.replace(" ", '')
            if line.count('доб') == 1:
              line = line.replace("(", "")
              line = line.replace(")", "")
              line = line.replace("доб", " доб")
            if line.count('(') == 0:
               line = line.replace('495', '(495)', 1)
            if line.count('-') == 0:
               last = line[12:14:]
               last_two = line[10:12:]
               line = line[:10:]
               line = line + "-" + last_two + "-" + last
            if len(full_line.split(';')[-2]) == 3 or len(full_line.split(';')[-2]) == 6:
              line = ';' + line + '.' + ';'
            else:
              line = line  + ';'
            line = line.replace('..', '.')
            full_line = full_line + line
          elif line.count("@") == 1:
            full_line = full_line + line
        except IndexError:
           continue
    return full_line
if __name__ == '__main__':
  for index in range(2, len(contacts_list)):
      string = contacts_list[index][0].split(";")
      full_line = format_list(string)
      contacts_list[index].pop(0)
      contacts_list[index].insert(0, full_line)

  for index in range(2, len(contacts_list)):
        for second_index in range(2, len(contacts_list)):
            try:
              list_one = contacts_list[index][0].split(";")
              list_two = contacts_list[second_index][0].split(";")
              format_line = []
              if index == second_index:
                continue
              elif list_one[0] == list_two[0]:
                    resulting_list = list_one
                    resulting_list.extend(x for x in list_two if x not in resulting_list)
                    full_line = format_list(resulting_list)
                    contacts_list.pop(second_index)
                    contacts_list.pop(index)
                    split_line = full_line.split(";")
                    if len(split_line[-1]) > 35:
                      last_index = split_line.pop(-1)
                      split_line[4] = last_index
                      full_line = format_list(split_line)
                    contacts_list.extend([[full_line]])
            except IndexError:
                continue
              
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
    pprint(contacts_list)