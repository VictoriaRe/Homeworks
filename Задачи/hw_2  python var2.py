
s=0
while s==0:
    w=str(input("Введите слово..."))
    for index, letter in enumerate(w):
        n=index+1
        if letter=="о" or letter=="п" or letter=="е":
            if n%2!=0:
                print (letter)
                s=1
  

                
