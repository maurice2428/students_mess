from tkinter import*
import random
from time import strftime
import time;
import datetime
from tkinter import messagebox

root = Tk()
root.geometry("1350x800+0+0")
root.title("Mess-Jaramogi Oginga Odinga Univerity of Science and Technology")
root.configure(background='#B8860B')


text_Input = StringVar()
operator = ""

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

Tops = Frame(root, width=1600, height=50, bd=5, relief='sunken')
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, bd=5, relief='sunken')
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bd=5, relief='sunken')
f2.pack(side=RIGHT)

f1a = Frame(f1, width=800, height=500, bd=5, relief='sunken')
f1a.pack(side=TOP)

f1b = Frame(f1, width=800, height=200, bd=5, relief='sunken')
f1b.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=700, bd=5, relief='sunken')
f1aa.pack(side=LEFT)

f1ab = Frame(f1a, width=400, height=700, bd=5, relief='sunken')
f1ab.pack(side=RIGHT)

Tops.configure(background='#DAA520')
f2.configure(background='#DAA520')
f1.configure(background='#DAA520')

#===========================Time=========================================================================================

#========================================================================================================================
lblInfo = Label(Tops,font= ("arial", 30, "bold"),text="MESS_JOOUST_SYSTEM",fg="black", bd= 2, anchor="w")
lblInfo.grid(row=0,column=0)
label = Label(Tops, font=("arial", 30),foreground="cyan")
label.grid(row=1,column=0)
time()
#===================================CALCULATOR=============================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_Input.set("")
    
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def ref():
    x = random.randint(120100, 240200)
    randomRef = str(x)
    rand.set(randomRef)
    
    CoF  =float(Chapati.get())
    CoD = float(Soda.get())
    CoCabbage = float(Cabbage.get())
    CoUgali = float(Ugali.get())
    CoBeef = float(Beef.get())
    CoNdegu = float(Ndegu.get())
    CoTea = float(Tea.get())
    CoMaandazi = float(Maandazi.get())
    CoBread = float(Bread.get())
    CoKales = float(Kales.get())
    CoMatumbo = float(Matumbo.get())
    CoBeans = float(Beans.get())
    
    
    CostofChapati = CoF * 10.00
    CostofSoda = CoD * 30.00
    CostofCabbage = CoCabbage * 10.00
    CostofUgali = CoUgali * 10.00
    CostBeef = CoBeef * 30.00
    CostNdegu = CoNdegu * 15.00
    CostTea = CoTea * 10.00
    CostMaandazi = CoMaandazi * 5.00
    CostBread = CoBread * 20.00
    CostKales = CoKales * 10.00
    CostMatumbo = CoMatumbo * 20.00
    CostBeans = CoBeans * 10.00
    
    CostofMeal = "Kshs.",str('%.2f' % (CostofChapati  + CostofSoda + CostofCabbage + CostofUgali + CostBeef +
                             CostNdegu + CostMaandazi + CostTea + CostBread + CostKales + CostMatumbo+ CostBeans))
    
    PayTax = ((CostofChapati  + CostofSoda + CostofCabbage + CostofUgali + CostBeef + 
                 CostNdegu + CostMaandazi + CostTea + CostBread + CostKales+ CostMatumbo+ CostBeans)*0.00125)
    
    TotalCost = (CostofChapati  + CostofSoda + CostofCabbage + CostofUgali + CostBeef + CostNdegu +
                     CostMaandazi + CostTea+ CostBread + CostKales+ CostMatumbo+ CostBeans)
    
    Ser_Charge = ((CostofChapati  + CostofSoda + CostofCabbage + CostofUgali + CostBeef + CostNdegu +
                     CostMaandazi + CostTea + CostBread + CostKales+ CostMatumbo + CostBeans)/99)
    
    Service = "Kshs.",str('%.2f' % Ser_Charge)    
    OverALLCost = "Kshs.",str('%.2f' % (PayTax + TotalCost + Ser_Charge))    
    PaidTax = "Kshs.",str('%.2f' % PayTax)
    
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverALLCost)
    
    
        
def qExit():
    qExit = messagebox.askyesno("Terminate System","Do you want to end session?")
    if qExit > 0:
        root.destroy()
        return
    

def Reset():
    rand.set("") 
    Chapati.set("")
    Ugali.set("")
    Cabbage.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Soda.set("")
    Tax.set("")
    Cost.set("")
    Beef.set("")
    Ndegu.set("")  
    Tea.set("") 
    Bread.set("")
    Kales.set("")
    Maandazi.set("")
    Matumbo.set("")
    Beans.set("")
#================================================Calculator=====================================================================================================
txtDisplay = Entry(f2, font=("arial", 20, "bold"), textvariable=text_Input, bd=5, insertwidth=8, bg="white", justify='right')
txtDisplay.grid(columnspan=5)

btn10 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="(", bg="grey", command=lambda: btnClick('(')).grid(row=2, column=4)
btn11= Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text=")", bg="grey", command=lambda: btnClick(')')).grid(row=3, column=4)
btn12 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="^", bg="grey", command=lambda: btnClick('**')).grid(row=4, column=4)
btn13= Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20,"bold" ), text=".", bg="grey", command=lambda: btnClick('.')).grid(row=5,column=4)
#===============================================================================================================================================================
btn7 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="7", bg="grey", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="8", bg="grey", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="9", bg="grey", command=lambda: btnClick(9)).grid(row=2, column=2)
Addition = Button(f2, padx=13, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="+", bg="grey", command=lambda: btnClick("+")).grid(row=2, column=3)
#===============================================================================================================================================================
btn6 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="4", bg="grey", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="5", bg="grey", command=lambda: btnClick(5)).grid(row=3, column=1)
btn4 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="6", bg="grey", command=lambda: btnClick(6)).grid(row=3, column=2)
Subtraction = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="-", bg="grey", command=lambda: btnClick("-")).grid(row=3, column=3)
#===============================================================================================================================================================
btn1 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="1", bg="grey", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="2", bg="grey", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="3", bg="grey", command=lambda: btnClick(3)).grid(row=4, column=2)
Multiply = Button(f2, padx=13, pady=16, bd=4, fg="white",font= ("arial", 20, "bold"), text="x", bg="grey", command=lambda: btnClick("*")).grid(row=4, column=3)
#===========================================================Buttons====================================================================================
btn0 = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 18, "bold"), text="0", bg="grey", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 14,"bold"), text="CL", bg="grey", command=btnClearDisplay).grid(row=5, column=1)
btnEquals = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 16, "bold"), text="=", bg="grey",command=btnEqualsInput).grid(row=5, column=2)
Division = Button(f2, padx=16, pady=16, bd=4, fg="white",font= ("arial", 18, ), text="/", bg="grey", command=lambda: btnClick("/")).grid(row=5, column=3)
#============================================================MESS INFO1================================================================================
rand = StringVar()
Chapati = StringVar()
Ugali = StringVar()
Cabbage = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Soda = StringVar()
Tax = StringVar()
Cost = StringVar()
Beef = StringVar()
Ndegu = StringVar()
Tea = StringVar()
Maandazi = StringVar()
Bread = StringVar()
Kales = StringVar()
Matumbo = StringVar()
Beans = StringVar()

lblReference = Label(f1aa,font= ("arial", 12, "bold"),text="Reference",fg="black", bd= 2, anchor="w")
lblReference.grid(row=0,column=0)
textReference = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=rand, bd=4,insertwidth=2, justify="right")
textReference.grid(row=0, column=1)

lblChapati = Label(f1aa,font= ("arial", 12, "bold"),text="Chapati",fg="black", bd= 2, anchor="w")
lblChapati.grid(row=1,column=0)
textChapati = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Chapati, bd=4,insertwidth=2,justify="right")
textChapati.grid(row=1, column=1)

lblMatumbo = Label(f1aa,font= ("arial", 12, "bold"),text="Matumbo",fg="black", bd= 2, anchor="w")
lblMatumbo.grid(row=2,column=0)
textMatumbo = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Matumbo, bd=4,insertwidth=2,justify="right")
textMatumbo.grid(row=2, column=1)

lblUgali = Label(f1aa,font= ("arial", 12, "bold"),text="Ugali",fg="black", bd= 2, anchor="w")
lblUgali.grid(row=3,column=0)
textUgali = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Ugali, bd=4,insertwidth=2, justify="right")
textUgali.grid(row=3, column=1)

lblCabbage = Label(f1aa,font= ("arial", 12, "bold"),text="Cabbage",fg="black", bd= 2, anchor="w")
lblCabbage.grid(row=4,column=0)
textCabbage = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Cabbage, bd=4,insertwidth=2,justify="right")
textCabbage.grid(row=4, column=1)

lblBeef = Label(f1aa,font= ("arial", 12, "bold"),text="Beef",fg="black", bd= 2, anchor="w")
lblBeef.grid(row=5,column=0)
textBeef = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Beef, bd=4,insertwidth=2, justify="right")
textBeef.grid(row=5, column=1)

lblNdegu = Label(f1aa,font= ("arial", 12, "bold"),text="Ndegu",fg="black", bd= 2, anchor="w")
lblNdegu.grid(row=6,column=0)
textNdegu = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Ndegu, bd=4,insertwidth=2, justify="right")
textNdegu.grid(row=6, column=1)

lblTea = Label(f1aa,font= ("arial", 12, "bold"),text="Tea",fg="black", bd= 2, anchor="w")
lblTea.grid(row=7,column=0)
textTea = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Tea, bd=4,insertwidth=2, justify="right")
textTea.grid(row=7, column=1)

lblMaandazi = Label(f1aa,font= ("arial", 12, "bold"),text="Maandazi",fg="black", bd= 2, anchor="w")
lblMaandazi.grid(row=8,column=0)
textMaandazi = Entry(f1aa, font=("arial", 12 , "bold"),fg="black",textvariable=Maandazi, bd=4,insertwidth=2, justify="right")
textMaandazi.grid(row=8, column=1)

#===========================================================MESS INFO2==========================================================
lblBeans = Label(f1ab,font= ("arial", 12, "bold"),text="Beans",fg="black", bd= 2, anchor="w")
lblBeans.grid(row=0,column=2)
textBeans = Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Beans, bd=4,insertwidth=2, justify="right")
textBeans.grid(row=0, column=3)

lblSoda = Label(f1ab,font= ("arial", 12, "bold"),text="Soda",fg="black", bd= 2, anchor="w")
lblSoda.grid(row=1,column=2)
textSoda = Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Soda, bd=4,insertwidth=2, justify="right")
textSoda.grid(row=1, column=3)

lblBread = Label(f1ab,font= ("arial", 12, "bold"),text="Bread",fg="black", bd= 2, anchor="w")
lblBread.grid(row=2,column=2)
textBread = Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Bread, bd=4,insertwidth=2, justify="right")
textBread.grid(row=2, column=3)

lblKales = Label(f1ab,font= ("arial", 12, "bold"),text="Kales",fg="black", bd= 2, anchor="w")
lblKales.grid(row=3,column=2)
textKales = Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Kales, bd=4,insertwidth=2, justify="right")
textKales.grid(row=3, column=3)

lblCost = Label(f1ab,font= ("arial", 12, "bold"),text="Cost of Meal",fg="black", bd= 2, anchor="w")
lblCost.grid(row=4,column=2)
textCost = Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Cost, bd=4,insertwidth=4, justify="right")
textCost.grid(row=4, column=3)

lblSubTotal = Label(f1ab,font= ("arial", 12, "bold"),text="SubTotal",fg="black", bd= 2, anchor="w")
lblSubTotal.grid(row=5,column=2)
textSubTotal= Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=SubTotal, bd=4,insertwidth=4, justify="right")
textSubTotal.grid(row=5, column=3)

lblStateTax = Label(f1ab,font= ("arial", 12, "bold"),text="Tax",fg="black", bd= 2, anchor="w")
lblStateTax.grid(row=6,column=2)
textStateTax= Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Tax, bd=4,insertwidth=4, justify="right")
textStateTax.grid(row=6, column=3)

lblService = Label(f1ab,font= ("arial", 12, "bold"),text="Service Charge",fg="black", bd= 2, anchor="w")
lblService.grid(row=7,column=2) 
textService= Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Service_Charge, bd=4,insertwidth=4, justify="right")
textService.grid(row=7, column=3)

lblTotal = Label(f1ab,font= ("arial", 12, "bold"),text="Total Cost",fg="black", bd= 2, anchor="w")
lblTotal.grid(row=8,column=2)
textTotal= Entry(f1ab, font=("arial", 12 , "bold"),fg="black",textvariable=Total, bd=4,insertwidth=4, justify="right")
textTotal.grid(row=8, column=3)
#===========================================================BUTTONS==========================================================
btnTotal  = Button(f1b, padx=16, pady=8, bd=8, fg="yellow",font= ("arial", 12, "bold"), text="TOTAL", bg="brown",command=ref).grid(row=13, column=1)
btnReset = Button(f1b, padx=16, pady=8, bd=8, fg="orange",font= ("arial", 12, "bold"), text="RESET", bg="grey",command=Reset).grid(row=13, column=2)
btnExit = Button(f1b, padx=16, pady=8, bd=8, fg="red",font= ("arial", 12, "bold"), text="EXIT", bg="lime",command=qExit).grid(row=13, column=3)
#===============================================================================================================================
root.mainloop()