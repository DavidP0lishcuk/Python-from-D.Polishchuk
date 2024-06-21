user_case = "999"

result = 10

while result >= 9:
    len_letter = len(user_case)
    user_case = int(user_case)
    result = 1
    list1 = []
    while len_letter > 0:
        list1.append(user_case // (10 ** (len_letter-1)))
        user_case = user_case % (10 ** (len_letter-1))
        len_letter -= 1
    for l_number in list1:
        result *= l_number
    user_case = str(result)


print(result)
