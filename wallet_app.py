"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""
import time
from datetime import datetime
from decimal import *



class Account(object):
    # var name always is string, var value is number
    def __init__(self, name, value):
        self.account_name = name
        self.account_value = value

class Transaction(object):
    # var name always is string, var value is number, account is object of Account class
    def __init__(self, value, account,category):
        self.transaction_name = datetime.now().strftime("%H:%M:%S %d-%m-%y")
        self.transaction_value = value
        self.transaction_account = account
        self.category = category
        spent_account_money = self.set_spend()
        account.account_value = spent_account_money


    # set
    def set_spend(self):
        spend = self.transaction_account.account_value - self.transaction_value
        return spend


class Wallet(object):
    transaction_list = {}
    account_list = {}
    category_list = {}

    def add_account(self,account):
        self.account_list[account.account_name] = account

    def add_transaction(self, transaction):
        self.transaction_list[transaction.transaction_name] = transaction
        self.category_list[transaction.category] = {}
        for item in self.transaction_list.values():
            for key in self.category_list:
                if item.category == key:
                    item_dict = {}
                    item_dict[item.transaction_name] = item
                    self.category_list[key].update(item_dict)
        print(self.category_list, "this one")






wallet = Wallet()



