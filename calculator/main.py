try:
    a= int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("what kind of operation you want to perform:-\n1. Addition press + \n2. Subtraction press - \n3. Multiplication press * \n4. Division press /")
    o= input("Enter your choice: ")
    match o:
        case '+':
            print(f"The sum of {a} and {b} is {a+b}")
        case '-':
            print(f"The difference of {a} and {b} is {a-b}")
        case '*':
            print(f"The product of {a} and {b} is {a*b}")
        case '/':
            if b != 0:
                print(f"The division of {a} by {b} is {a/b}")
            else:
                print("Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")
except Exception as e:
    print("Enter valid value of a and b")