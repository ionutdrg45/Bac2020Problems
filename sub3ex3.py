f = open("numere.in", "r")

n = f.readline()
array = f.readline()
array = array.split()

checker = [0] * int(n)

for i in array:
    checker[int(i)] += 1

number = 0

for c in checker:
    if c == 0:
        number += 1

print(number)