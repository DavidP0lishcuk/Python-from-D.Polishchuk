number =int(input("Enter four-digit number"))#number=1234
number1 = number // 1000 #number1=1
number = number % 1000 #number=234
number2 = number // 100 #number2=2
number = number % 100 #number=34
number3 = number // 10 #number3=3
number = number % 10 #number=4

print(number1)
print(number2)
print(number3)
print(number)