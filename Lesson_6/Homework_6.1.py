import string

user_case = input("Some letters:")

l1, l2 = user_case.split('-')

l1 = string.ascii_letters.index(l1)
l2 = string.ascii_letters.index(l2)+1

print(string.ascii_letters[l1:l2])

