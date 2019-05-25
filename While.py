# While.py

i = 1
while i <= 5:
    print(i)
    i = i + 1

i=1
while i <= 5:
    print(i)
    i = i + 1
else:
    print("i > 5")

l = [1,2,3,4,5]
for items in l:
    pass
print("After")

string = "Budi Luhur"
for x in string:
    if x == 'h':
        break
    print(x)

string = "Budi Luhur"
for x in string:
    if x == 'h':
        continue
    print(x)