from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for index_string in range(1, len(contacts_list)):
  for index in range(len(contacts_list[0])):
    string = contacts_list[index_string][index]
    if len(re.split(r'[\s]', string)) == 3 and index == 0:
      lastname = re.split(r'[\s]', string)[0]
      firstname = re.split(r'[\s]', string)[1]
      surname = re.split(r'[\s]', string)[2]
      continue
    elif len(re.split(r'[\s]', string)) == 2 and index == 0:
      lastname = re.split(r'[\s]', string)[0]
      firstname = re.split(r'[\s]', string)[1]
      for index_second in range(2, len(contacts_list[0])):
        string_second = contacts_list[index_string][index_second]
        if re.search(r'[\w]+[и]+[ч]',string_second) != None:
          surname = re.search(r'[\w]+[и]+[ч]',string_second)[0]
    elif len(re.split(r'[\s]', string)) == 1 and index == 0:
      lastname = re.split(r'[\s]', string)[0]
      for index_second in range(1, len(contacts_list[0])):
        string_second = contacts_list[index_string][index_second]
        if re.search(r'[\w]+[и]+[ч]',string_second) != None and len(re.split(r'\s',string_second)) == 2:
          firstname = re.split(r'\s',string_second)[0]
          surname = re.split(r'\s',string_second)[1]
          continue
        elif index_second == 1:
          firstname = string_second
        elif index_second == 2:
          surname = string_second
      continue
    if re.search(r'ФНС', string) != None:
      organization = string
      continue
    elif re.search(r'Минфин', string) != None:
      organization = string
      continue
    elif string == '' and index == 3:
      organization = ""
      continue
    if string == '' and index == 4:
      position = contacts_list[index_string][index]
      continue
    elif len(re.split(r'[\s]', string)) > 5:
      position = string
      continue
    if re.search(r'[+]|[+]\d|\d', string) != None and re.search(r'[@]', string) == None:
      phone = string
      phone = phone.replace(' ', '').replace('-', '').replace('(','').replace(')', '')
      if len(phone) == 11:
        phone= '+'+ '7'+'('+ phone[1:4:]+')'+ phone[4:7:]+'-' + phone[7:9:]+'-'+phone[9:11:]+'.'
        continue
      if phone.count('доб') == 1:
        phone= '+' + '7'+'('+ phone[1:4:]+')'+ phone[4:7:]+'-' + phone[7:9:]+'-'+phone[9:11:]+' ' + phone[12:15:] + phone[15:20:]+'.'
      else:
        phone= '+'+ '7'+'('+ phone[2:5:]+')'+ phone[5:8:]+'-' + phone[8:10:]+'-'+phone[10:12:]+'.'
        continue
    elif string == '' and index == 5:
      phone = ''
      continue
    if string == '' and index == 6:
      email = ''
      continue
    elif re.search(r'@', string) != None:
      email = string
      continue
  format_string = [lastname, firstname, surname, organization, position, phone, email]
  contacts_list[index_string] = format_string

for index in range(1, len(contacts_list)):
  for index_second in range(1, len(contacts_list)):
    string_one = contacts_list[index]
    string_two = contacts_list[index_second]
    if index == index_second:
      continue
    elif string_one[0] == string_two[0]:
      second_contact_list = []
      for index_string in range(len(contacts_list[0])):
        if string_one[index_string] == '':
          string_one[index_string] = string_two[index_string]
      contacts_list[index] = string_one

for index in contacts_list:
  if contacts_list.count(index) > 1:
    contacts_list.remove(index)
         

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
## Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list)