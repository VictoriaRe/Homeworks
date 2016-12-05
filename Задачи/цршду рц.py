##word=input("Enter the word...")
##for index, letter in enumerate(word):
##    #print(index,letter)
##    if (index+1)%2==0:
##        if letter!="а" and letter!="к":
##            print (index+1, letter)


##word=input("Enter the word...")
##word=list(word)
###print(word)
##for i in range(len(word)-1, -1, -1):
##    letter=word[i]
##    #print(i, letter)
##    if letter!="з" and letter!="я":
##        print(letter)
##i=0
##key="программирование"
##N=int(input("Сколько раз хотите вводить слова?.."))
##for i in range (N):
##    word=input("Слово N"+str(i+1)+" ")
##    i+=1
##    print(word)
####    if word==key:
####        break
####print("bye")
##
word=input("Enter the word..")
l=len(word)
half1=l//2
half2=""
for i in range(len(word)-1,half1-1,-1):
    #letter=word[i]
    half2+=word[i]
print(word[:half1]+half2)


##n=int(input("n= "))
##sum=""
##for i in range(n, -1,-1):
##    sum+=str(i)
##print(sum)
