lis1 = [3, 4, 5, 5, 6, 0, 8, 0, 11, 142, 0, 0, 12]

l2 = 0

for l2 in lis1:
    if l2 == 0:
     lis1.remove(0)
     lis1.append(0)

print(lis1)
