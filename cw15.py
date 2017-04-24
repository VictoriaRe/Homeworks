##получает на вход путь к какой-либо папке,
##находит в этой папке и ее подпапках все файлы с расширением .txt,
##собирает словарь, в котором для всех словоформ из всех текстов записано количество вхождений,
##распечатывает 10 самых частых словоформ.

import os
import re
def searching():
    bigrams=[]
    for root, dirs, files in os.walk("."):
        for file in files:
            if ".txt" in file:
                print(file)
                with open (file, "r", "utf-8") as f:
                    f=f.read()
                    
                    
