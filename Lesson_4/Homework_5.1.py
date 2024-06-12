import string
import keyword

user_case = input("Some word:")

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^ `{|}~"""

result = True

if user_case[0].isdigit():
    result = False

if not user_case.islower():
    result = False

for char in user_case:
    if char in punctuation:
        result = False
        break

if user_case in keyword.kwlist:
    result = False

counter_letters = 0

counter = 0

for char in user_case:
    if char == "_":
        counter += 1
    if char.isalpha():
        counter_letters += 1

if counter > 1 and counter_letters == 0:
    result = False

if user_case == "_":
    result = True


if not result:
    print(False)
else:
    print(True)









