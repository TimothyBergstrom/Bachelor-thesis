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

#Needed for calculations
import math


###########################################
#LIST CREATION

Tlist=[]
Glist=[]

namelist=['T','G']

###########################################
#CHOOSING FOLDERS (optional)

#Finds folder location
cwd = os.getcwd()

#saves root cwd
rootcwd=cwd

print('Opening GUI to choose file')
try:
    import tkinter
    from tkinter import filedialog
    cwd = os.getcwd()
    root = tkinter.Tk()
    root.withdraw()
    print('Gui opened')
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename()
        
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
    

#EVERYTHING ABOVE THIS LINE IS STANDARDIZED IN ALL SCRIPTS.
#_________________________________________________________


###########################################
#FETCHING DATA

F=open(filename,'r')
lines = F.readlines()
F.close()
Tsave=0

#T
location1=[i for i,x in enumerate(lines) if ('Temperature' in x) and ('Kelvin' in x) and ('Pressure' in x) and ('Atm.' in x)]
#location1=location1fix[0::2]
for i in location1:
    foundstring=lines[i]
    searchvalue = re.search('Temperature (.+?) Kelvin', foundstring)
    if searchvalue is None:
        print('ERROR in T')
    valuestring = searchvalue.group(1)
    value=float(valuestring)
    T=value
    if T==Tsave:
        _donothing=1 #print('ignoring value')
    else:
        Tsave=T
        Tlist.append(T)


#G
location2=[i for i,x in enumerate(lines) if ('Sum of electronic and thermal Free Energies' in x)]
for i in location2:
    foundstring=lines[i]
    searchvalue = re.search('= (.+?)\n', foundstring)
    if searchvalue is None:
        print('ERROR in G')
    valuestring = searchvalue.group(1)
    value=float(valuestring)
    G=value
    Glist.append(G)


#Relative G
relativelist=[]
print('Makes G values relative')
if None in Glist:
    print('Empty values detected in GS, fixing list.')
minvalue=min(x for x in Glist if x is not None)
for i in range(len(Glist)):
    i=Glist[i]
    if i is not None:
        relativelist.append(i-minvalue)
    elif i is None:
        relativelist.append(i)
#Glist=relativelist
#NOT RELATIVE
'''
#H and S
location3before=[i for i,x in enumerate(lines) if ('KCal/Mol' in x) and ('Cal/Mol-Kelvin' in x) and ('Cal/Mol-Kelvin' in x)]
location3 = [x+1 for x in location3before]
for i in location3:
    foundstring=lines[i]
    valuestring=foundstring[6:]
    valuelist=valuestring.split(' ')


    #Removes empty
    valuelist = list(filter(None, valuelist))
    
    #H kcal/mol
    valuestring=valuelist[0]
    value=float(valuestring)
    H=value
    Hlist.append(H)

    #S cal/mol
    valuestring=valuelist[2]
    value=float(valuestring)
    value=value/1000 #change to kcal/mol
    S=value
    Slist.append(S)
'''

'''	
#X
R=8.314462175
for i in range(0,len(Slist)):
    Xlist.append(math.exp(-Glist[i]/(R*Tlist[i])))
'''

###########################################
#CSV INTO MAIN FOLDER

print('Writing csv file in main folder...')

#creates datafolder
if not os.path.exists(rootcwd + '\\' + 'data'):
    os.makedirs(rootcwd + '\\' + 'data')

#Finds name of saving
cutcwd=filename
cutlocation=[a for a,x in enumerate(cutcwd) if '/' in x]
cutcwd=cutcwd[(cutlocation[-1]+1):]
csvname=cutcwd

#Goes to dataroot
os.chdir(rootcwd+'\\'+'data')

#zips everything
ziplist=[Tlist,Glist]

#transposes ziplist
ziptransposed=list(map(list, zip(*ziplist)))
ziptransposednames=list(map(list, zip(*namelist)))
#ziptransposed=ziplist

#writes everything
F=open(csvname+'freq'+'.csv','w')
wr=csv.writer(F,delimiter='\n')
wr.writerow(ziptransposednames)
wr.writerow(ziptransposed)
F.close()


###########################################
#CSV FIXING TO IMPORT IN MATLAB

#removes [ and ]
F=open(csvname+'freq'+'.csv','r')
lines=F.readlines()
F.close()

q=[]
for y in lines:
    x=y
    x=x.replace('[', '')
    x=x.replace(']', '')
    x=x.replace('None','NaN')
    x=x.replace('\n','')
    x=x.replace("'",'')
    q.append(x)
linesfix=q


#rewrites everything
F=open(csvname+'freq'+'.csv','w')
wr=csv.writer(F,delimiter='\n')
wr.writerow(linesfix)
F.close()

print('Csv file writing successful!')
time.sleep(3)
