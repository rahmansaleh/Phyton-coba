# For.py

my_list = [1,2,3,4,5]

for x in my_list:
    print(x)

for x in my_list:
    if x % 2 == 0:
        print(x)

string  = "Budi Luhur"
for x in string:
    print(x)

my_list = [(1,2), (3,4), (5,6), (7,8)]
print(len(my_list))

for tup in my_list:
    print(tup)

for a,b in my_list:
    print(a,b)

for a,b in my_list:
    print(a)

my_dict = {"k1":1, "k2":2, "k3":3}
for i in my_dict:
    print(i)

for i in my_dict.items():
    print(i)

for a,b in my_dict.items():
    print(b)