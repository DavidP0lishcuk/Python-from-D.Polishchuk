list1 = [1, 2, 3, 4, 5, 6]

sum1 = 0

for index in range(0,len(list1),1):
    if index % 2 == 0:
        sum1 = sum1+list1[index]

print(list1[-1]*sum1)
