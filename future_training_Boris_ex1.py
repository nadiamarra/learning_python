def f3(x,y):
    a=y-1
    b=x+1
    c=a+b
    x=x+y
    y=y-x
    print("F3 x=",x, "y=",y)
    print("F3 a=", a, "b=",b,"c=",c)

    return x+y

def f2(x,y):
    a=x
    b=y
    c=f3(a,b)
    print("F2 x=",x, "y=", y)
    print("F2 a=", a, "b=",b,"c=",c)

    return c

def f1(x,y):
    a=2*x
    b=x+y
    c=f2(a,b)
    print("F1 x=",x, "y=", y)
    print("F1 a=", a, "b=",b,"c=",c)

    return c

def main():
    x=10
    y=20
    z=0
    z=f1(x,y)
    print ("Main x=",x,"y=",y,"z=",z)

main()
