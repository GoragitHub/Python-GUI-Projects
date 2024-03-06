from tkinter import *
# from tkinter.ttk import *
import random
import time
import sqlite3
# Connect to the database (or create a new one if it doesn't exist)
connection = sqlite3.connect("restaurant.db")
cursor = connection.cursor()

# Create a table for orders if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fries INTEGER,
        lunch_fries INTEGER,
        burger INTEGER,
        pizza INTEGER,
        cheese_burger INTEGER,
        drinks INTEGER,
        total_cost REAL,
        service_charge REAL,
        tax REAL,
        Total REAL
    )
''')
connection.commit()


root=Tk()
root.geometry("1600x980")
# root.resizable(0,0)
root.title("Resturent Manege System")
Tops=Frame(root,width=1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=700,relief=SUNKEN)
f2=Frame(root,width=400,height=700,relief=SUNKEN)

f1.pack(side=LEFT)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))
lblinfo=Label(Tops,font="aria 30 bold",text=" Dhrubo's Restaurent Management System",anchor="w",foreground="steel blue")
lblinfo.grid(row=0,column=0)
lblinfo=Label(Tops,font="aria 20",text=localtime,foreground="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)

text_input=StringVar()
operator=""

txtdisplay=Entry(f2,font=("ariel 20 bold"),textvariable=text_input,justify=RIGHT,bd=7,insertwidth=5)
txtdisplay.grid(columnspan=4)

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def clrdisplay():
    global operator    
    operator=""
    text_input.set(operator)

def equls():
    global operator
    sumup=str(eval(operator))

    text_input.set(sumup)
    operator=""

def total():
    x=random.randint(12980,50876)    
    randomRef=str(x)
    rand.set(randomRef)

    cof=float(Fries.get())
    colf=float(lunchfries.get())
    cob=float(Burger.get())
    cop=float(Pizza.get())
    coC_b=float(Cheese_burger.get())
    cod=float(Drinks.get())

    costofFries=cof*25
    costofLargefries=colf*40
    costofBurger=cob*35
    costofPizza=cop*50
    costofCheese_burger=coC_b*35
    costofDrinks=cod*35

    costofMeal=f"Rs.{str(costofFries+costofLargefries+costofBurger+costofPizza+costofCheese_burger+costofDrinks)}"
    PayTax=((costofFries+costofLargefries+costofBurger+costofPizza+costofCheese_burger+costofDrinks)*0.33)
    TotalCost=(costofFries+costofLargefries+costofBurger+costofPizza+costofCheese_burger+costofDrinks)
    Ser_Charge=((costofFries+costofLargefries+costofBurger+costofPizza+costofCheese_burger+costofDrinks)/99)
    Service="Rs." ,str("%.2f"% Ser_Charge)
    OverAllCost="Rs.",str(PayTax+TotalCost+Ser_Charge)
    Service_Charge.set(Service)
    cost.set(costofMeal)
    Tax.set(PayTax)
    Subtotal.set(costofMeal)
    Total.set(OverAllCost)
    # Insert order details into the database
    cursor.execute('''
        INSERT INTO orders (
            fries, lunch_fries, burger, pizza, cheese_burger, drinks,
            total_cost, service_charge, tax, Total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        int(Fries.get()), int(lunchfries.get()), int(Burger.get()),
        int(Pizza.get()), int(Cheese_burger.get()), int(Drinks.get()),
        TotalCost, Ser_Charge, PayTax, TotalCost + Ser_Charge + PayTax
    ))
    connection.commit()
    connection.close()

def xquit():
    root.destroy() 


def clear_one():
    global operator
    operator = operator[:-1]
    text_input.set(operator)       

def reset():
    rand.set("")
    Fries.set("")
    lunchfries.set("")
    Burger.set("") 
    Pizza.set("")
    Cheese_burger.set("")   
    Drinks.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Tax.set("")
    cost.set("")

#------------------------------------------------------------------------------------------
btn=Button(f2,text="7",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(7))
btn.grid(row=2,column=0)

btn8=Button(f2,text="8",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,text="9",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(9))
btn9.grid(row=2,column=2)

Addition=Button(f2,text="+",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)

btn6=Button(f2,text="6",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(6))
btn6.grid(row=3,column=2)

btn4=Button(f2,text="4",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,text="5",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(5))
btn5.grid(row=3,column=1)

Subtraction=Button(f2,text="-",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f2,text="1",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,text="2",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,text="3",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(3))
btn3.grid(row=4,column=2)

Multiplecation=Button(f2,text="*",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick("*"))
Multiplecation.grid(row=4,column=3)

btn0=Button(f2,text="0",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick(0))
btn0.grid(row=5,column=0)

btnclear=Button(f2,text="C",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=clrdisplay)
btnclear.grid(row=5,column=1)

btndot=Button(f2,text=".",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick("."))
btndot.grid(row=5,column=2)

Devision=Button(f2,text="/",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=lambda: btnclick("/"))
Devision.grid(row=5,column=3)

Devision=Button(f2,text="=",padx=16,pady=16,bd=4,width=10,fg="black",font="ariel 20 bold",bg="powder blue",command=equls)
Devision.grid(columnspan=3)

btnclear=Button(f2,text="<",padx=16,pady=16,bd=4,fg="black",font="ariel 20 bold",bg="powder blue",command=clear_one)
btnclear.grid(row=6,column=3)

rand=StringVar()
Fries=StringVar()
lunchfries=StringVar()
Cheese_burger=StringVar()
Burger=StringVar()
Pizza=StringVar()
Drinks=StringVar()
Service_Charge=StringVar()
Tax=StringVar()
cost=StringVar()
Subtotal=StringVar()
Total=StringVar()

lblreference=Label(f1,font="aria 16 bold",text="Order No.",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=0,column=0)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=rand,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=0,column=1)

lblreference=Label(f1,font="aria 16 bold",text="Cheese Burger",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=5,column=0)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Cheese_burger,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=5,column=1)

lblfries=Label(f1,font="aria 16 bold",text="Fries Meal",fg="steel blue",bd=10,anchor="w")
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font="ariel 16 bold",textvariable=Fries,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtfries.grid(row=1,column=1)

lblreference=Label(f1,font="aria 16 bold",text="Lunch Meal",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=2,column=0)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=lunchfries,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=2,column=1)

lblreference=Label(f1,font="aria 16 bold",text="Burger",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=3,column=0)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Burger,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=3,column=1)

lblreference=Label(f1,font="aria 16 bold",text="pizza",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=4,column=0)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Pizza,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=4,column=1)

lblreference=Label(f1,font="aria 16 bold",text="Drinks",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=0,column=2)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Drinks,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=0,column=3)

lblreference=Label(f1,font="aria 16 bold",text="Cost",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=1,column=2)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=cost,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=1,column=3)

lblreference=Label(f1,font="aria 16 bold",text="Service Charge",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=2,column=2)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Service_Charge,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=2,column=3)

lblreference=Label(f1,font="aria 16 bold",text="Sub total",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=3,column=2)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Subtotal,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=3,column=3)

lblreference=Label(f1,font="aria 16 bold",text="Tax",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=4,column=2)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Tax,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=4,column=3)

lblreference=Label(f1,font="aria 16 bold",text="Total",fg="steel blue",bd=10,anchor="w")
lblreference.grid(row=5,column=2)
txtreference=Entry(f1,font="ariel 16 bold",textvariable=Total,bd=6,insertwidth=4,bg="powder blue",justify="right")
txtreference.grid(row=5,column=3)

btnTotal=Button(f1,padx=16,pady=8,bd=10,fg="black",font="ariel 16 bold",width=10,text="Total",bg="powder blue",command=total)
btnTotal.grid(row=6,column=1)

btnTotal=Button(f1,padx=16,pady=8,bd=10,fg="black",font="ariel 16 bold",width=10,text="Reset",bg="powder blue",command=reset)
btnTotal.grid(row=6,column=2)

btnTotal=Button(f1,padx=16,pady=8,bd=10,fg="black",font="ariel 16 bold",width=10,text="Exit",bg="powder blue",command=xquit)
btnTotal.grid(row=6,column=3)

def price():
    master=Tk()
    master.geometry("500x300")
    master.title("Price list")
    lblinfo=Label(master,font="aria 15 bold",text="ITEM",fg="Black",bd=5)
    lblinfo.grid(row=0,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="____________________",fg="white",bd=5)
    lblinfo.grid(row=0,column=2)
    lblinfo=Label(master,font="aria 15 bold",text="Price",fg="Black",bd=5)
    lblinfo.grid(row=0,column=3)
    lblinfo=Label(master,font="aria 15 bold",text="Fries Meal",fg="Steel Blue",bd=3)
    lblinfo.grid(row=1,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="25",fg="Steel Blue",bd=3)
    lblinfo.grid(row=1,column=3)
    lblinfo=Label(master,font="aria 15 bold",text="Lunch Meal",fg="Steel Blue",bd=3)
    lblinfo.grid(row=2,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="40",fg="Steel Blue",bd=3)
    lblinfo.grid(row=2,column=3)
    lblinfo=Label(master,font="aria 15 bold",text="Burger Meal",fg="Steel Blue",bd=3)
    lblinfo.grid(row=3,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="35",fg="Steel Blue",bd=3)
    lblinfo.grid(row=3,column=3)
    lblinfo=Label(master,font="aria 15 bold",text="Pizza",fg="Steel Blue",bd=3)
    lblinfo.grid(row=4,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="50",fg="Steel Blue",bd=3)
    lblinfo.grid(row=4,column=3)
    lblinfo=Label(master,font="aria 15 bold",text="Cheese Burger",fg="Steel Blue",bd=3)
    lblinfo.grid(row=5,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="35",fg="Steel Blue",bd=3)
    lblinfo.grid(row=5,column=3)
    lblinfo=Label(master,font="aria 15 bold",text="Drink",fg="Steel Blue",bd=3)
    lblinfo.grid(row=6,column=0)
    lblinfo=Label(master,font="aria 15 bold",text="35",fg="Steel Blue",bd=3)
    lblinfo.grid(row=6,column=3)

btnPrice=Button(f1,padx=16,pady=8,bd=10,fg="black",font="ariel 16 bold",width=10,text="Price",bg="powder blue",command=price)
btnPrice.grid(row=6,column=0)

root.mainloop()
