#--------------------------------------INTERNPE------------ASSIGNMENT--------------------------------


#--------------------------------------------CURRENCY CONVERTER--------------------------------------------


import tkinter as tk
from tkinter import *
import tkinter.messagebox
 
root = tk.Tk() 

root.title("Currency Conversion")



headlabel = tk.Label(font=('Comic sans', 19,'bold'), text = '                                   Currency Converter:  ') 
headlabel.grid(row=1, column=0,sticky=W)
 
variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 
 
variable1.set("currency") 
variable2.set("currency") 

def RealTimeCurrencyConversion(): 
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()
    
    from_currency = variable1.get() 
    to_currency = variable2.get()
    
    if (Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Amount Not Entered","\n Please a valid amount.")
        
    elif (from_currency=="currency" or to_currency=="currency"):
        tkinter.messagebox.showinfo("Currency Not Selected.","\n Please select FROM and TO Currency .")
        
    else:
        new_amt = c.convert(from_currency,to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount)) 


    
    
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","AUD","DOP","FJD","KES","NZD","SGD","LKR","XCD"]


root.configure() 
root.geometry("700x400") 

Label2 =Label(root, font=('Comic sans', 28,'bold'), text="",padx=2,pady=2)
Label2.grid(row=1, column=0,sticky=W)


label1 = tk.Label(root,font=('Comic sans', 15,'bold'), text = "\t    Enter Amount  :  ")
label1.grid(row=2, column=0,sticky=W)

label1 = tk.Label(root,font=('Comic sans', 15,'bold'), text = "\t    From - Currency  :  ") 
label1.grid(row=3, column=0,sticky=W)

label1 = tk.Label(root,font=('Comic sans', 15,'bold'), text = "\t    To - Currency  :  ") 
label1.grid(row=4, column=0,sticky=W)

label1 = tk.Label(root,font=('Comic sans', 15,'italic'), text = "\t    Converted Amount  :  ") 
label1.grid(row=8, column=0,sticky=W)


Label2 =Label(root, font=('Comic sans', 20,'bold'), text="",padx=2,pady=2)
Label2.grid(row=5, column=0,sticky=W)

Label2 =Label(root, font=('Comic sans', 20,'bold'), text="",padx=2,pady=2)
Label2.grid(row=7, column=0,sticky=W)



FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list) 
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list) 

FromCurrency_option.grid(row = 3, column = 0, ipadx = 45,sticky=E) 
ToCurrency_option.grid(row = 4, column = 0, ipadx = 45,sticky=E) 




Amount1_field = tk.Entry(root) 
Amount1_field.grid(row=2,column=0,ipadx =28,sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8,column=0,ipadx =31,sticky=E) 




Label_9 =Button(root, font=('arial', 15,'underline'), text="   Convert  ",padx=2,pady=2, command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)

Label2 =Label(root, font=('Comic sans', 7,'bold'), text="",padx=2,pady=2)
Label2.grid(row=9, column=0,sticky=W)


root.mainloop()