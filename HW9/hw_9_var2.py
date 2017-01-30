#открыть файл прочитать по строкам рассплитить по словам
# создать массив рез-тов
#сравнить слово с рег выраж
#если нет в резах, записать
#распечать резы

import re

def saferes(results, w):
    if w not in results:
        results.append(w)
    return results

def replace_punct(wow):
    symbol=".?!, /()-:" +"\""
    symbol=list(symbol)
    for s in symbol:
        wow=wow.replace(s, '')
    return wow
            
i=0
resul=[]
with open ("dovlatov.txt","r",encoding="utf-8") as f:
    for line in f:
        regex1=r"\bнай(ти(сь)?|д(и(те(сь)?|сь)?|у(т(ся)?|(сь)?)|я(сь)?|е(шь(ся)?|т(е(сь)?|(ся)?)|м(ся)?)))\b"
        regex2=r"\bнаш(е(л(ся)?|дш(ая(ся)?|ую(ся)?|е(го(ся)?|е(ся)?|й(ся)?)))|л(а(сь)?|о(сь)?|и(сь)?))\b"
        line=line.lower()
        line=line.split()
        for word in line:
            word=replace_punct(word)
            word=word.replace("ё", "е")
            res=re.search("("+regex1+")|("+ regex2+")", word)
            if res!=None:
                resul=saferes(resul, word)
resul.sort()
print('\n'.join(resul))
            
