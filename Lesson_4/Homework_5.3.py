
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
space = " "

user_case = input("Some word:")

for s1 in punctuation:
    if s1 in user_case:
        user_case = user_case.replace(s1, '')

user_case = user_case.title()

for s2 in space:
    if s2 in user_case:
        user_case = user_case.replace(s2, '')

if len(user_case) > 139:
    user_case = user_case[:139]

print("#" + user_case)

#Python Commnity
#i like python community!
#Should, I. subscribe? Yes!
#t!e@S#T e$XA%m
