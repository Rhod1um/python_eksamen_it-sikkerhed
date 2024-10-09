#!/usr/bin/python3

print("hej")

def fkt(*args):
    str=""
    for i in args:
        str = str+i
    return str

print(fkt("der","tyu", "gyhu"))

ls=[]

for i in range(0,101,-1):
    ls.append(i)

print(ls)
