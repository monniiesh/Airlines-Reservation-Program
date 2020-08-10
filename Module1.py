#Aircraft
from os import rename,remove,path
#import keyboard
from tkinter import *
from time import sleep
import datetime

root=Tk()

def enter():
    
    global flno,name,capacity,splace,dplace,h1,m1,h2,m2,dtime,atime,texpense,fout
    fout=open('Aircraft.txt','a')
    

    fout=open('Aircraft.txt','a')
    flno=str(ent1.get())
    name=str(ent2.get())
    capacity=int(ent10.get())
    splace=str(ent3.get())
    dplace=str(ent4.get())
    try:
        h1=int(ent5x.get())
    except:
        error=Tk()
        error.title('Error')
        Label(error,text='Time Error').pack()
        print('\a')
        error.mainloop()
    finally:
        h1=int(ent5x.get())
        h1x=str(ent5x.get())

    try:
        m1=int(ent5y.get())
    except:
        error=Tk()
        error.title('Error')
        Label(error,text='Time Error').pack()
        print('\a')
        error.mainloop()
    finally:
        m1=int(ent5y.get())
        m1x=str(ent5y.get())
    
    dtime=str(h1x)+':'+str(m1x)

    try:
        h2=int(ent6x.get())
    except:
        error=Tk()
        error.title('Error')
        Label(error,text='Time Error').pack()
        print('\a')
        error.mainloop()
    finally:
        h2=int(ent6x.get())
        h2x=str(ent6x.get())

    try:
        m2=int(ent6y.get())
    except:
        error=Tk()
        error.title('Error')
        Label(error,text='Time Error').pack()
        print('\a')
        error.mainloop()
    finally:
        m2=int(ent6y.get())
        m2x=str(ent6y.get())

    atime=str(h2x)+':'+str(m2x)
    texpense=int(ent9.get())

def add(t):
    enter()
    c=0
    if h1>=24 or h1<0 or h2>=24 or h2<0 or m1>=60 or m1<0 or m2>=60 or m2<0:
        c=1
    else:
        c=0
        
    if c==1:
        error=Tk()
        error.title('Error')
        Label(error,text='Time Error').pack()
        print('\a')
        error.mainloop()
    else:
        fout.write(flno+','+name+','+str(capacity)+','+splace+','+dplace+','+dtime+','+atime+','+str(texpense)+'\n')
        fout.close()
        Sort()
        sleep(10)

    curdate=datetime.datetime.now()
    Flight_file='F'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'
    Fout=open(Flight_file,'a')
    Fout.write(flno + ',' + '0' +'\n')
    Fout.close()

                

def show(c):
    fin=open('Aircraft.txt')
    boot=Tk()
    boot.title('Preview')
    Label(boot,text='FL No',borderwidth=2,relief='groove',width=18).grid(row=0,column=0)
    Label(boot,text='Aircraft',borderwidth=2,relief='groove',width=18).grid(row=0,column=1)
    Label(boot,text='Capacity',borderwidth=2,relief='groove',width=18).grid(row=0,column=2)
    Label(boot,text='Splace',borderwidth=2,relief='groove',width=18).grid(row=0,column=3)
    Label(boot,text='Dplace',borderwidth=2,relief='groove',width=18).grid(row=0,column=4)
    Label(boot,text='Dtime',borderwidth=2,relief='groove',width=18).grid(row=0,column=5)
    Label(boot,text='Atime',borderwidth=2,relief='groove',width=18).grid(row=0,column=6)
    Label(boot,text='Texpense',borderwidth=2,relief='groove',width=18).grid(row=0,column=7)
    c=0
    for data in fin:
        c+=1
    fin.close()
    fin=open('Aircraft.txt')
    infotot=[]
    for data in fin:
        data=data.strip()
        info=data.split(',')
        infotot.append(info)
    for x in range(0,c):
        for i in range(8):
            Label(boot,text=infotot[x][i],borderwidth=1,relief='solid',width=18).grid(row=x+1,column=i)
    fin.close()
    boot.mainloop()
                

def Sort():
        fin=open('Aircraft.txt')
        infotot=[]
        for data in fin:
                info=data.split(',')
                infotot.append(info)
        infotot.sort()
        fin.close()
        Temp=open('temp.txt','a')
        for data in infotot:
            Temp.write(','.join(data))
        Temp.close()
        remove('Aircraft.txt')
        rename('Temp.txt','Aircraft.txt')
                


root.title('Aircraft')

Label(root, width=500, height=500, background='LightSkyBlue1').place(x=1,y=1)

lab1=Label(root,text='FlNo', background='LightSkyBlue1')
lab1.grid(row=0,column=0,sticky=W)
ent1=Entry(root)
ent1.grid(row=0,column=1,sticky=W)

lab2=Label(root,text='Aircraft', background='LightSkyBlue1')
lab2.grid(row=1,column=0,sticky=W)
ent2=Entry(root)
ent2.grid(row=1,column=1,sticky=W)

lab10=Label(root,text='Capacity', background='LightSkyBlue1')
lab10.grid(row=2,column=0,sticky=W)
ent10=Entry(root)
ent10.grid(row=2,column=1,sticky=W)

lab3=Label(root,text='Dplace', background='LightSkyBlue1')
lab3.grid(row=3,column=0,sticky=W)
ent3=Entry(root)
ent3.grid(row=3,column=1,sticky=W)

lab4=Label(root,text='Splace', background='LightSkyBlue1')
lab4.grid(row=4,column=0,sticky=W)
ent4=Entry(root)
ent4.grid(row=4,column=1,sticky=W)

lab5=Label(root,text='Dtime', background='LightSkyBlue1')
lab5.grid(row=0,column=5,sticky=W)
ent5x=Entry(root,width=2)
ent5x.grid(row=0,column=6,sticky=W)
Label(root,text=':', background='LightSkyBlue1').grid(row=0,column=7,sticky=W)
ent5y=Entry(root,width=2)
ent5y.grid(row=0,column=8,sticky=W)

lab6=Label(root,text='Stime', background='LightSkyBlue1')
lab6.grid(row=2,column=5,sticky=W)
ent6x=Entry(root,width=2)
ent6x.grid(row=2,column=6,sticky=W)
Label(root,text=':', background='LightSkyBlue1').grid(row=2,column=7,sticky=W)
ent6y=Entry(root,width=2)
ent6y.grid(row=2,column=8,sticky=W)

lab9=Label(root,text='Texpense', background='LightSkyBlue1')
lab9.grid(row=7,column=0,sticky=W)
ent9=Entry(root)
ent9.grid(row=7,column=1,sticky=W)

sub=Button(root,text='Submit')
sub.bind('<Button-1>',add)
sub.grid(sticky=W,row=9,column=0)

showbutton=Button(root,text='Preview')
showbutton.bind('<Button-1>',show)
showbutton.grid(sticky=W,row=9,column=1)

'''
status=Label(root,text='')
status.grid(column=5,row=7)
'''

root.geometry('300x200')

root.mainloop()






        

