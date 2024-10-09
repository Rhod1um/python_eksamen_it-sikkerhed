#!/usr/bin/python3

import challenge
import re

game=challenge.client(ip_address="cybergame.dk",port=39594)

game.login("vero1609","Frydkjær")

# spm 0

game.question(0)

print(game.data(0))

# game.answer(game.data(0))

def my_answer0(my_var):
    return my_var

game.answer(0, my_answer0(game.data(0)))

# spm 1

game.question(1)

print(game.data(1))

def my_answer1(my_var):
    return my_var*2
    
game.answer(1, my_answer1(game.data(1)))

# spm 2

game.question(2)

print(game.data(2))

def my_answer2(my_var):
    return my_var.upper()
    
game.answer(2, my_answer2(game.data(2)))

# spm 3

game.question(3)

print(game.data(3))
    
def my_answer3(my_var):
    return my_var[::-1]

game.answer(3, my_answer3(game.data(3)))
    
# spm 4

game.question(4)

print(game.data(4))

# it can't return my_var.sort() directly

def my_answer4(my_var):
    return sorted(my_var)

game.answer(4, my_answer4(game.data(4)))
    
# spm 5

game.question(5)

print(game.data(5))

# slicing 
def my_answer5(my_var):
    return my_var[0:3]

game.answer(5, my_answer5(game.data(5)))

# spm 6

game.question(6)

print(game.data(6))

# list comprehension
def my_answer6(my_var):
    return [x*5 for x in my_var]

game.answer(6, my_answer6(game.data(6)))

# spm 7

game.question(7)

print(game.data(7))

# slicing
def my_answer7(my_var):
    return my_var[5]

game.answer(7, my_answer7(game.data(7)))

# spm 8

game.question(8)

print(game.data(8))

# slicing
def my_answer8(my_var):
    t = set(my_var)
    ls = list(t)
    return sorted(ls)

game.answer(8, my_answer8(game.data(8)))

# spm 9

game.question(9)

print(game.data(9))
   
def my_answer9(my_var):
    return my_var.replace('be','python')
    
game.answer(9, my_answer9(game.data(9)))

# spm 10

game.question(10)

print(game.data(10))

def my_answer10(my_var):
    ls = my_var.split()
    for i in range(len(ls)):  
        if ls[i] =="star":
            ls[i] = "star"[::-1]
    ls = " ".join(ls)
    return ls

game.answer(10, my_answer10(game.data(10)))

# spm 11

game.question(11)

print(game.data(11))

def my_answer11(my_var):
    i = 0
    ls = [my_var]
    while len(ls) < 20:
        my_var = my_var + 5
        ls.append(my_var)
    return ls
        
game.answer(11, my_answer11(game.data(11)))

# spm 12

game.question(12)

print(game.data(12))

def my_answer12(my_var):
    count = 0
    ip = '192.168.1.212'
    for i in my_var:
        if i[0] == ip:
            return i[1]

game.answer(12, my_answer12(game.data(12)))

# spm 13

game.question(13)

print(game.data(13))

def my_answer13(my_var):
    count = 0
    for i in my_var:
        count = count + i
    return count

game.answer(13, my_answer13(game.data(13)))
        
# spm 14

game.question(14)

print(game.data(14))
print(type(game.data(14)))

def my_answer14(my_var):
    ny_ls = []
    ls = my_var.split(",")
    for i in ls:  
        t = tuple(i.split(":"))
        ny_ls.append(t)
    return ny_ls

game.answer(14, my_answer14(game.data(14)))

# spm 15

game.question(15)

print(game.data(15))

def my_answer15(my_var):
    del(my_var['192.168.1.243'])
    return my_var

game.answer(15, my_answer15(game.data(15)))

# spm 16

game.question(16)

print(game.data(16))

def my_answer16(my_var):
    ls = my_var.split()
    for i in ls:
        my_var = my_var.replace(i, i[::-1])
    print(my_var)    
    return my_var


game.answer(16, my_answer16(game.data(16)))

# spm 17

game.question(17)

print(game.data(17))

def my_answer17(my_var):
    ls=[]
    i = 0
    while i < 10:
        ls.append(my_var)
        i=i+1
    print(ls)
    return ls

game.answer(17, my_answer17(game.data(17)))

# spm 18

game.question(18)

print(game.data(18))

def my_answer18(my_var):
    my_var["yellow"]=22
    print(my_var)
    return my_var

game.answer(18, my_answer18(game.data(18)))

# spm 19

game.question(19)

def my_answer19(my_var):
    ips = []
    ls = my_var.split(" ")
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_matches = re.findall(ip_pattern, my_var)
    ips = set(ip_matches)
    return ips
    
game.answer(19, my_answer19(game.data(19)))
    
# spm 20

game.question(20)

def my_answer20(my_var):
    statuses = {}
    count = 0
    ls = my_var.split(" ")
    status_pattern = r'\ \d{3}\ '
    status_matches = re.findall(status_pattern, my_var)
    
    status_matches_nw = []
    for i in status_matches:
        status_matches_nw.append(i.strip())
    
    for i in status_matches_nw:
        statuses[i] = status_matches_nw.count(i)
    print(statuses)
    return statuses
    
game.answer(20, my_answer20(game.data(20)))

# spm 21

game.question(21)

def my_answer21(my_var):
    sum = 0
    count = 0
    avg = 0
    sizes = []
    ls = my_var.split(" - - ")
    res_pattern = r'\ \d{4,5}\n'
    for i in range(len(ls)):
        if " 200 " in ls[i]:
            size = re.findall(res_pattern, ls[i])
            sizes.append(int(size[0]))
    print(sizes)
    for i in sizes:
        sum = sum + int(i)
        count = count+1
    avg = sum / count
    return int(avg)
    
game.answer(21, my_answer21(game.data(21)))

# spm 22

game.question(22)

def my_answer22(my_var):
    count = 0
    png_pattern = r'png'
    png_matches = re.findall(png_pattern, my_var)
    return png_matches.count("png")

game.answer(22, my_answer22(game.data(22)))

# spm 23

game.question(23)

def my_answer23(my_var):
    series = {}
    for i in my_var:
        series[i[1]] = i[0]
    print(type(series))
    return series
    
game.answer(23, my_answer23(game.data(23)))

# spm 24

game.question(24)

print(game.data(24))

def my_answer24(my_var):
    ls = []
    for i in range(101):
        if i % 3 != 0:
            ls.append(i)
    lss = sorted(ls)
    print(lss)
    return lss

game.answer(24, my_answer24(game.data(24)))

# spm 25

game.question(25)

print(game.data(25))

def my_answer25(my_var):
    hash = 0
    code = list(4)
    letters = "abcdefghijklmnopqrstuvwxyz"
    while my_var != hash:
        for i in letters:
            code = i
        hash = code.sha1()

# spm 26

game.question(26)

print(game.data(26))

# spm 27

game.question(27)

print(game.data(27))

def my_answer27(my_var):
    return "network"
    
game.answer(27, my_answer27(game.data(27)))

# spm 28

game.question(28)

print(game.data(28))

print(type(game.data(28)))

def my_answer28(my_var):
    return "a4:67:06:8d:83:a1"
    
game.answer(28, my_answer28(game.data(28)))

# spm 29

game.question(29)

print(game.data(29))

def my_answer29(my_var):
    return 39

game.answer(29, my_answer29(game.data(29)))

# spm 30

game.question(30)

print(game.data(30))

def my_answer30(my_var):
    return 3775708311

game.answer(30, my_answer30(game.data(30)))

# Der er en GET style.css, så ACK og det er IKKE den rigtige ACK
# så er der 200 OK for (text/css) (noget andet) og så er der den rigtige ACK 
# de to der ikke er relevante har samme ack nr
# men relatic ack på GET er 9979 og det næste er over tusing så det passer med at size
# er plusset på, men hvor ser man size? 

# spm 31

game.question(31)

print(game.data(31))

def my_answer31(my_var):
    return "0.client-channel.google.com"

game.answer(31, my_answer31(game.data(31)))

# spm 32

game.question(32)

print(game.data(32))

def my_answer32(my_var):
    return 3728276336+140  # segment number + payload size = ack number

game.answer(32, my_answer32(game.data(32)))

# spm 33

game.question(33)

print(game.data(33))

def my_answer33(my_var):
    my_var = int(my_var)
    tcp_header = 20
    udp_header = 8
    return (my_var + tcp_header, my_var + udp_header)  # laver tuple direkte

game.answer(33, my_answer33(game.data(33)))

# spm 34

game.question(34)

print(game.data(34))

def my_answer34(my_var):
    room = 0
    floor = 0
    for i in my_var:
        if i == "^":
            floor = floor + 1
        if i == "v":
            floor = floor - 1
        if i == ">":
            room = room + 1
        if i == "<":
            room = room - 1
    return (floor, room)

game.answer(34, my_answer34(game.data(34)))

# spm 35

game.question(35)

print(game.data(35))








