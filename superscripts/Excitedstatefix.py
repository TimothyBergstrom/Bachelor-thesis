print('This program was made to add the correctly done calculations of TD. New .com files are made to fix it')

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
#CREATING FILES

water=''
if 'water' in cwd:
    print('Calculation in water')
    water='SCRF=(Solvent=water)'

#Goes to folders
for i in namn:

    os.chdir(currentcwd+'\\'+i)

    #skapar lägga till list
    titelnamn= i + ' deg'
    titelfil='%chk=' + i + '.chk\n'
    if choosen == 'Azo':
        fix=['\n','D 45 44 43 26 F','\n','\n']
    else:
        fix=['\n','D 14 13 9 10 F','\n','\n']
        
    add2=['$rungauss\n','%mem=50Gb\n','%nprocs=32\n',titelfil,
          '#CAM-B3LYP/cc-pVDZ opt(noeigentest,modredundant) nosymm ', water, ' TD(NStates=3, root=1) ',
          'guess=read ', 'geom=allcheck', '\n', '\n',str(fix),'--Link1--\n',
          '$rungauss\n','%mem=50Gb\n','%nprocs=32\n',titelfil,
          '#CAM-B3LYP/cc-pVDZ nosymm ', water, ' TD(NStates=2, triplets, root=1) ',
          'guess=read ', 'geom=allcheck','\n', '\n']

    #stänger fil
    F = open(i+'excited'+'.com','w')
    for a in range(0,len(add2)):
        F.write(add2[a])
    F.close()   

print('DONE!')
time.sleep(3)

