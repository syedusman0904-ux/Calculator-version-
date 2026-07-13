def Add(a,b):
    return a + b
def Subtract(a,b):
    return a - b
def Multiply(a,b):
    return a * b
def Divide(a,b):
    if b=="0":
        return "Error!"
    return a / b
print("="*9,"simple calculator","="*8)
h=[]
c=1
while True:
    print(c)
    print("select option")
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.history\n6.clean history\n7.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        o='+'
        result='result', Add(num1,num2)
    elif choice=="2":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        o='-'
        result='result=', Subtract(num1,num2)
    elif choice=="3":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        o='*'
        result='result', Multiply(num1,num2)
    elif choice=="4":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        o='/'
        result='result', Divide(num1,num2)
    elif choice=="5":
        result=("history", h)
    elif choice=="6":
        h=[]
        result=("history clearn", h)
    elif choice=="7":
        result="Exit"
        break
    else:
        result="Invalid input"
    print(result)
    h.append(c)
    h.append('[')
    h.append(num1)
    h.append(o)
    h.append(num2)
    h.append('=')
    h.append(result)
    h.append(']')
    c+=1
        
