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
    account = Account("cash", 1100)
    transaction_list = []
    account_list = []
    def add_account(self):
        self.account_list.append(self.account)

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)


wallet = Wallet()




