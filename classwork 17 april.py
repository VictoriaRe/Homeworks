##Написать свою имплементацию функции shutil.rmtree() - то есть функцию,
##которая удаляет выбранную папку со всеми папками и файлами внутри неё.
##import os
##def delete_folder(path):
##    for root, dirs, files in os.walk(path, topdown=False):
##        for f in files:
##            os.remove(os.path.join(path, f))
##        for d in dirs:
##            os.rmdir(os.path.join(root,d))
##        os.rmdir(path)
##        print("check it")
##delete_folder(r"C:\Users\student\Desktop\2539")


##Написать программу, которая рисует дерево текущей папки в таком виде:
##--folder1
## --folder4
##       file4
##       file5
## --folder5
##--folder2
## file2
## file3
##--folder3

##import os
##def main():
##    d={}
##    for root, dirs, files in os.walk("."):
##        num = 0
##        for r in root:
##            if r == '\\':
##                num += 1 # какая глубина?
##        root = root.split('\\')[-1]
##        print('\t'*(num - 1), root)
##        for f in files:
##            print('\t'*num, f)
##main()

##Скачать архив и распаковать его. Это уже знакомый нам корпус BAWE. В папке CORPUS_TXT и CORPUS_UTF-8 лежат одни и те же тексты,
##только в CORPUS_UTF-8 они с разметкой, а в CORPUS_TXT без разметки. Представленные тексты принадлежат к разным дисциплинам:
##History, Sociology, Literature, etc. Вам нужно собрать корпуса эссе для каждой дисциплины и посчитать частотный список для каждого корпуса.
##Для этого вам нужно извлечь категорию эссе из xml-файлов в папке CORPUS_UTF-8, а затем взять файл с таким же
##именем в папке CORPUS_TXT и добавить его содержимое в соответствующий корпус.
#открыть каждый файл из папки ютээф
#прочитать его
#найти в нем тег <p n="discipline">Sociology</p> точнее слово которое между ними и
#для каждого такого файла если это имя не совпадает с тем что было до
#создать папку с таким именем
#открыть 

import os
def main(path):
    for root, dirs, files in os.walk(path):
        



main("C:\Users\student\Desktop\2539\CORPUS_UTF-8")

