def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("1. Addition      2. Subtraction     3. Multiplication        4. Division")
ch = input("Enter choice : ")
x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
if ch=='1':
    print("Addition : ",add(x,y))
elif ch=='2':
    print("Subtraction : ",sub(x,y))
elif ch=='3':
    print("Multiplication : ",mul(x,y))
elif ch=='4':
    print("Division : ",div(x,y))
else:
    print("Invalid choice")
