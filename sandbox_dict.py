
import datetime
from tkinter import *
date_value = datetime.datetime.now().strftime("%d-%m-%y")

account = {}
account["cash"] = 1000

print (account)

transaction = {}

transaction["value"] = 100
transaction["discription"] = "it's transaction"
transaction["category"] = "test_category"
transaction_stack = {}
transaction_stack[date_value] = transaction

def calc(account_v,transaction_v):
	calc  = account_v - transaction_v
	account['cash'] = calc
	
calc(account['cash'], transaction['value'])	
print (transaction_stack)

print (account)

root = Tk()
root.geometry('200x300')
entry = Entry(root)
entry.pack()

import time
def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')
label = Label(root,font='sans 20')
label.pack()
label.after_idle(tick)

def callback():
	time_value = label['text']
	tr_value = entry.get()
	transaction_stack[time_value] = transaction
	transaction["value"] = tr_value
	print(transaction_stack)
	print(time_value)

btn = Button(root, text = 'get',command = callback)
btn.pack()
root.mainloop()