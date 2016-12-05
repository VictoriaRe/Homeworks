##sum=0
##n=int(input("Сколько чисел использовать? Ваш ответ: "))
##for i in range (n):
##    N=int(input("N"+str(i+1)+"= "))
##    N=N**3
####    sum+=N
####print(sum)
##mult=1
##n=int(input("Факториал какого числа вы хотите узнать "))
##for i in range (1,n+1):
####    N=int(input("N"+str(i+1)+"= "))
##    mult*=i
##print(mult)

##sum=0
##mult=1
##n=int(input("Сумму факториалов скольких чисел вы хотите узнать "))
##for i in range (1,n+1):
##    mult*=i
####    sum+=mult
####print(sum)
##olya=0
##n=int(input("Сколько чисел использовать? Ваш ответ: "))
##for i in range (n):
##    N=int(input("N"+str(i+1)+"= "))
####    if N==0:
####        olya+=1
####print(olya)
##sum=""
##n=int(input())
##if n<=9:
##    for i in range (1,n+1):
##        sum+=str(i)
##        print(sum)
##else:
##    print("DO SVIDANIYA")
N=int(input("TOTAL..."))
sum=0
sumcontrol=0
for s in range(N+1):
    sumcontrol+=s
for i in range (N-1):
    uhave=int(input("Номер карточки, который у вас на руках..."))
    sum+=uhave
numbacart=sumcontrol-sum
print("Номер потерянной карточки ", numbacart)
    
    
    
