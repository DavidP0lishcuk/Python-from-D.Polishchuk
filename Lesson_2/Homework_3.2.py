x = float(input("First number:"))

operation = input("Operation (+, -, *, /):")

y = float(input("Second number:"))

try:
    if operation == "+":
        print(x + y)
    elif operation == "-":
        print(x - y)
    elif operation == "*":
        print(x * y)
    elif operation == "/":
        print(x / y)

except:
    if ZeroDivisionError:
        print("You can't divide by zero!")
