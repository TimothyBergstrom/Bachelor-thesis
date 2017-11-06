print('MAIN\n')

###########################################
#IMPORTING

#Imports OS
import os

#Needed for sleep
import time

#GUI
from tkinter import *

#Import filename
from tkinter import filedialog

#Import filename
from tkinter import messagebox

###########################################
#CHOOSING FOLDERS (optional)

#Finds folder location
cwd = os.getcwd()

#saves root cwd
rootcwd=cwd

#Goes to script folder
os.chdir(cwd+'/superscripts')

#Finds folder location
currentdir = os.getcwd()



###########################################
#SCRIPTS

def Autofill():
    os.system("Autofill.py")

def Autofix():
    os.system("Autofix.py")

def Checkrot():
    os.system("Checkrot.py")

def Excitedstatefix():
    os.system("Excitedstatefix.py")

def Fetchdata():
    os.system("Fetch_data.py")

def Fetchfreq():
    os.system("Fetch_freq.py")

def PDCbatchfixer():
    os.system("PDCbatchfixer.py")

def Tempfiller():
    os.system("Tempfiller.py")

def Totalcputime():
    os.system("Totalcputime.py")

###########################################
#INFO SCRIPTS

def create_window():
    window = Toplevel(root)

def Autofillinfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program fixes and fills the .com files '
             'already found in the folders')
    title='Autofillinfo'
    messagebox.showinfo(title, message)

def Autofixinfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program creates .com files from .xyz files.\n '
             'WARNING: This overwrites what Autofill does '
             '(but can be used to reset everything) ')
    title='Autofixinfo'
    messagebox.showinfo(title, message)

def Checkrotinfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program checks .zmat files if the angle '
             'has been correctly done.\n '
             'Old code: Not good for irregular .zmat files ')
    title='Checkrotinfo'
    messagebox.showinfo(title, message)

def Excitedstatefixinfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program creates .com files '
             'but only for excited state calculations')
    title='Excitedstatefixinfo'
    messagebox.showinfo(title, message)

def Fetchdatainfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program fetches the data from the .log files '
             'and creates a .csv file where the data is stored '
             'which can be found in superscripts/data folder.\n '
             'If excitedstate files are found (from Excitedstatefix), '
             'the values from the those files are used instead. ')
    title='Fetchdatainfo'
    messagebox.showinfo(title, message)

def Fetchfreqinfo():
    message=('Select .log file (EX: L0tail.log) from Laurdan or HPC-Azo.\n '
             'This program fetches the data from the .log files '
             'that has been run with Freq calculations.\n '
             'The data are stored in a .csv file '
             'which can be found in superscripts/data folder ')
    title='Fetchfreq'
    messagebox.showinfo(title, message)

def PDCbatchfixerinfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program creates sbatch files (.sh) '
             'that can be used to run on PDCs computers. ')
    title='PDCbatchfixer'
    messagebox.showinfo(title, message)

def Tempfillerinfo():
    message=('Input the name of the file.\n '
             'This program will create a .com file which can be used '
             'to run the freq calculations with temperatures '
             'ranging from 1 to 480 K.\n '
             'The .com files require .chk files to run. ')
    title='Tempfillerinfo'
    messagebox.showinfo(title, message)

def Totalcputimeinfo():
    message=('Select folder (EX: B3LYP) from Laurdan or HPC-Azo.\n '
             'This program will sum up the total core hours that '
             'was used to run the calculations.\n '
             'The data is saved in a .csv file '
             'which can be found in superscripts/data folder.\n '
             'Old code: Not updated for long ')
    title='Totalcputimeinfo'
    messagebox.showinfo(title, message)


###########################################
#GUI

#Main window
root = Tk()

#Frame
f = Frame(root, height=230, width=350)
f.grid_propagate(0) # don't shrink

#Makes it a grid
f.grid()

#Gridsettings
Grid.rowconfigure(root, 0, weight=2)
Grid.columnconfigure(root, 0, weight=2)

h=3
w=12
#Buttons
b1 = Button(f, height=h, width=w, text='Autofill', command=Autofill)
b2 = Button(f, height=h, width=w, text='Autofix', command=Autofix)
b3 = Button(f, height=h, width=w, text='Checkrot', command=Checkrot)
b4 = Button(f, height=h, width=w, text='Excitedstatefix', command=Excitedstatefix)
b5 = Button(f, height=h, width=w, text='Fetchdata', command=Fetchdata)
b6 = Button(f, height=h, width=w, text='Fetchfreq', command=Fetchdata)
b7 = Button(f, height=h, width=w, text='PDCbatchfixer', command=PDCbatchfixer)
b8 = Button(f, height=h, width=w, text='Tempfiller', command=Tempfiller)
b9 = Button(f, height=h, width=w, text='Totalcputime', command=Totalcputime)

h=1
w=1
#Info buttons
b1info= Button(f, height=h, width=w, text='i', background='red', command=Autofillinfo)
b2info= Button(f, height=h, width=w, text='i', background='red', command=Autofixinfo)
b3info= Button(f, height=h, width=w, text='i', background='red', command=Checkrotinfo)
b4info= Button(f, height=h, width=w, text='i', background='red', command=Excitedstatefixinfo)
b5info= Button(f, height=h, width=w, text='i', background='red', command=Fetchdatainfo)
b6info= Button(f, height=h, width=w, text='i', background='red', command=Fetchfreqinfo)
b7info= Button(f, height=h, width=w, text='i', background='red', command=PDCbatchfixerinfo)
b8info= Button(f, height=h, width=w, text='i', background='red', command=Tempfillerinfo)
b9info= Button(f, height=h, width=w, text='i', background='red', command=Totalcputimeinfo)

#Fixing buttons
b1.grid(row=0,column=0, padx=10, pady=10)
b2.grid(row=0,column=1, padx=10, pady=10)
b3.grid(row=0,column=2, padx=10, pady=10)
b4.grid(row=1,column=0, padx=10, pady=10)
b5.grid(row=1,column=1, padx=10, pady=10)
b6.grid(row=1,column=2, padx=10, pady=10)
b7.grid(row=2,column=0, padx=10, pady=10)
b8.grid(row=2,column=1, padx=10, pady=10)
b9.grid(row=2,column=2, padx=10, pady=10)

#Fixing infobuttons
b1info.place(x=102, y=50, anchor=SW)
b2info.place(x=217, y=50, anchor=SW)
b3info.place(x=330, y=50, anchor=SW)
b4info.place(x=102, y=125, anchor=SW)
b5info.place(x=217, y=125, anchor=SW)
b6info.place(x=330, y=125, anchor=SW)
b7info.place(x=102, y=200, anchor=SW)
b8info.place(x=217, y=200, anchor=SW)
b9info.place(x=330, y=200, anchor=SW)

#Keeps window
root.mainloop()
