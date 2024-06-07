import random

l1 = []

while len(l1) < random.randint(3, 10):
    l1.append(random.randint(3, 7))

print(l1)
xyz = [l1[0],l1[2],l1[-2]]


print(xyz)
