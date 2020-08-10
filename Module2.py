from tkinter import *
import datetime
import random
from operator import itemgetter

root=Tk()
root.title('Report')
root.geometry('270x200')

Label(root, width=500, height=500, background='LightSkyBlue1').place(x=1,y=1)
Label(root, relief='solid', borderwidth=2, width=35, height=6, background='Alice Blue').place(x=2,y=2)
Label(root, relief='solid', borderwidth=2, width=35, height=5, background='Alice Blue').place(x=2,y=100)

Label(root,text='Passenger Name', background='Alice Blue').place(x=4,y=5)
entry_main1=Entry(root,width=20)
entry_main1.place(x=100,y=5)

Label(root, text='Flight Number', background='Alice Blue').place(x=4,y=102)
entry_main2=Entry(root,width=20)
entry_main2.place(x=100,y=103)

Label(root, text='Aircraft', background='Alice Blue').place(x=4,y=125)
entry_main3=Entry(root,width=20)
entry_main3.place(x=100,y=125)


def Slip(a):
	Passenger_Name=str(entry_main1.get())
	Passenger_Name=Passenger_Name.upper()
	if Passenger_Name=='':
		print('\a')
		boot=Tk()
		boot.title('Error')
		Label(boot,text='No Data Input').pack()
		boot.geometry('200x20')
		boot.mainloop()
	else:
		curdate=datetime.datetime.now()
		name='P'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'
		found=0
		fout1=open(name)
		for data in fout1:
			a=data.split('{')
			if Passenger_Name==a[5]:
				found=1
				main_array=data.split('{')
				fout2=open('Aircraft.txt')
				for data in fout2:
					arr2=data.split(",")
					if main_array[0]==arr2[0]:
						aircraft=arr2[1]
				curdate=datetime.datetime.now()

				soot=Tk()
				soot.title('Reservation Slip')
				soot.geometry('550x200')
				Label(soot, relief='solid', borderwidth=2, width=75, height=12).place(x=2,y=2)
				Label(soot, text='-'*103).place(x=6,y=18)
				Label(soot, text='-'*103).place(x=6,y=160)
				Label(soot, text='Reservation Slip').place(x=6,y=6)

				Label(soot,text='PNR Number').place(x=6,y=40)
				Label(soot,text=':   {}'.format(main_array[1])).place(x=100,y=40)

				Label(soot,text='Status').place(x=6,y=60)
				Label(soot,text=':   {}'.format(main_array[11])).place(x=100,y=60)

				Label(soot,text='Seat Number').place(x=6,y=80)
				Label(soot,text=':   {}'.format(main_array[2])).place(x=100,y=80)

				Label(soot,text='From').place(x=6,y=100)
				Label(soot,text=':   {}'.format(main_array[3])).place(x=100,y=100)

				Label(soot,text='Name').place(x=6,y=120)
				Label(soot,text=':   {}'.format(main_array[5])).place(x=100,y=120)

				Label(soot,text='Contact No').place(x=6,y=140)
				Label(soot,text=':   {}'.format(main_array[9])).place(x=100,y=140)

				Label(soot, text='Flight Number').place(x=250,y=40)
				Label(soot,text=':   {}'.format(main_array[0])).place(x=350,y=40)

				Label(soot, text='Aircraft').place(x=250,y=60)
				Label(soot,text=':   {}'.format(aircraft)).place(x=350,y=60)

				Label(soot, text='Date Of Journey').place(x=250,y=80)
				Label(soot,text=':   {}'.format(str(curdate.day)+'/'+str(curdate.month)+'/'+str(curdate.year))).place(x=350,y=80)

				Label(soot, text='To').place(x=250,y=100)
				Label(soot,text=':   {}'.format(main_array[4])).place(x=350,y=100)

				Label(soot, text='Age').place(x=250,y=120)
				Label(soot,text=':   {}'.format(main_array[8])).place(x=350,y=120)

				Label(soot, text='Fare').place(x=250,y=140)
				Label(soot,text=':   {}'.format(main_array[10])).place(x=350,y=140)

				soot.mainloop()

				fout2.close()
		fout1.close()
		
		if found != 1:
			print('\a')
			boot=Tk()
			boot.title('Error')
			Label(boot,text="Booking Does Not Exist").pack()
			boot.geometry('200x20')
			boot.mainloop()

def Ticket(a):
	Passenger_Name=str(entry_main1.get())
	Passenger_Name=Passenger_Name.upper()
	if Passenger_Name=='':
		print('\a')
		boot=Tk()
		boot.title('Error')
		Label(boot,text='No Data Input').pack()
		boot.geometry('200x20')
		boot.mainloop()
	else:
		curdate=datetime.datetime.now()
		name='P'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'
		found=0
		fout1=open(name)
		for data in fout1:
			a=data.split('{')
			if Passenger_Name==a[5]:
				found=1
				main_array=data.split('{')
				
				curdate=datetime.datetime.now()

				soot=Tk()
				soot.title('Passenger Ticket')
				soot.geometry('550x200')
				Label(soot, relief='solid', borderwidth=2, width=75, height=12).place(x=2,y=2)
				Label(soot, text='-'*103).place(x=6,y=18)
				Label(soot, text='-'*103).place(x=6,y=160)
				Label(soot, text='Passenger Ticket').place(x=6,y=6)

				Label(soot,text='Ticket Number').place(x=6,y=40)
				Label(soot,text=':   {}'.format(random.randint(1000,5000))).place(x=100,y=40)

				Label(soot,text='From').place(x=6,y=60)
				Label(soot,text=':   {}'.format(main_array[3])).place(x=100,y=60)

				Label(soot,text='Name').place(x=6,y=80)
				Label(soot,text=':   {}'.format(main_array[5])).place(x=100,y=80)

				Label(soot, text='Date of Issue').place(x=250,y=40)
				Label(soot,text=':   {}'.format(str(curdate.day)+'/'+str(curdate.month)+'/'+str(curdate.year))).place(x=350,y=40)

				Label(soot, text='To').place(x=250,y=60)
				Label(soot,text=':   {}'.format(main_array[4])).place(x=350,y=60)

				Label(soot, text='Fare').place(x=250,y=80)
				Label(soot,text=':   {}'.format(main_array[10])).place(x=350,y=80)

				soot.mainloop()

		fout1.close()

		if found != 1:
			print('\a')
			boot=Tk()
			boot.title('Error')
			Label(boot,text="Booking Does Not Exist").pack()
			boot.geometry('200x20')
			boot.mainloop()


def Chart(A):
	Flight_No=str(entry_main2.get())
	Flight_No=Flight_No.upper()
	Aircraft_Name=str(entry_main3.get())
	Aircraft_Name=Aircraft_Name.upper()
	if Flight_No=='' or Aircraft_Name=='':
		print('\a')
		boot=Tk()
		boot.title('Error')
		Label(boot,text='No Data Input').pack()
		boot.geometry('200x20')
		boot.mainloop()

	else:
		curdate=datetime.datetime.now()
		name='P'+str(curdate.day)+str(curdate.month)+str(curdate.year)+'.txt'
		fout1=open(name)
		temp_array=[]
		c=0
		found=0
		for data in fout1:
			data=data.strip()
			a=data.split('{')
			if Flight_No==a[0]:
				found=1
				c+=1
				main_array=data.split('{')
				temp_array.append(main_array)

		if found==1:
			fout2=open('Aircraft.txt')
			for data in fout2:
				arr=data.split(',')
				if Flight_No==arr[0]:
					time=arr[5]
			fout2.close()
			curdate=datetime.datetime.now()
			
			soot=Tk()
			soot.title('Reservation Chart')
			soot.geometry('500x500')


			Label(soot, text='Flight Number').place(x=5,y=5)
			Label(soot,text=':   {}'.format(Flight_No)).place(x=105,y=5)

			Label(soot, text='Aircraft').place(x=5,y=30)
			Label(soot,text=':   {}'.format(Aircraft_Name)).place(x=105,y=30)

			Label(soot, text='Date Of Journey').place(x=250,y=5)
			Label(soot,text=':   {}'.format(str(curdate.day)+'/'+str(curdate.month)+'/'+str(curdate.year))).place(x=350,y=5)

			Label(soot, text='Departure Time').place(x=250,y=30)
			Label(soot,text=':   {}'.format(time)).place(x=350,y=30)

			'''
			fout=open('P9112019.txt')
			arr=[]
			c=0
			for data in fout:
				c+=1
				data=data.strip()
				a=data.split('{')
				arr.append(a)
			'''
			temp_array.sort(key=itemgetter(2))

			Label(soot, text='-'*103).place(x=5,y=65)
			Label(soot,relief='solid', borderwidth='2',width=65, height=2).place(x=2,y=83)
			Label(soot,text='Seat No').place(x=5,y=90)
			Label(soot,text='Name').place(x=75,y=90)
			Label(soot,text='Age').place(x=190,y=90)
			Label(soot,text='Destination').place(x=240,y=90)
			Label(soot,text='PNR').place(x=340,y=90)
			Label(soot,text='Status').place(x=410,y=90)

			for x in range(c):
				y_value=125
				for k in temp_array:
					Label(soot,text='{}'.format(k[2])).place(x=5,y=y_value)
					Label(soot,text='{}'.format(k[5])).place(x=75,y=y_value)
					Label(soot,text='{}'.format(k[6])).place(x=190,y=y_value)
					Label(soot,text='{}'.format(k[4])).place(x=240,y=y_value)
					Label(soot,text='{}'.format(k[1])).place(x=340,y=y_value)
					Label(soot,text='{}'.format(k[11])).place(x=410,y=y_value)
					y_value+=20

			soot.mainloop()

Reservation_Slip=Button(root,text='Reservation Slip',width=30)
Reservation_Slip.bind('<Button-1>',Slip)
Reservation_Slip.place(x=6,y=30)

Passenger_Ticket=Button(root,text='Passenger Ticket',width=30)
Passenger_Ticket.bind('<Button-1>',Ticket)
Passenger_Ticket.place(x=6,y=62)

Reservation_Chart=Button(root,text='Reservation Chart',width=30)
Reservation_Chart.bind('<Button-1>',Chart)
Reservation_Chart.place(x=6,y=150)


root.mainloop()
