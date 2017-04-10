##import os
##import shutil
###with open (f) #будет кодировка по усмолчанию мак ютф8 виндовс
###windows C:\\Users\\student\\Downloads #путь файла
###os.path.abspath(".")
###os.getcwd()
##os.path.join("cou", "1.txt") #rabotaet vezde
##os.path.exists("cou")
##os.listdir(".")#vozvrashaet massiv
##s="hello"
##i=1
##for f in os.listdir("."):
##    if f endswith (".txt"):
##        with open(f, "a", encoding="utf-8") as w:
##            w.write(s*i)
##            i+=1
##
###sozdat' papku
##os.mkdir("corpus")
##
###sozdat' papku v papke
##
##os.makedirs("a\\b\\c\\path")
##
##os.rename("corpus", "corpus new") #snachala staroe imya potom novoe
##
##os.path.isfile("cou\\2.txt")
##os.path.isdir("cou")
##
##shutil.copy("texts\\corpus1.txt", "new") #kopirovat' file
##shutil.copytree("texts", "new_corpus") #vse papki kopirovat'
##shutil.move
##
##os.remove("corpus\\corpus2.txt") #udalit' navsegda
##shutil.rmtree("cou")

##Пользователь вводит предложение на английском языке, и программа создает вложенные друг в друга папки,
##так чтобы путь к самой глубокой из них составлял введенное предложение. Например,
##если пользователь ввел предложение "It is a wonderful day",
##программа должна создать вложенные папки, и путь к последней из них должен быть "it/is/a/wonderful/day"

##import os
##names=input("Enter a phrase ...")
##names=names.replace(" ", "\\")
##os.makedirs(names)

import os
numba=int(input("enter the number"))
for i in range (1, numba+1):
    os.mkdir(str(i))

    for j in range(1,i+1):
        open (str(j), "w", encoding="utf-8")
#numbers=[1, numba]
#print(numbers)
#os.mkdir()


    
