import datetime
from random import randint
import os
from tkinter import *
import datetime

root=Tk()
root.title('Main Menu')

a=IntVar()
b=IntVar()

curdate=datetime.datetime.now()
temp_name='F'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'

def aircraft(a):
    os.system('python Module1.py')

def report(a):
    os.system('python Module2.py')

def create(a):
    curdate=datetime.datetime.now()
    name='P'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'
    #temp_name='F'+name[1:]
    fin=open(name,'a')
    fout=open('Aircraft.txt')
    flno=str(ent1.get())
    c=0
    for data in fout:
        arr=data.split(',')
        if flno==arr[0]:
            valplace=arr[3]
            c=1
    if c==0:
        print('\a')
        boot=Tk()
        boot.title('Error')
        Label(boot,text='Flight Does Not Exist').pack()
        boot.geometry('200x20')
        boot.mainloop()
    pnr=str(ent2.get())
    depart=str(ent3.get())
    arrival=str(ent4.get())
    if arrival.lower()!=valplace.lower():
        print('\a')
        loot=Tk()
        loot.title('Error')
        Label(loot,text='Invalid Destination Place').pack()
        loot.geometry('200x20')
        loot.mainloop()
    pas=str(ent5.get())
    age=str(ent6.get())
    if int(age)<0:
        print('\a')
        koot=Tk()
        koot.title('Error')
        Label(koot,text='Invalid Age').pack()
        koot.geometry('200x20')
        koot.mainloop()
    else:
        actage=age
    address=str(ent7.get())
    phone=str(ent8.get())
    amount=str(ent9.get())
    Fout=open(temp_name,'a')
    if a=='PY_VAR1':
        sex='Male'
    else:
        sex='Female'
    if b=='PY_VAR1':
        st='W'
    else:
        st='C'
    #Fout=open('Flight.txt')
    Fout=open(temp_name)
    temp=open('Temp.txt','a')
    d=0
    for data in Fout:
        data=data.strip()
        arr=data.split(',')
        print(arr)
        if flno!=arr[0]:
            temp.write(arr[0]+','+arr[1]+'\n')
        else:
            seat=int(arr[1])+1
            d=1
            temp.write(arr[0]+','+str(seat)+'\n')
    Fout.close()
    temp.close()
    os.remove(temp_name)
    os.rename('temp.txt',temp_name)

    if d==0:
        print('\a')
        soot=Tk()
        soot.title('Error')
        Label(soot,text='Flight Fill').pack()
        soot.geometry('200x20')
        soot.mainloop()

    try:
        fin.write(flno+'{'+pnr+'{'+str(seat)+'{'+depart+'{'+arrival+'{'+pas+'{'+actage+'{'+sex+'{'+address+'{'+phone+'{'+amount+'{'+st+'\n')
    except:
        print('\a')
        moot=Tk()
        moot.title('Error')
        Label(moot,text='Invalid Data Input').pack()
        moot.geometry('200x20')
        moot.mainloop()

    fin.close()
    fout.close()
    #Label(root,text='Saved').grid(row=19,column=0,sticky=E)

def check(A):
    fout=open(temp_name)
    Fout=open('Aircraft.txt')
    name=str(ent10.get())
    for data in Fout:
        arr=data.split(',')
        if name==arr[0]:
            Max=arr[2]
    for data in fout:
        arr=data.split(',')
        if name==arr[0]:
            total=str(int(Max)-int(arr[1]))
            Label(root,text=total,background='White').place(x=240,y=477)
    fout.close()
    Fout.close()

def show(c):
    curdate=datetime.datetime.now()
    file='P'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'
    fin=open(file)
    Label(root,text='FL No',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=5,padx=(20,0))
    Label(root,text='Pnr',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=6)
    Label(root,text='Seat',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=7)
    Label(root,text='Depart',borderwidth=2,relief='groove',width=11,background='PaleGreen1').grid(row=7,column=8)
    Label(root,text='Arrive',borderwidth=2,relief='groove',width=11,background='PaleGreen1').grid(row=7,column=9)
    Label(root,text='Name',borderwidth=2,relief='groove',width=11,background='PaleGreen1').grid(row=7,column=10)
    Label(root,text='Age',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=11)
    Label(root,text='Sex',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=12)
    Label(root,text='Address',borderwidth=2,relief='groove',width=15,background='PaleGreen1').grid(row=7,column=13)
    Label(root,text='Phone',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=14)
    Label(root,text='Amount',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=15)
    Label(root,text='ST',borderwidth=2,relief='groove',width=9,background='PaleGreen1').grid(row=7,column=16)
    c=0
    for data in fin:
        c+=1
    fin.close()
    fin=open(file)
    infotot=[]
    for data in fin:
        data=data.strip()
        info=data.split('{')
        infotot.append(info)
    for x in range(0,c):
        for i in range(0,12):
            if i==0:
                Label(root,text=infotot[x][i],borderwidth=1,relief='solid',width=9,background='DarkSeaGreen1').grid(row=8+x,column=5+i,padx=(20,0))
            elif i==8:
                Label(root,text=infotot[x][i],borderwidth=1,relief='solid',width=15,background='DarkSeaGreen1').grid(row=8+x,column=5+i)
            elif i in [3,4,5]:
                Label(root,text=infotot[x][i],borderwidth=1,relief='solid',width=11,background='DarkSeaGreen1').grid(row=8+x,column=5+i)
            else:
                Label(root,text=infotot[x][i],borderwidth=1,relief='solid',width=9,background='DarkSeaGreen1').grid(row=8+x,column=5+i)

    fin.close()
    #boot.mainloop()


Label(root,background='Dodger Blue',height=40,width=40).place(x=0,y=0)
Label(root,background='LightSkyBlue1',height=40,width=1000).place(x=285,y=0)
Label(root,relief='solid',borderwidth=2,width=20,background='Alice Blue',height=6).place(x=1,y=2)
Label(root, text='Options', relief='solid', borderwidth=2, width=18,background='Lavender').grid(row=0, column=0,pady=5,padx=(8,6),columnspan=2,sticky=W)
airbut=Button(root,text='Aircraft',width=15,background='Lavender')
airbut.bind('<Button-1>', aircraft)
airbut.grid(row=1, column=0, padx=16,columnspan=2,sticky=W)
airrep=Button(root,text='Report',width=15,background='Lavender')
airrep.bind('<Button-1>',report)
airrep.grid(row=2, column=0, padx=16,pady=3,columnspan=2,sticky=W)
Label(root,relief='solid',borderwidth=2,background='Alice Blue',width=38,height=20).place(x=1,y=130)
Label(root,text='Passenger Details Entry',background='Lavender',relief='solid',borderwidth=2,width=38).grid(row=6,column=0,pady=18,columnspan=2,padx=(1,0))
Label(root,text='Flight No.',background='Alice Blue').grid(row=7,column=0)
ent1=Entry(root)
ent1.grid(row=7,column=1,columnspan=1,sticky=W)
Label(root,text='PNR',background='Alice Blue').grid(row=8,column=0)
ent2=Entry(root)
ent2.grid(row=8,column=1,sticky=W)
Label(root,text='Depature',background='Alice Blue').grid(row=9,column=0)
ent3=Entry(root)
ent3.grid(row=9,column=1,sticky=W)
Label(root,text='Arrival',background='Alice Blue').grid(row=10,column=0)
ent4=Entry(root)
ent4.grid(row=10,column=1,sticky=W)
Label(root,text='Name',background='Alice Blue').grid(row=11,column=0)
ent5=Entry(root)
ent5.grid(row=11,column=1,sticky=W)
Label(root,text='Age',background='Alice Blue').grid(row=12,column=0)
ent6=Entry(root,width=3)
ent6.grid(row=12,column=1,sticky=W)
Radiobutton(root,text='Male',variable=a,value=1,background='Alice Blue').grid(row=13,column=0)
Radiobutton(root,text='Female',variable=a,value=2,background='Alice Blue').grid(row=13,column=1,sticky=W)
Label(root,text='Address',background='Alice Blue').grid(row=14,column=0)
ent7=Entry(root,width=30)
ent7.grid(row=14,column=1,sticky=W)
Label(root,text='Phone No.',background='Alice Blue').grid(row=15,column=0)
ent8=Entry(root)
ent8.grid(row=15,column=1,sticky=W)
Label(root,text='Amount',background='Alice Blue').grid(row=16,column=0)
ent9=Entry(root)
ent9.grid(row=16,column=1,sticky=W)
Radiobutton(root,text='W',variable=b,value=1,background='Alice Blue').grid(row=17,column=0)
Radiobutton(root,text='C',variable=b,value=2,background='Alice Blue').grid(row=17,column=1,sticky=W)
sub1=Button(root,text='Submit',width=15,background='Lavender')
sub1.bind('<Button-1>',create)
sub1.grid(row=18,column=1,padx=40,sticky=E)
Label(root,relief='solid',borderwidth=2,width=38,height=3,background='Alice Blue').place(x=1,y=468)
Label(root,text='Seats Availabilty',relief='solid',borderwidth=2,width=38,background='Lavender').place(x=1,y=445)
Label(root,text='Flight No.',background='Alice Blue').grid(row=20,column=0,pady=65)
ent10=Entry(root,width=12)
ent10.grid(row=20,column=1,sticky=W)
sub2=Button(root,text='Submit',background='Lavender')
sub2.bind('<Button-1>',check)
sub2.place(x=165,y=475)
sub3=Button(root,text='Show',width=13,background='Lavender')
sub3.bind('<Button-1>',show)
sub3.place(x=25,y=385)



root.geometry('1200x1000')
root.mainloop()