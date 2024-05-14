number =int(input("Enter five-digit number"))#number=12345
q =(number%10)*10000 #number=50000
e =(number//10%10)*1000 #number=4000
r =(number//100%10)*100 #number=300
t =(number//1000%10)*10 #number=20
y =(number//10000) #number=1
print(q+e+r+t+y)