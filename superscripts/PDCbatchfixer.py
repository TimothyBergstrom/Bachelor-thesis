print('This program creates .sh files for PDC SLURM\n')

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
elif 'tail' in cwd:
    namn=namnLt
    print('Laurdan with tail has been choosen')
else:
    namn=namnL
    print('Laurdan without tail has been choosen')


#EVERYTHING ABOVE THIS LINE IS STANDARDIZED IN ALL SCRIPTS.
#_________________________________________________________



###########################################
#FIXING

for i in namn:
    os.chdir(currentcwd+'\\'+i)


    #Adds dir location
    cutcwd=cwd
    cutlocation=[a for a,x in enumerate(cutcwd) if '\\' in x]
    cutcwd=cutcwd[(cutlocation[-2]+1):]
    dirname=cutcwd
    dirname=dirname.replace('\\','/')
    dirname=dirname

    add1=['#!/bin/bash\n',
          '#SBATCH -A m.2017-1-102\n',
          '#SBATCH -J ', i, '\n',
          '#SBATCH -t 20:00:00\n',
          '#SBATCH --nodes=1\n',
          '#SBATCH --ntasks-per-node=32\n',                                                                                                             
          '#SBATCH --ntasks-per-node=32\n',                                                                                                    
          'module load gaussian/g09.D01\n',
          '\n',
          'export g09root=/afs/.pdc.kth.se/pdc/vol/gaussian/G09RevD.01\n',
          '\n',
          'export GAUSS_SCRDIR=/cfs/klemming/scratch/t/tib/',dirname,'\n'
          '\n',
          'source $g09root/g09/bsd/g09.profile\n'
          '\n',
          'cd $PBS_O_WORKDIR\n',
          '\n',
          'STARTDIR=$SLURM_SUBMIT_DIR\n',
          '\n',
          'job=',i,'\n',
          '\n',
          'SCRATCHDIR=/cfs/klemming/scratch/t/tib/',dirname,'/$job',
          '\n',
          'mkdir -p $SCRATCHDIR\n',
          '\n',
          'cd $STARTDIR\n',
          '\n',
          'cp $STARTDIR/$job.com $SCRATCHDIR\n',
          '\n',
          'cd $SCRATCHDIR\n',
          '\n',
          '/afs/.pdc.kth.se/pdc/vol/gaussian/G09RevD.01/g09/g09 ', #Do not add \n here!
          i,'.com &> ',i,'.log\n',
          '\n',
          'cp ',i,'.log $SLURM_SUBMIT_DIR\n',
          'cp ',i,'.chk $SLURM_SUBMIT_DIR\n',
          '\n',
          'cd $SLURM_SUBMIT_DIR\n',
          '\n']


    #Creates file
    F = open('run'+i+'.sh','wb')
    for a in range(0,len(add1)):
        line=add1[a]
        linebyte=str.encode(line)
        F.write(linebyte)
    F.close()
print('Finished creating files')
time.sleep(3)

