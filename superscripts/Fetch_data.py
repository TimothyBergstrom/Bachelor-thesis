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
#if not os.path.exists(cwd + '\\' + 'data'):
#    os.makedirs(cwd + '\\' + 'data')

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

print(' ')

#EVERYTHING ABOVE THIS LINE IS STANDARDIZED IN ALL SCRIPTS.
#_________________________________________________________


###########################################
#FETCHING DATA

itt=0
printed=0

for foldername in foldernamelist:
    valuelist=[]
    lines=[]
    for i in namn:
        lines=[]
        try:           
            os.chdir(currentcwd+'\\'+i) #Goes to all folders inside
            if (os.path.isfile(i +'.log')) and foldername=='GS':
                F = open(i+'.log','r+') #Opens log file
                lines = F.readlines()
                F.close() #TA EJ BORT
            elif foldername=='GS':
                F = open(i+'excited'+'.log','r+') #Opens log file
                print('No log files for GS in ', i, ', using excited log')
                lines = F.readlines()
                F.close() #TA EJ BORT

            if os.path.isfile(currentcwd+'\\'+i+'\\'+i+'excited.log') and (foldername == 'S1' or foldername == 'T1'):
                if printed!=1:
                    print('Found fixed files. Using them instead')
                    printed=1
                F = open(i+'excited'+'.log','r+') #Opens log file
                lines = F.readlines()
                F.close() #TA EJ BORT

            if lines==[]:
                print('ERROR! Lines empty in ', i, ' state ',foldername)

            if (os.path.isfile(i +'fix'+'.log')) and foldername=='T1':
                F = open(i+'fix'+'.log','r+') #Opens log file
                print('Special: Fixed files for T1')
                lines = F.readlines()
                F.close() #TA EJ BORT

            if foldername=='GS':
                #Finds where the data is located
                if 'B3LYP' in cwd and 'CAM' not in cwd:
                    where=[a for a,x in enumerate(lines) if 'E(RB3LYP)' in x and 'SCF Done' in x]
                elif 'CAM-B3LYP' in cwd:
                    wheretocut=[a for a,x in enumerate(lines) if 'Job cpu time:' in x ] 
                    where=[a for a,x in enumerate(lines) if 'E(RCAM-B3LYP)' in x and 'SCF Done' in x]
            elif foldername=='S1':
                where=[a for a,x in enumerate(lines) if 'Excited State   1:'
                       in x and 'Singlet-?Sym' in x]
                if where==[]:
                        where=[a for a,x in enumerate(lines) if 'Excited State   1:'
                       in x and 'Singlet-A' in x]
            elif foldername=='T1':
                where=[a for a,x in enumerate(lines) if 'Excited State   1:' in x 
                        and 'Triplet-?Sym' in x]
                if where==[]:
                    where=[a for a,x in enumerate(lines) if 'Excited State   1:'
                       in x and 'Triplet-A' in x]
            else:
                print('ERROR! Cannot find correct values')
                
            if where==[]:
                print('ERROR! Problem in ' + foldername + ' and ' + i)

            #Removes all values that have not been converged
            foundstring=lines[where[-1]]

            #searches string
            if foldername=='GS':
                searchvalue = re.search('=  (.+?) A.U', foundstring)
            elif foldername=='S1':
                searchvalue = re.search('Sym (.+?) eV', foundstring)
                if searchvalue is None:
                    searchvalue = re.search('A (.+?) eV', foundstring)
            elif foldername=='T1':
                searchvalue = re.search('Sym (.+?) eV', foundstring)
                if searchvalue is None:
                    searchvalue = re.search('A (.+?) eV', foundstring)

            #DEBUG
            #print(foldername + foundstring)

            valuestring = searchvalue.group(1)

            #Converts value to float (decimal values)
            value=float(valuestring)

            if foldername=='GS':
                #eV
                value=value*27.2114
                
            #Adds to valuelist
            valuelist.append(value)

            print('Values recovered from ', i)
            
            #Closes file
            F.close()
            
        except:
            print('Error in ', i,', setting value to NaN')
            value=None
            valuelist.append(value)
            
    print('Fetching ' + foldername + ' data was successful! Saving data...')
    
    #saves data as list
    vars()[foldername+'data'] = valuelist

    #saves data as list (debugging)
    vars()[foldername+'data'+'debug'] = valuelist

    #reset folder
    os.chdir(cwd)

    try:
        #Closes file
        F.close()
    except:
        donothing=1

    print(' ')


###########################################
#MANAGING DATA 1

relativelist=[]
#makes relative
print('Makes GS values relative')
if None in GSdata:
    print('Empty values detected in GS, fixing list.')
minvalue=min(x for x in GSdata if x is not None)
for i in range(len(GSdata)):
    i=GSdata[i]
    if i is not None:
        relativelist.append(i-minvalue)
    elif i is None:
        relativelist.append(i)
GSdata=relativelist

S1datarelative=[]
for x,y in zip(S1data, GSdata):
    if x==None or y==None:
        add=None
    else:
        add=x+y
    S1datarelative.append(add)

T1datarelative=[]
for x,y in zip(T1data, GSdata):
    if x==None or y==None:
        add=None
    else:
        add=x+y
    T1datarelative.append(add)
    
S1data=S1datarelative
T1data=T1datarelative

print('Relative values to array successful')
    
###########################################
#MANAGING DATA 2

#creates kcal/mol
for x in allnames:
    vars()[x+'kcal'+'data']=[]

#creates kcal/mol
for x in allnames:
    for i in range(0,len(vars()[x+'data'])):
        if vars()[x+'data'][i] == None:
            vars()[x+'kcal'+'data'].append(None)
        else:
            vars()[x+'kcal'+'data'].append(vars()[x+'data'][i]*23.0609)

#adds deg to allnames
allnames.insert(0,'Deg')

#zips everything
ziplist=[Deg,GSdata,S1data,T1data,
         GSkcaldata, S1kcaldata, T1kcaldata]

#transposes ziplist
ziptransposed=list(map(list, zip(*ziplist)))

###########################################
#WRITING CSV

#print('Writing csv file in choosen folder...')

#goes to data folder
os.chdir(rootcwd+'\\'+'data')

#saves data as csv file
F=open(choosen+'.csv', 'w')

#writer
wr = csv.writer(F, delimiter=',')
wr.writerow(allnames)
wr = csv.writer(F, delimiter='\n')
wr.writerow(ziptransposed)

F.close()


###########################################
#CSV FIXING TO IMPORT IN MATLAB

#removes [ and ]
F=open(choosen+'.csv','r')
lines=F.readlines()
F.close()

q=[]
for y in lines:
    x=y
    x=x.replace('[', '')
    x=x.replace(']', '')
    x=x.replace('None','NaN')
    x=x.replace('\n','')
    q.append(x)
linesfix=q


#rewrites everything
F=open(choosen+'.csv','w')
wr=csv.writer(F,delimiter='\n')
wr.writerow(linesfix)
F.close()
os.remove(choosen+'.csv')

#print('Csv file writing successful!')


###########################################
#CSV INTO MAIN FOLDER

print('Writing csv file in main folder...')

#creates datafolder
if not os.path.exists(rootcwd + '\\' + 'data'):
    os.makedirs(rootcwd + '\\' + 'data')

#Finds name of saving
cutcwd=cwd
cutlocation=[a for a,x in enumerate(cutcwd) if '\\' in x]
cutcwd=cutcwd[(cutlocation[-1]+1):]
csvname=cutcwd

#Goes to dataroot
os.chdir(rootcwd+'\\'+'data')

#writes everything
F=open(choosen+csvname+'.csv','w')
wr=csv.writer(F,delimiter='\n')
wr.writerow(linesfix)
F.close()

print('Csv file writing successful!')
time.sleep(3)
