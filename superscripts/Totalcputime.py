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
#CHOOSING

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


###########################################
#CHOOSING FOLDERS (optional)

#Finds folder location
cwd = os.getcwd()

#saves root cwd
rootcwd=cwd

print('GUI to choose folder? Needs Tkinter. Y or N')
guiornot=input('')

if guiornot in ('Y','y'):
    try:
        import tkinter
        from tkinter import filedialog
        cwd = os.getcwd()
        root = tkinter.Tk()
        root.withdraw()
        dirname = filedialog.askdirectory(parent=root,initialdir=cwd,title='Please select a directory')
        os.chdir(dirname)
        
    except (RuntimeError, TypeError, NameError):
        print('Error. You do not have Tkinter to choose folder. Put script in correct folder to proceed')
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
    print('Goes to Laurdan folder\n')
    os.chdir(cwd+'\\'+'Laurdan')

currentcwd = os.getcwd()

#EVERYTHING ABOVE THIS LINE IS STANDARDIZED IN ALL SCRIPTS.
#_________________________________________________________


###########################################
#FETCHING AND CONVERTING (old code, will be broken)

import math

##WITHOUT TAIL
for foldername in foldernamelist:
    os.chdir(cwd+'\\'+foldername) #Goes to correct folder
    currentcwd = os.getcwd()

    for i in namn:
        os.chdir(currentcwd+'\\'+i) #Goes to all folders inside
        F = open(i+'.log','r+') #Opens log file
        lines = F.readlines()
        F.close() #TA EJ BORT

        #Finds where the data is located
        where=[a for a,x in enumerate(lines) if 'Job cpu time:  ' in x]  

        #Finds if TP has been done
        if len(where) == 1:
            #Removes all values that have not been converged
            foundstring=lines[where[len(where)-1]]

            #cuts string
            foundstring=foundstring[15:]

            #searches string times
            for x in times:
                if x == 'days':
                    searchvalue = re.search(' (.*?)'+x, foundstring)
                if x == 'hours':
                    searchvalue = re.search('days (.*?)'+x, foundstring)
                if x == 'minutes':
                    searchvalue = re.search('hours (.*?)'+x, foundstring)
                if x == 'seconds':
                    searchvalue = re.search('minutes (.*?)'+x, foundstring)

                if searchvalue:
                    valuestring = searchvalue.group(1)
            
                    #Converts value to float (decimal values)
                    value=float(valuestring)
             
                    #saves in list
                    vars()[x].append(value)
            
        else:

            for multicalculations in range(1,3): #If ES has been calculated
                foundstring=lines[where[len(where)-multicalculations]]

                #cuts string
                foundstring=foundstring[15:]

                #searches string times
                for x in times:
                    if x == 'days':
                        searchvalue = re.search(' (.*?)'+x, foundstring)
                    if x == 'hours':
                        searchvalue = re.search('days (.*?)'+x, foundstring)
                    if x == 'minutes':
                        searchvalue = re.search('hours (.*?)'+x, foundstring)
                    if x == 'seconds':
                        searchvalue = re.search('minutes (.*?)'+x, foundstring)

                    if searchvalue:
                        valuestring = searchvalue.group(1)
            
                    #Converts value to float (decimal values)
                        value=float(valuestring)
             
                    #saves in list
                        vars()[x].append(value)


        #Closes file
        F.close()

    #reset folder
    os.chdir(cwd)
        

#sum of all floats
for x in times:
    vars()[x+'total']=sum(vars()[x])

save=0
debugsave=[]
debugbeforesave=[]
debugclock=[]
tic=0 #I had some problems with if statements. This fixes it
#some fixing
for x in reversed(times):
    vars()[x+'value'] = vars()[x+'total'] + save #adds extra

    if x is 'seconds':
        clock=60
        debugclock.append(clock)
    elif x is 'minutes':
        clock=60
        debugclock.append(clock)
    else:
        clock=24
        debugclock.append(clock)
    
    beforesave=vars()[x+'value']/clock
    save=math.floor(beforesave)
    debugsave.append(save)
    debugbeforesave.append(beforesave)
    vars()[x+'fixed']=(vars()[x+'value'])%clock #changes
    


totaltime=[]
#makes list
for x in times:
    totaltime.append(vars()[x+'fixed'])

#goes to data folder
os.chdir(cwd+'\\'+'data')

#saves a csv
with open('totalCPUtime'+'.csv', 'w') as F:
    wr = csv.writer(F, delimiter='\n')
    wr.writerow(totaltime)
    wr.writerow(times)


F.close()

    
###########################################
#CSV INTO MAIN FOLDER

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
F=open('data'+csvname+'.csv','w')
wr=csv.writer(F,delimiter='\n')
wr.writerow(linesfix)
F.close()

print('\nCsv file writing successful! Data can now be found in data folder in the root folder (location of scripts)')
time.sleep(3)



