#прочитать его, поделить на предложения
#(просто по знакам конца предложения),
#удалить знаки препинания
#Найти предложения длиннее 10 слов,
#и для этих предложений распечатать слова,
#начинающиеся с заглавной буквы
import re
def sentence(): 
    with open ("dovlatov.txt", "r", encoding="utf-8") as f:
               text=f.read()
               text=re.sub("\n", " ", text)
               res=re.split(r'[.|!|?|…]', text)
               return res
            
def deletepunc(sentence):
    r=[]
    for s in sentence:
        for symb in ".,?!:\"...;":
            s=s.replace(symb, "")
            s=re.sub("- ", "", s)
            s=re.sub("  {1,10}", " ", s)
        r.append(s)
    return r
    
def find_print(sentclear):
    v=[re.findall("[А-Я]\w* ", sent) for sent in sentclear if len(sent.split(" "))>10]
    new_v=[print(elem, end="\n") for row in v for elem in row]

p=sentence()
s=deletepunc(p)
find_print(s)
