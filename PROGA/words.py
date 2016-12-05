import random

with open ("words.txt","r",encoding="utf-8") as f:
    lines=f.readlines ()
    random.shuffle(lines)
    score=0
    for line in lines:
        line=line.strip()
        word,hint =line.split (" ", 1)
##
##            text=f.readlines ()
##            print (text)
##
##        for word in words:
##            word = random.choice (words)

        response=input ("Какое слово загадано?\n"+"Hint: "+hint+" ")
        if response == word:
            print ("GOOD")
            score+=1
        else:
            print ("Not that good, try again, the word was ", word)
with open("sxores.txt", "w", encoding="utf-8")as n:
    percent=score/6*100
    n.write("Here are ur results: ")
    n.write (str(percent)+"%")
    

