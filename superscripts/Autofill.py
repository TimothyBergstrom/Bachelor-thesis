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
#LIST CREATION

#Creates list with names L
namnL=[]
for i in range(0,190,10):
    namnL.append('L' + str(i))

#Creates list with names Ltail
namnLt=[]
for i in range(0,190,30):
    namnLt.append('L' + str(i)+'tail')

#Creates list with names Azo
namnAzo=[]
for i in range(0,190,10):
    namnAzo.append('Azo' + str(i))

#Creates list of folders
foldernamelist=['GS','S1', 'T1']

#Creates empty lists for each folder
for foldername in foldernamelist:
    vars()[foldername] = []

#makes list with all names
allnames=foldernamelist

#creates deg
Deg=[]
for i in range(0,190,10):
    Deg.append(i)

#Creates empty list
Emptylist=[None]*19


###########################################
#CHOOSING (inactivated)
'''
check=0
while check not in ('L','l','Lt','lt','Azo','azo'):

    print('Which molecule? L, Lt or Azo?')
    check=str(input(''))

    if check in ('L','l'):
        namn=namnL
    elif check in ('Lt','lt'):
        namn=namnLt
    elif check in ('Azo','azo'):
        namn=namnAzo
    else:
        print('wrong name!')
'''

###########################################
#CHOOSING FOLDERS (optional)

#Finds folder location
cwd = os.getcwd()

#saves root cwd
rootcwd=cwd

print('Opening GUI to choose folder')
try:
    import tkinter
    from tkinter import filedialog
    cwd = os.getcwd()
    root = tkinter.Tk()
    root.withdraw()
    print('Gui opened')
    dirname = filedialog.askdirectory(parent=root,initialdir=cwd,title='Please select a directory')
    os.chdir(dirname)
        
except (RuntimeError, TypeError, NameError):
    print('Error. You do not have Tkinter to choose folder. Put script in correct folder to proceed. There will be errros')
    input('Press enter to quit')
    quit()

###########################################
#FOLDER CREATION AND MOVEMENT

#Finds folder location
cwd = os.getcwd()

#creates datafolder
if not os.path.exists(cwd + '\\' + 'data'):
    os.makedirs(cwd + '\\' + 'data')

#Goes to Laurdan folder if it exists
if os.path.exists(cwd+'\\'+'Laurdan'):
    print('Goes to Laurdan folder')
    os.chdir(cwd+'\\'+'Laurdan')

currentcwd = os.getcwd()


###########################################
#AUTOCHOOSE (experimental)

if 'Azo' in cwd or 'azo' in cwd:
    namn=namnAzo
    print('Azobenzene has been choosen')
    choosen='Azo'
elif 'tail' in cwd:
    namn=namnLt
    print('Laurdan with tail has been choosen')
    choosen='Laurdan'
else:
    namn=namnL
    print('Laurdan without tail has been choosen')
    choosen='Laurdan'


#EVERYTHING ABOVE THIS LINE IS STANDARDIZED IN ALL SCRIPTS.
#_________________________________________________________


###########################################
#CHANGING (old code, will be broken)

#Checks for water
water=''
if 'water' in cwd:
    print('Calculation in water')
    water='SCRF=(Solvent=water)'

#Checks for density function
if 'CAM' in currentcwd:
    densityfunc='#CAM-B3LYP'
    print('CAM-B3LYP calculation for groundstate opt')
else:
    densityfunc='#B3LYP'
    print('B3LYP calculation for groundstate opt')

#Goes to folders
for i in namn:
    os.chdir(currentcwd+'\\'+i)
    F = open(i+'.com','r+')
    lines = F.readlines()
    F.close() #TA EJ BORT
    
    #Finds 0 1
    koordinat1=[hitta for hitta,x in enumerate(lines) if x == '0 1\n' or x == '0 1 \n']
    koordinat1=koordinat1[0]
    lines=lines[koordinat1:len(lines)]

    #Finds where it ends
    koordinat2=[hitta for hitta,x in enumerate(lines) if 'D' and 'F' in x]
    koordinat2=koordinat2[0]
    lines=lines[0:koordinat2+1]    

    #Removes spaces
    for a in range(0,len(lines)):
        if lines[a].startswith(' '):
            x=lines[a]
            x=x[1:]
            lines[a]=x


    if choosen == 'Laurdan':
        fix='D 14 13 9 10 F'
    else:
        fix='D 45 44 43 26 F'

    #Creates lists
    titelnamn= i + ' deg'
    titelfil='%chk=' + i + '.chk\n'
    add1=['$rungauss\n','%mem=50Gb\n', '%nprocs=32\n', titelfil,densityfunc,'/cc-pVDZ nosymm ',
          'opt(noeigentest,modredundant) TD(NStates=3, root=1) ',water,'\n','\n', titelnamn, '\n', '\n']
    add2=['\n', '\n','--Link1--\n','%mem=50Gb\n','%nprocs=32\n',titelfil, '#CAM-B3LYP/cc-pVDZ nosymm ', ' TD(NStates=2, triplets, root=1) ', 'guess=read ', 'geom=(allcheck,modredundant)','\n', '\n',fix,'\n', '\n',]
    
    #Writes front
    for a in range(len(add1)-1,-1,-1):
        lines.insert(0,add1[a])

    #Writes back
    for a in range(0,len(add2)):
        lines.append(add2[a])

    #Creates file
    F = open(i+'.com','w')
    for a in range(0,len(lines)):
        F.write(lines[a])
    F.close()

    #Creates file
    F = open(i+'excited.com','w')
    for a in range(0,len(add2)):
        F.write(add2[a])
    F.close()

print('Filling .com files successful!')
time.sleep(3)
