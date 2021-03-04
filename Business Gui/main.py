from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from datetime import datetime
import os
#-------------------------------------------------------------Total Function-------------------------------------------


def total():
    try:
        Total = (int(Ricevar.get()) + int(Chickenvar.get()) + int(Curdvar.get()) + int(Oilvar.get()) + int(
            Onionvar.get())+ int(Gheevar.get()) + int(Masalavar.get()) + int(Khademasalevar.get()) + int(Gasvar.get()) +int(Petrolvar.get()) + int(Othervar.get()))
        Totalvar.set(Total)
        Expensesvar.set(Total)
    except Exception as e:
        msg.showerror("Not Get","Values Not Get Please Re-Enter the values")


def clear():
    Ricevar.set("")
    Chickenvar.set("")
    Curdvar.set("")
    Oilvar.set("")
    Onionvar.set("")
    Gheevar.set("")
    Masalavar.set("")
    Khademasalevar.set("")
    Gasvar.set("")
    Petrolvar.set("")
    Chicksale.set("")
    Korsales.set("")
    Setchickenvar.set("")
    Setkormavar.set("")
    Othervar.set("")
    Totalvar.set("")
    Salesvar.set("")
    Expensesvar.set("")
    Profitvar.set("")


def Set():
    total_Sales=float(Chicksale.get()) * int(Setchickenvar.get()) + float(Korsales.get()) * int(Setkormavar.get())
    Total_Expense = (int(Ricevar.get()) + int(Chickenvar.get()) + int(Curdvar.get()) + int(Oilvar.get()) + int(Onionvar.get()) + int(Gheevar.get()) + int(Masalavar.get()) + int(Khademasalevar.get()) + int(Gasvar.get()) + int(Petrolvar.get()) + int(Othervar.get()))
    Salesvar.set(total_Sales)
    Profitvar.set(total_Sales-Total_Expense)

def Record():
    Total_Expenses = (int(Ricevar.get()) + int(Chickenvar.get()) + int(Curdvar.get()) + int(Oilvar.get()) + int(Onionvar.get()) + int(Gheevar.get()) + int(Masalavar.get()) + int(Khademasalevar.get()) + int(Gasvar.get()) + int(Petrolvar.get()) + int(Othervar.get()))
    total_Sale = float(Chicksale.get()) * int(Setchickenvar.get()) + float(Korsales.get()) * int(Setkormavar.get())
    with open ("Record.txt",'a+') as f:
        f.write(f"{datetime.now()}    {Total_Expenses}    {Chicksale.get()}    { Korsales.get()}    {total_Sale}\n")
        read_file=f.readlines()
        l45.delete(*l45.get_children())
        for i in read_file:
            l45.insert("",END,values=i)


def showall():
    with open('Record.txt','r') as f:
        read_lines=f.readlines()
        l45.delete(*l45.get_children())
        for i in read_lines:
            l45.insert("", END, values=i)




def Printout():
    file_path='Record.txt'
    os.startfile(file_path,'print')
#-------------------------------------------------------------Basic structure-------------------------------------------

root=Tk()
root.geometry("1366x768")
root.minsize(1366,768)
root.title("Accounts")

#--------------------------------------------------------------Frames---------------------------------------------------

f1=Frame(root,bg='red',border=10,relief=SUNKEN)
f1.pack(side='top',fill=X)

f2=Frame(root,bg="grey",border=10,width=10,relief=SUNKEN)
f2.place(x=10,y=90,width=400,height=590)

f3=Frame(root,bg="grey",border=10,width=10,relief=SUNKEN)
f3.place(x=450,y=90,width=420,height=590)

f4=Frame(root,border=10)
f4.place(x=900,y=90,width=450,height=340)

f6=Frame(root,bg="grey",border=10,width=10,relief=SUNKEN)
f6.place(x=890,y=490,width=450,height=150)









#------------------------------------------------------------Labels of root-----------------------------------------------------

l1=Label(f1,text="Welcome to Raw Accounts",bg="red",font="comicasansms 30 bold").pack()

#----------------------------------------------------------Expenses Area Labels------------------------------------------------
l2=Label(f2,text="Expenses",font="comicasansms 20 bold",border=10,relief=GROOVE,bg='grey').place(x=35)

l3=Label(f2,text="Rice",font="comicasansms 15 bold",bg="grey").place(x=15,y=70)
l4=Label(f2,text="Chicken",font="comicasansms 15 bold",bg="grey").place(x=15,y=110)
l5=Label(f2,text="Curd",font="comicasansms 15 bold",bg="grey").place(x=15,y=150)
l6=Label(f2,text="Oil",font="comicasansms 15 bold",bg="grey").place(x=15,y=190)
l7=Label(f2,text="Onion",font="comicasansms 15 bold",bg="grey").place(x=15,y=230)
l8=Label(f2,text="Ghee",font="comicasansms 15 bold",bg="grey").place(x=15,y=270)
l9=Label(f2,text="Masala",font="comicasansms 15 bold",bg="grey").place(x=15,y=310)
l10=Label(f2,text="Khade Masale",font="comicasansms 15 bold",bg="grey").place(x=15,y=350)
l11=Label(f2,text="Gas",font="comicasansms 15 bold",bg="grey").place(x=15,y=390)
l12=Label(f2,text="Petrol",font="comicasansms 15 bold",bg="grey").place(x=15,y=430)
l35=Label(f2,text="Other Exp",font="comicasansms 15 bold",bg="grey").place(x=15,y=470)
l36=Label(f2,text="Total",font="comicasansms 15 bold",bg="grey").place(x=15,y=510)



#---------------------------------------------------------------Buttons-------------------------------------------------

B1=Button(f2,text="Total",font="comicasansms 10 bold",bg="grey",command=total,activebackground="grey").place(x=120,y=540)


#-----------------------------------------------------------Label after expenses  Entry Widget------------------------------------
l13=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=75)
l14=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=115)
l15=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=155)
l16=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=195)
l17=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=235)
l18=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=275)
l19=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=315)
l20=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=355)
l21=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=395)
l22=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=435)
l23=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=475)
l34=Label(f2,text="Rs",font="comicasansms 15 bold",bg="grey").place(x=280,y=515)


#----------------------------------------------------------All Expense Variables------------------------------------------------
Ricevar=StringVar()
Chickenvar=StringVar()
Curdvar=StringVar()
Oilvar=StringVar()
Onionvar=StringVar()
Gheevar=StringVar()
Masalavar=StringVar()
Khademasalevar=StringVar()
Gasvar=StringVar()
Petrolvar=StringVar()
Totalvar=StringVar()
Othervar=StringVar()


#-------------------------------------------------------------Entry Wighet----------------------------------------------
Rice_Entry=Entry(f2,textvariable=Ricevar).place(x=150,y=75)
Chicken_Entry=Entry(f2,textvariable=Chickenvar).place(x=150,y=115)
Curd_Entry=Entry(f2,textvariable=Curdvar).place(x=150,y=155)
Oil_Entry=Entry(f2,textvariable=Oilvar).place(x=150,y=195)
Onion_Entry=Entry(f2,textvariable=Onionvar).place(x=150,y=235)
Ghee_Entry=Entry(f2,textvariable=Gheevar).place(x=150,y=275)
Masala_Entry=Entry(f2,textvariable=Masalavar).place(x=150,y=315)
Khademasala_Entry=Entry(f2,textvariable=Khademasalevar).place(x=155,y=355)
Gas_Entry=Entry(f2,textvariable=Gasvar).place(x=150,y=395)
Petrol_Entry=Entry(f2,textvariable=Petrolvar).place(x=150,y=435)
Other_Entry=Entry(f2,textvariable=Othervar).place(x=150,y=475)
Total_Entry=Entry(f2,textvariable=Totalvar,state='readonly').place(x=150,y=515)




#-----------------------------------------------------------Sales Area-------------------------------------------------
l25=Label(f3,text="Sales",font="comicasansms 20 bold",border=10,relief=GROOVE,bg='grey').pack()

#------------------------------------------------------------Sales labes-----------------------------------------------
l26=Label(f3,text="Chicken",font="comicasansms 20 bold",bg="grey").place(x=10,y=90)
l27=Label(f3,text="Korma",font="comicasansms 20 bold",bg="grey").place(x=10,y=130)
l28=Label(f3,text="Kg",font="comicasansms 15 bold",bg="grey").place(x=290,y=90)
l29=Label(f3,text="Kg",font="comicasansms 15 bold",bg="grey").place(x=290,y=130)

#-------------------------------------------------------------Button in frame 3-----------------------------------------
b2=Button(f3,text="Submit",font="comicasansms 10 bold",bg="grey",activebackground="grey").place(x=150,y=170)
b3=Button(f3,text="Set",font="comicasansms 10 bold",bg="grey",command=Set,activebackground="grey").place(x=150,y=350,width=120)
b4=Button(f3,text="Record",font="comicasansms 10 bold",bg="grey",command=Record,activebackground="grey").place(x=150,y=540)

#-------------------------------------------------------------Sales area All variables----------------------------------
Chicksale=StringVar()
Korsales=StringVar()


#---------------------------------------------------------------Sales area Entry Widget---------------------------------
Chicksale_entry=Entry(f3,textvariable=Chicksale).place(x=150,y=95)
Korsale_entry=Entry(f3,textvariable=Korsales).place(x=150,y=135)

#----------------------------------------------------------------Net Area----------------------------------------------
l30=Label(f3,text="Amount",font="comicasansms 20 bold",border=10,relief=GROOVE,bg='grey').place(x=110,y=210)

#----------------------------------------------------------------Label for Net prfit-----------------------------------
l31=Label(f3,text="Chicken Biryani",font="comicasansms 20 bold",bg="grey").place(x=10,y=270)
l32=Label(f3,text="Korma",font="comicasansms 20 bold",bg="grey").place(x=10,y=310)
l37=Label(f3,text="Rs/Kg",font="comicasansms 10 bold",bg="grey").place(x=360,y=280)
l38=Label(f3,text="Rs/Kg",font="comicasansms 10 bold",bg="grey").place(x=360,y=320)
#-----------------------------------------------------------------All variables in Amount area--------------------------
Setchickenvar=StringVar()
Setkormavar=StringVar()


#-------------------------------------------------------------------Entry widget int amount area------------------------
Setchicken_Entry=Entry(f3,textvariable=Setchickenvar).place(x=230,y=280)
SetKorma_Entry=Entry(f3,textvariable=Setkormavar).place(x=230,y=320)


#----------------------------------------------------------------Sales Area--------------------------------------------
l39=Label(f3,text="Profit",font="comicasansms 15 bold",border=10,relief=GROOVE,bg='grey').place(x=150,y=390)



#--------------------------------------------------------------Label In sales Area--------------------------------------
l40=Label(f3,text="Sales",font="comicasansms 15 bold",bg="grey").place(x=10,y=450)
l41=Label(f3,text="Expenses",font="comicasansms 15 bold",bg="grey").place(x=10,y=480)
l42=Label(f3,text="Profit",font="comicasansms 15 bold",bg="grey").place(x=10,y=510)

#-----------------------------------------------------------------Variables in profit area------------------------------
Expensesvar=StringVar()
Salesvar=StringVar()
Profitvar=StringVar()
#---------------------------------------------------------------Entry widget in Profit area-----------------------------
Expense_Entry=Entry(f3,textvariable=Salesvar,state="readonly",font="comicasansms 10 bold").place(x=200,y=450)
Sales_Entry=Entry(f3,textvariable=Expensesvar,state="readonly",font="comicasansms 10 bold").place(x=200,y=480)
Profit_Entry=Entry(f3,textvariable=Profitvar,state="readonly",font="comicasansms 10 bold").place(x=200,y=510)

#-----------------------------------------------Scroll bars-------------------------------------------------------------
Scroll_x=Scrollbar(f4,orient=VERTICAL)
Scroll_y=Scrollbar(f4,orient=HORIZONTAL)

#------------------------------------------------Treeview--------------------------------------------------------------
l45=ttk.Treeview(f4,column=("Date","Time","Expenses","Chicken Weight","Korma Weight","Sales"))
Scroll_x.pack(side='bottom',fill=X)
Scroll_y.pack(side="right",fill=Y)
Scroll_x.config(command=l45.xview)
Scroll_y.config(command=l45.yview)
l45.heading("Date",text="Date")
l45.heading("Time",text="Time")
l45.heading("Expenses",text="Expense")
l45.heading("Chicken Weight",text="Chicken Weight")
l45.heading("Korma Weight",text="Korma Weight")
l45.heading("Sales",text="Sales")
l45['show']='headings'
l45.column("Date",width=100)
l45.column("Time",width=100)
l45.column("Expenses",width=80)
l45.column("Chicken Weight",width=100)
l45.column("Korma Weight",width=90)
l45.column("Sales",width=50)
l45.pack(fill=BOTH,expand=1)
l45.pack()


#--------------------------------------------------------------------Frame 6 all buttons-------------------------------
b5=Button(f6,text='Show All',font='comicasansms 10 bold',bg="grey",activebackground="grey",command=showall).place(x=10,y=60)
b6=Button(f6,text='Clear',font='comicasansms 10 bold',bg="grey",activebackground="grey",command=clear).place(x=110,y=60)
b7=Button(f6,text="Print Record",font='comicasansms 10 bold',bg="grey",activebackground="grey",command=Printout).place(x=180,y=60)
#--------------------------------------------------------------------------Label in frame 6----------------------------
l46=Label(f6,text='Control Pannel',font='comicasansms 10 bold',bg="grey",border=10,relief=GROOVE).pack()




root.mainloop()