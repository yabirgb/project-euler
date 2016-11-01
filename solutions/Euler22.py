import string

letters = dict(zip(string.ascii_uppercase, range(1,27)))

def name_sum(name):
    return sum(string.ascii_uppercase.index(x)+1 for x in name)

with open("aux/p022_names.txt", "r") as file:
    data = file.read()
    list_names = sorted(data.replace('"', '' ).split(","))

    total = sum(name_sum(name)*pos for pos,name in enumerate(list_names, 1))

    print(total)
