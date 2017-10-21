"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""
from  time import *
class Account(object):
        def __init__(self):
                self.account_name = 'Cash'#input('enter account name: ')
                self.account_value = 100#input("enter account value: ")


class Transaction(object):
        def __init__(self):
                self.transaction_name = 'test'#input('enter transaction name: ')
                self.transaction_value = 50#input('enter transaction value ')
                # self.transaction_account = Account()
                # self.transaction_date = time()


class Wallet(object):

        account = Account()
        transaction = Transaction()
    # transaction.transaction_account = account

