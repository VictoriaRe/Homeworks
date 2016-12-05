n=input("Ваше имя...")
a=input("Ваш возраст...")
c=input("Ваш любимый цвет...")
m=input("Ваш любимый музыкальный испольнитель...")
d=input("Ваша мечта...")
with open("information.txt", "w", encoding="utf-8") as f:
    f.write ("Вот информация, которую мы узнали:\n")
    f.write (n + "\n" + a + "\n" + c + "\n" + m + "\n" + d + "\n")
    
    
