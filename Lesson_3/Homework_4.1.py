lis1 = [3, 4, 5, 5, 6, 0, 8, 0, 11, 142, 0, 0, 12]

lis2 = []

while True:
  if 0 in lis1:
     lis1.remove(0)
     lis2.append(0)
  else:
      break

lis1 = lis1+lis2

print(lis1)
