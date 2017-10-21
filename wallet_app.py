"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""
import time
from datetime import date
today = date.today()
# print(today)
class Account(object):
        def __init__(self,name, value):
                self.account_name = name
                self.account_value = value

cash_account = Account("cash",1000)
print(cash_account.account_name)
class Transaction(object):
        def __init__(self,name, value):
                self.transaction_name = name
                self.transaction_value = value
                self.transaction_account = cash_account
                self.transaction_date = today
        def set_transaction(self):
                spent = self.transaction_account.account_value-self.transaction_value
                return  spent

test_transaction = Transaction('test',50)

print (test_transaction.transaction_date)
print (test_transaction.set_transaction())
class Wallet(object):
       pass

