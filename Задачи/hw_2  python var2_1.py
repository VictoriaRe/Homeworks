res=0

def selectLetter():
    w=str(input("Введите слово..."))
    res=0
    for index, letter in enumerate(w):
        n=index+1
        if n%2!=0:
            if letter=="о" or letter=="п" or letter=="е":
                print (letter +"\n") #выводим пор.номера и элементы
                res=1
    return res

while selectLetter()==0:
     selectLetter()

