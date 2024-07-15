# Android lock patterns generator
# Amerthatsme

from itertools import product
from time import time
# List of all n-digit combinations
p1 = ['1','2','3','4','5','6','7','8','9']
p2= []
p3= []
p4= []
p5= []
p6= []
p7= []
p8= []
p9= []

# Read files to load computed combinations
f2=open('p2.txt','r')
for i in f2.readlines():
    p2.append(i[:-1])
f2.close()

f3=open('p3.txt','r')
for i in f3.readlines():
    p3.append(i[:-1])
f3.close()

f4=open('p4.txt','r')
for i in f4.readlines():
    p4.append(i[:-1])
f4.close()

f5=open('p5.txt','r')
for i in f5.readlines():
    p5.append(i[:-1])
f5.close()

f6=open('p6.txt','r')
for i in f6.readlines():
    p6.append(i[:-1])
f6.close()

f7=open('p7.txt','r')
for i in f7.readlines():
    p7.append(i[:-1])
f7.close()

f8=open('p8.txt','r')
for i in f8.readlines():
    p8.append(i[:-1])
f8.close()

f9=open('p9.txt','r')
for i in f9.readlines():
    p9.append(i[:-1])
f9.close()

# All possible single connections
con = {'1':('2','4','5','6','8'), '2':('1','3','4','5','6','7','9'),
       '3':('2','4','5','6','8'), '4':('1','2','3','5','7','8','9'),
       '5':('1','2','3','4','6','7','8','9'), '6':('1','2','3','5','7','8','9'),
       '7':('2','4','5','6','8'), '8':('1','3','4','5','6','7','9'),
       '9':('2','4','5','6','8')}

def p2_gen():
    for i in p1:
        for j in con[i]:
            p2.append(i+j)

    f=open('p2.txt','w')
    for n in p2:
        f.write(n+'\n')
    f.close()

def p3_gen():
    for i in p2:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p3.append(i+k)

    f=open('p3.txt','w')
    for n in p3:
        f.write(n+'\n')
    f.close()

def p4_gen():
    for i in p3:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p4.append(i+k)

    f=open('p4.txt','w')
    for n in p4:
        f.write(n+'\n')
    f.close()

def p5_gen():
    for i in p4:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p5.append(i+k)

    f=open('p5.txt','w')
    for n in p5:
        f.write(n+'\n')
    f.close()

def p6_gen():
    for i in p5:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p6.append(i+k)

    f=open('p6.txt','w')
    for n in p6:
        f.write(n+'\n')
    f.close()

def p7_gen():
    for i in p6:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p7.append(i+k)

    f=open('p7.txt','w')
    for n in p7:
        f.write(n+'\n')
    f.close()

def p8_gen():
    for i in p7:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p8.append(i+k)

    f=open('p8.txt','w')
    for n in p8:
        f.write(n+'\n')
    f.close()

def p9_gen():
    for i in p8:
        for j in con[i[-1]]:
            for k in j:
                if k not in i:
                    p9.append(i+k)

    f=open('p9.txt','w')
    for n in p9:
        f.write(n+'\n')
    f.close()

def all_combos():
    n=0
    for i in (p4,p5,p6,p7,p8,p9):
        n+=len(i)
    print(n)

def generate():
    start = time()
    p2_gen()
    p3_gen()
    p4_gen()
    p5_gen()
    p6_gen()
    p7_gen()
    p8_gen()
    p9_gen()
    stop = time()
    print('Time: '+str(stop-start)+' seconds')

generate()
# It took 1.6652418070572457 seconds to generate!!!!!!!!!
