"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""
import time
from datetime import datetime
from tkinter import *



class Account(object):
    # var name always is string, var value is number
    def __init__(self, name, value):
        self.account_name = name
        self.account_value = value


class Transaction(object):
    # var name always is string, var value is number, account is object of Account class
    def __init__(self, value, account):
        self.transaction_name = datetime.now().strftime("%H:%M %d-%m-%y")
        self.transaction_value = value
        self.transaction_account = account
        spent_account_money = self.set_spend()
        account.account_value = spent_account_money

    # set
    def set_spend(self):
        spend = self.transaction_account.account_value - self.transaction_value
        return spend


class Wallet(object):
    account = Account("cash", 1000)
    transaction = []
    test_account_list = []
    def add_account(self):
        self.test_account_list.append(self.account)

    def add_transaction(self, transaction):
        self.transaction.append(transaction)


wallet = Wallet()


#GUI:

#root window
root = Tk()

#timer
def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')
label = Label(root, font='sans 20')
label.pack()
label.after_idle(tick)

#input
input_value = Entry(root)
input_value.pack()

def callback():

    entered_value  = input_value.get()
    print (entered_value)
    wallet.add_transaction(Transaction(int(entered_value),wallet.account))
    print(wallet.account.account_value)


#button
def button_click():
        bg = '#f4e541'
        button_test['bg'] = bg
button_test = Button(root, text= "test",command = callback)
button_test.pack()
#test_area
def make_test():
    wallet.add_account()
    print(wallet.test_account_list)

button_test_dict = Button(root,text = "dict",command = make_test)
button_test_dict.pack()
#  window options
root.title('Simple wallet app')
root.geometry('500x400')
root.resizable(True, False)

root.mainloop()
