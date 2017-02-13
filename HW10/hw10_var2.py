import re

def searching():
    with open ('Волгоград.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    reg_gen = '<table style="background:inherit;width:100%"(?:.|\n)*</table>'
    if re.search(reg_gen, text):
        card = re.search(reg_gen, text).group()
        reg_hours = 'Часовой пояс(?:.|\n)*?<a (?:.|\n)*?>(.*)</a>'
        if re.search(reg_hours, card):
            hours = re.search(reg_hours, card).group(1)
            with open ('time_city.txt', 'a', encoding = 'utf-8') as f:
                f.write(hours)
        else:
            print('Информации о часовом поясе города не найдено')
            with open ('time_city.txt', 'a', encoding = 'utf-8') as f:
                f.write('Информации о часовом поясе города не найдено')
    else:
        print('Таблицы не найдено')
        with open ('time_city.txt', 'a', encoding = 'utf-8') as f:
                f.write('Таблицы не найдено')
    
searching()
