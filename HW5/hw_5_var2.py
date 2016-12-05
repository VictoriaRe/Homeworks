maximum=0
minimum=10**5
with open ("dost.txt","r",encoding="utf-8") as f:
    for line in f.readlines():
        l=len(line)
        if l>maximum:
            maximum=l
        if l<minimum and l!=0:
            minimum=l
        k=maximum/minimum
print("Cамая короткая строка текста короче самой длинной в ",k, "раз.")

