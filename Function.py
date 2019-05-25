# Function.py
# tips : sebaiknya function hanya mengembalikan nilai. tidak mencetak aoutput

def hello(name="Budi Luhur"):
    """
    Created By : Rahman
    Input : 1 - String
    Output : 1 - String
    """
    return "Hello, "+name

def hitung(a=5, b=4):
    return a*b

print(hello())
print(hello("rahman"))
print(hitung())
print(hitung(1,2))