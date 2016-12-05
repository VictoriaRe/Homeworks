##w=input("Введите слово: ")
##n=str()
##for i, letter in enumerate(w):
##    n+=letter
##    print (n)
##print("Хорошего дня!")

w=input("WORD...")
w=list(w)
for i in range(len(w)):
    n=w[i:]
    print("".join(n))
