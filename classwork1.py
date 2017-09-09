import re
import urllib.request  # импортируем модуль 
req = urllib.request.Request('https://yandex.ru/pogoda/moscow')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')
   regPostPogoda = re.compile('<div class="current-weather__thermometer current-weather__thermometer_type_now">.*?</div>', flags=re.U | re.DOTALL)
   pogoda = regPostPogoda.findall(html)
   new_pogoda = []
   regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
   regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
   for t in pogoda:
       clean_t = regSpace.sub("", t)
       clean_t = regTag.sub("", clean_t)
       new_pogoda.append(clean_t)
   for t in new_pogoda:
        print("погода сегодня: ", t)
   regPostCloud = re.compile('<div class="forecast-brief__item-comment">.*?</div>', flags=re.U | re.DOTALL)
   cloud=regPostCloud.findall(html)
   new_clouds=[]
   regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
   regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
   for p in cloud:
       clean_p = regSpace.sub("", p)
       clean_p = regTag.sub("", clean_p)
       new_clouds.append(clean_p)
   print("облачность сегодня: ", new_clouds[0])
   regPostSunrise = re.compile('<span class="current-weather__info-label">Восход:.*?</span>', flags=re.U | re.DOTALL)
   sunrise = regPostPogoda.findall(html)
   new_sunrise = []
   regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
   regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
   for t in sunrise:
       clean_t = regSpace.sub("", t)
       clean_t = regTag.sub("", clean_t)
       new_sunrise.append(clean_t)
       print(new_sunrise)
##   for t in new_sunrise:
##        print(": ", t)
##   <span class="current-weather__info-label">Восход: </span>
