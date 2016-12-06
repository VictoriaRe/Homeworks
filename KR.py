with open ("KR.txt","r",encoding="utf-8") as f:
    for line in f.readlines():
        if line.find("союз")!=-1:
            print(line)

    word=""
    sumipm=0        
    for line in f.readlines():
        if line.find("сущ")!=-1 and line.find("жен")!=-1:
            word+=line.split(" ")[0]
            word+=", "
            sumipm+=float(line.split(" ")[-1])
    print("Слова существительные женского рода и единственного числа: ", word, "Сумма вхожжений всех этих слов следющая: ", sumipm)
            
