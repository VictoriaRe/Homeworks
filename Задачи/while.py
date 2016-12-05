##s=1
##i=0
##N=int(input ("N= "))
##while s*2<N:
##    s*=2
##    i+=1
##print("i= ",i, end=", ")
####print("s= ", s)
##i=1
##x=float(input("Вклад.."))
##p=float(input("процент годовых..."))
##y=float(input("сумма вклада с процентами..."))
##while x<=y:
##    x*=0.01*p+1
####    x=round(x,2)
####    #print(x)
####    i+=1
####print("years...",i)
####i=0
##sum=0
##n=1
##v=10
##i=0
##maximum=0
##while n>=0:
##    n=int(input())
##    if n==0:
##        v=33
##    if v==10:
##        if n>maximum:
##            maximum=n
##            i1=i
##        i+=1
##print(i1+1)

word=input("Enter the word...")
for index, letter in enumerate(word):
    #print(index,letter)
    if index%2!=0 and (letter!="а" or letter!="к"):
        print (index, letter)
    
