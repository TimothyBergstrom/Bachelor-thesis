print('This program checks .zmat files if correct rotation has been done\n')

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

if 'Azo' in cwd:
    namn=namnAzo
    print('Azobenzene has been choosen')
elif 'tail' in cwd:
    namn=namnLt
    print('Laurdan with tail has been choosen')
else:
    namn=namnL
    print('Laurdan without tail has been choosen')


#EVERYTHING ABOVE THIS LINE IS STANDARDIZED IN ALL SCRIPTS.
#_________________________________________________________



###########################################
#CHECKING (old code)
for foldername in foldernamelist:
    #os.chdir(cwd+'\\'+foldername) #Goes to correct folder
    currentcwd = os.getcwd()
    valuelist=[]
    print(str(foldername))
    print('\n')
    for i in namn:
        os.chdir(currentcwd+'\\'+i) #Goes to all folders inside
        F = open(i+'.zmat','r+')
        lines = F.readlines()
        F.close() #TA EJ BORT

        #Finds where the data is located
        if check == ('Lt' or 'lt'):
            where=[a for a,x in enumerate(lines) if 'dih14' in x]
        elif

        foundstring=lines[where[len(where)-1]]

        if str(tic) in foundstring:
            print('correct')
        else:
            print('Incorrect!'+'Ltail' + str(tic))

    #reset folder
    os.chdir(cwd)

input('Press enter to end')
