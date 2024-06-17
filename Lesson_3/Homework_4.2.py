list1 = [0, 1, 7, 2, 4, 8]

sum1 = 0

if not list1:
    print(0)

else:
    for index in range(0, len(list1), 1):
        if index % 2 == 0:
            sum1 = sum1+list1[index]

if list1:
    print(list1[-1] * sum1)

