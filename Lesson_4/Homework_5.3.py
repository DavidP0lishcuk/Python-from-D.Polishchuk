
punctuation = r"""!"#$%&' ()*+,-./:;<=>?@[\]^_`{|}~"""

user_case = input("Some word:")

user_case = user_case.title()

for s1 in punctuation:
    if s1 in user_case:
        user_case = user_case.replace(s1, '')

if len(user_case) > 139:
    user_case = user_case[:139]

print("#" + user_case)
