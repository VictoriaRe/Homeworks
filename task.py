#5 баллов - открыть файл, посчитать в нем количество слов.
#Распечатать это количество.

##with open ("pretest.txt", "r", encoding="utf-8") as f:
##    f=f.read()
##    words=f.split()
##    quantity=len(words)
##    print("Количество слов в тексте: ", quantity)

##8 баллов - создать частотный словарь для всех слофоворм,
##встретившихся в тексте.
##Распечатать его в отдельный csv-файл,
##отсортировав по алфавиту
##(на каждой строчке слово + запятая + количество вхождений).

import csv
import re
def first():
    voc={}
    with open ("pretest.txt","r",encoding="utf-8") as f:
        text=f.read()
        text=text.lower()
        forms=text.split()
        for i in range(len(forms)):
            key=forms[i].strip('.,!?*:() — «»\""')
            if key not in voc:
                voc[key]=1
            else:
                voc[key]+=1
        return voc

#поменять местами ключи со значениями    
def invert_dict_nonunique(d):
    newdict = {}
    for k, v in d.items():
        newdict.setdefault(v, []).append(k)
    return newdict
    
    
def writecsv(vocabulary):   
    ### пишем csv
    with open('resul.csv', 'w', encoding='utf-8') as n:
        text = csv.writer (n, delimiter=',')
        header = ['слово', 'количество вхождений'] # это будет заголовок
        text.writerow(header)
        l=list(vocabulary.keys()) #создаем список ключей
        l.sort() #сортируем список
        for key in l:
            text.writerow([key, vocabulary[key]])

##voc=first()
##voc_invert=invert_dict_nonunique(voc) #частотный словарь отсортиров по частоте
##writecsv(voc_invert)

##10 баллов - найти все вхождения конструкции род. падеж прилагательного c безударн. окончанием -аго +
##род. падеж сущ. 1 или 2 скл. (например, великорусскаго языка) в файле.
##Выписать в отдельный файл найденные конструкции и их контексты - 3
##слова слева и 3 слова справа (каждая конструкция и её контекст на отдельной строчке).

def searching():
    with open ("pretest.txt","r",encoding="utf-8") as f:
        text=f.read()
        text=text.lower()
        reg_constr ='(?:(?:[А-Яа-яіѢѣ])+[\s,.!\?:;"\(\)\'»\n\t—]+?){3}[А-Яа-яiѢѣ]+?аго [А-Яа-яiѢѣ]+?(?:а|и)[\s,.!\?:;"\(\)\'»\n\t—]{,5}(?:[А-Яа-яiѢѣ]+?[\s,.!\?;:—"\(\)\'»\n\t]+?){3}'
        constr=re.findall(reg_constr,text)
        print("\n".join(constr))
searching()

#репозиторий https://github.com/flying-bear/HSE_programming
# словари https://www.ibm.com/developerworks/ru/library/l-python_part_4/
