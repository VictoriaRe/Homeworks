##wordlist=[]
##w="lol"
###print(w)
##while w!="":
##    w=input("Введите слово...")
##    wordlist.append(w)
##    
###print("\n".join(wordlist))
##for i in range(len(wordlist)):
##    w=wordlist[i]
##    #print(w)
##    if w=="":
##        break
##    word2=""
##    for k in range(len(w)-1,-1,-1):
##        #letter=w[k]
##        if k==2:
##            continue 
##        word2+=w[k]
##    print(word2)
    
wordlist=[]
w="lol"
#print(w)
while w!="":
    w=input("Введите слово...")
    wordlist.append(w)
    
#print("\n".join(wordlist))
for i in range(len(wordlist)):
    w=wordlist[i]
    #print(w)
    if w=="":
        break
    #word2=""
    #for k in range(len(w)):
        #word2+=w[k]
    print(w[i+1:])
