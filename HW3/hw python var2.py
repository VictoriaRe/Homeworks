a=int(input())
b=int(input())
c=int(input())
if a*b==c:
    print(str(a)+" умножить на "+ str(b) +" равно "+str(c))
else:
    print(str(a)+" умножить на "+ str(b) +" не равно "+str(c))

x=-b/a
if b<0:
    z=""
else:
    z="+"

if c==x:
    print (str(c)+" является решением линейного уравнения " + str(a)+ "x" +z+ str(b) + " = 0 ")
else:
    print(str(c)+" не является решением линейного уравнения " + str(a)+ "x" + z + str(b) + " = 0 ")
