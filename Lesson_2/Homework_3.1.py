y = [1,1,9]

if len(y)>1:
    last_element = y.pop()
    y.insert(0, last_element)
    print(y)
else:
    print()

if len(y) == 1:
    print(y)

if len(y) == 0:
    print(y)