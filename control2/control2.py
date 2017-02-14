#1 1. (5 баллов) Открыть файл с корпусом, подсчитать в нём число строк;
##открыть другой файл для записи,записать туда число строк,
##найденных в файле с корпусом.

##def first():
##    with open ("1.txt", "r", encoding="utf-8") as f:
##        lines=0
##        for line in f.readlines():
##            lines+=1
##        #print("Количество строк: ", lines)
##    with open ("resul.txt", "w", encoding="utf-8") as new:
##        new.write("Количество строк: "+ str(lines))    
##firsttask=first()

##2. (8 баллов) Создать словарь, в котором ключами являются строки с морфологическим разбором слов (то есть значения атрибута type для строк,
##в которых имеется "<w lemma="), а значениями - количество их вхождений в файле.
##Распечатать ключи из словаря в открытый для записи файл (значения распечатывать не нужно).
import re
def searching(): #ищем строки
    with open ('1.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
        reg_tag = '<w lemma="(.*)</w>'
        if re.findall(reg_tag, text):
            for i in text:
                constr = re.findall(reg_tag, text)
                  


    d={}
    #with open ('constr.txt', 'r', encoding = 'utf-8') as m:
    for l in range(len(c)):
            #key=forms[i].strip('.,!?*:() — «»\""')
        if constr[l] not in d:
            d[key]=1
        else:
            d[key]+=1
    with open ('constr.txt', 'a', encoding = 'utf-8') as s:
        s.write("\n".join(c))
    #return 
        

search=searching()

       
