print('This program fetches data from log files and writes it as a csv file\n')

###########################################
#IMPORTING

#Imports OS
import os

#Needed for fetching data from string
import re

#Needed to create csv
import csv

#Needed for sleep
import time

###########################################
#CHANGING (old code, will be broken)

namn=input('Namn= ')

i=namn
#Creates lists
titelnamn= i + ' deg'
titelfil='%chk=' + i + '.chk\n'
templist=[]
for a in range(0,500,20):
    templist.append(str(float(a)))

structure=[' 1.0 1.0\n', '12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n'
           ,'14.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n','12.0\n'
           ,'16.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n'
           ,'1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','1.0\n','\n','\n']
add1=['$rungauss\n','%mem=50Gb\n','%nprocs=20\n',titelfil,'#CAM-B3LYP/cc-pVDZ freq=(readiso,HinderedRotor) guess=read geom=allcheck\n','\n']
add2=['--Link1--\n','%mem=50Gb\n','%nprocs=20\n',titelfil,'#CAM-B3LYP/cc-pVDZ freq=(readiso,HinderedRotor) guess=read geom=allcheck\n','\n']
#Creates file
F = open(i+'.com','w')
for a in add1:
    F.write(a)
F.write('1.0')
for a in structure:
    F.write(a)
for a in range(1,len(templist)):
    for aa in add2:
        F.write(aa)
    F.write(templist[a])
    for a in structure:
        F.write(a)
F.close()

print('Filling .com files successful!')
time.sleep(3)
