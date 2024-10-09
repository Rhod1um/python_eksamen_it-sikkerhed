#!/usr/bin/python3

ls = range(100) # er range(0, 100)
ls = range(1, 100) # er range(0, 100)
print(ls)
print(type(ls))

ls=[]

for i in range(100):
    if i%2 == 0:
        ls.append(i)

print(ls)

name = "veronica bistrup frydkjær"
name = name.split()
sn = name[2][::-1]
print(sn)

# set kan man tilføje og fjerne men ikke ændre eksisterende element

st = {1,2,3,3}
print(st)
print(type(st))

#st[0] = 3
print(st)

#tuple, immutable

print("tuple")
tp = (1,2,3)
summ=0
for i in tp:
    summ = summ + i
print(summ)

ls = tuple(tp)

# dict

dct = {"hej": 1, "nej": 2}

dct.update({"hejj":3})
dct["ghj"] = 9

print(dct)

print(dct.values())
print(type(dct.keys()))

for i in dct.values():
    print(i)

print("sum: ")

def add(**kwargs):
    print(type(kwargs))
    return sum(kwargs.values())

print(add(name=1,der=2,wfe=3,wef=4))

with open("challenge.py", "r") as file:
    str = file.read()
#print(str)

try: 
    str = open("challenge.py", "r")
    #print(str.read())
    str.close()
except:
    print("could not open file")


ls = list(range(1,11))
names = ["vgh", "gvhbj", "hvb"]
print(ls)
dct = {}
for i in ls:
    dct[i] = 0

print(dct)

tp = ("apple", "orange")
str = "gbhjnkmlgg"
print(type(tp))

print(str.count("g"))
print(tp.count("apple"))

dct = {"cat":3, "dog":4}
st = {1,2,3}
st.add(4)

ls=[]
def list_dict():
    for i in dct.keys():
        print(i)
        ls.append(i)
    return ls
print(list_dict())

def my_function(*args):
    if len(args) > 1:
        print("number of arguments are more than 1")
    else:
        print("not larger than 1")

my_function(1,1,1,1)

print(st)

def summ(**kwargs):
    for i in kwargs.keys():
        if kwargs[i]%2==0:
            print(f"{i} has {kwargs[i]} is even number")
        else:
            print(f"{i} has {kwargs[i]} is odd number")

summ(er=1,we=2,et=3)

ls = list(range(1,101))
print(ls)
for i in (range(100)):
    print(i)

ls = (7,4)
print(sorted(ls)) #alt efter sorted() er en liste
# dict og set kan ikke bruge slice
print(ls[::1]) #printer hele listen fordi : er start tal, : er slut og 1 er "jump"
# mens 
print(ls[:1]) #printer første element da start er : og 1 er slut elementet og jump er bare 1 som default
#^^den printer første element fordi den går op til 1 element hvilket er 2. element fordi det starter på 0
print(ls[:0]) # giver 0 fordi den starter på 1 element og går op til, men uden at inkludere, 0
# første element er inkludiv og andet er eksklusiv. Samme med range
print(ls[:-1])

str = "vero-fry"
name = str.split("-")
dct = {"for":name[0], "eft":name[1]}
for i in dct.values():
    print(i[::-1])

