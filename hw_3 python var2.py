w="bonjour"
s=[]
while w:
    w=str(input ("Введите слово..."))
    if w=="":
        continue
    if len(w)>5:
        s.append (w)
for i in range(len(s)):
    print (s[i])
print ("Спасибо, до свиданья!")
    
