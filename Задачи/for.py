##A=int(input())
##B=int(input())
##if A<B:
##    for i in range (A,B+1):
##        print(i)
##else:
##    for n in range (A,B-1,-1):
##        print(n)

##A=int(input("A= "))
##B=int(input("B= "))
##
##for i in range (A,B-1,-1):
####    #if i%2==0:
####    print(i%2==0)
####print("Au revoir")
##
##sum=0
##for i in range (10): 
##    n1=int(input("N"+str(i+1)+"= "))
##    sum=sum+n1
####print(sum)
sum=0
n=int(input("Сколько чисел суммроват? "))
for i in range (n):
    N=int(input("N"+str(i+1)+"= "))
    sum+=N
print(sum)
