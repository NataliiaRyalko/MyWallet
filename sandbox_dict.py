
import datetime
from tkinter import *
date_time = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%y")

account = {}
account["cash"] = 1000

print (account)

transaction = {}

transaction["value"] = 100
transaction["discription"] = "it's transaction"
transaction["category"] = "test_category"
transaction_stack = {}
transaction_stack[date_time] = transaction

def calc(account_v,transaction_v):
	calc  = account_v - transaction_v
	account['cash'] = calc
	
calc(account['cash'], transaction['value'])	
print (transaction_stack)

print (account)

root = Tk()
# root.geometry('200X300')
entry = Entry(root)
entry.pack()
def callback():
	tr_value = entry.get()
	transaction_stack[date_time] = transaction
	transaction["value"] = tr_value
	print(transaction_stack)
	print(date_time)
btn = Button(root, text = 'get',command = callback)
btn.pack()
root.mainloop()