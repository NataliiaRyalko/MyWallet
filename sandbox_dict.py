
import datetime

date_time = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%y")

account = {}
account["cash"] = 1000

print account

transaction = {}

transaction["value"] = 100
transaction["discription"] = "it's transaction"
transaction["category"] = "test_category"
transaction_stack = {}
transaction_stack[date_time] = transaction

def calc(account_v,transaction_value):
	calc  = account_v - transaction_value
	account['cash'] = calc
	
calc(account['cash'], transaction['value'])	
print transaction_stack

print account
