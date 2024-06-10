#CALCULATOR


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b
while True:
    x=int(input("num1: "))
    y=int(input("num2: "))
    z=input("Enter the operator: (+,-,*,/)")
    if(z=="+"):
        print(x,z,y,"=",add(x,y))
    elif(z=="-"):
        print(x,z,y,"=",sub(x,y))
    elif(z=="*"):
        print(x,z,y,"=",mul(x,y))
    elif(z=="/"):
        print(x,z,y,"=",div(x,y))
    else:
        print("Invalid operator")

    m=input("Do you want to continue: (Y,N) ")
    if(m!="y"):
        break

