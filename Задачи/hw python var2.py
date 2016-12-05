a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a*b==c:
    print(str(a)+" умножить на "+ str(b) +" равно "+str(c))
else:
    print(str(a)+" умножить на "+ str(b) +" не равно "+str(c))

if b<0:
    z=""
else:
    z="+"    

if a==0 and b!=0:
    print(str(c)+" не является решением линейного уравнения " + str(a)+ "x" + z + str(b) + " = 0 ")
else:
    if a==0:
        x=0
    else:
        x=-b/a
        
    if c==x:
        print (str(c)+" является решением линейного уравнения " + str(a)+ "x" +z+ str(b) + " = 0 ")
    else:
        print(str(c)+" не является решением линейного уравнения " + str(a)+ "x" + z + str(b) + " = 0 ")
