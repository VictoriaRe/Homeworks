##d={"France": "Paris",
##   "USA": "Washington DC",
##   "Georgia": "Tbilisi",
##   "Russia": "Moscow",
##   "Austria": "Vienna"}
##for key in d:
##    print (key, "-", d[key])

##d={"France": "Paris",
##   "USA": "Washington DC",
##   "Georgia": "Tbilisi",
##   "Russia": "Moscow",
##   "Austria": "Vienna"}
##def capital():
##    country=input("Enter the country name...")
##    if country in d:
##        return d[country]
##    else:
##        return "bye"
##print(capital())

i=0
r=0
d={"France": "Paris",
   "USA": "Washington DC",
   "Georgia": "Tbilisi",
   "Russia": "Moscow",
   "Austria": "Vienna"}
def revert(d):
    n={}
    for i in d.keys():
        city=d[i]
        n[city]=i
    return n
print(revert(d))
