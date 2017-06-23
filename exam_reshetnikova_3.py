

##1 (5 баллов). Посчитайте, сколько в каждом файле слов,
##запишите эту информацию в новый текстовый файл
##в формате "название файла<табуляция>количество слов",
##для каждого файла информация на новой строчке.

##2 (8 баллов). Создайте csv-таблицу с полями
##"Название файла", "Автор", "Дата создания текста",
##содержащую информацию о всех статьях.
##
##import csv
##
##data = ['5', '18', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0']
##
##with open('list_to_csv.csv', 'w', newline='') as csv_file:
##    csv_writer = csv.writer(csv_file)
##    for item in data:
##        csv_writer.writerow([item])

import os
import re
import csv

def first_task(text):
    tag_word="<w>"
    word=re.findall(tag_word, text)
    counting=len(word)
    return counting

def second_task(file, text):
    auth=[]
   # <meta content="неизвестный" name="author"></meta>
    tag_author="<meta content=\"?[\w\s]+\"?\s?name=\"author"
    tag_data="<meta content=\"[\d\.]+\" name=\"created"
    authors=re.findall(tag_author, text)
    datas=re.findall(tag_data, text)
    for a in authors:
        a=a[15:-14]
    for d in datas:
        d=d[15:-15]
    with open("tabl.txt", "a", encoding="utf-8") as v:
        v.write(file+"\t"+a+"\t"+d+"\t"+"\n")
    return v
    
        
    


for root, dirs, files in os.walk('news'):
    for file in files:
        if ".xhtml" in file:
            with open (os.path.join(root, file), "r", encoding="cp1251") as f:
                text=f.read()
                with open ("words_counting", "a", encoding="utf-8") as t:
                    t.write(file+"\t"+str(first_task(text))+"\n")
                    second_task(file,text)
             

              
        #   for i in range(len(datas)):
        #csv_writer.writerow(datas[i][15:-15])
       # for i in range(len(authors)):
        #    csv_writer.writerow(datas[i][15:-15])

    
