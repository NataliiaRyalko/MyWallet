#
# import datetime
# from tkinter import *
# date_value = datetime.datetime.now().strftime("%d-%m-%y")
#
# account = {}
# account["cash"] = 1000
#
# print (account)
#
# transaction = {}
#
# transaction["value"] = 100
# transaction["discription"] = "it's transaction"
# transaction["category"] = "test_category"
# transaction_stack = {}
# transaction_stack[date_value] = transaction
#
# def calc(account_v,transaction_v):
# 	calc  = account_v - transaction_v
# 	account['cash'] = calc
#
# calc(account['cash'], transaction['value'])
# print (transaction_stack)
#
# print (account)
#
# root = Tk()
# root.geometry('200x300')
# entry = Entry(root)
# entry.pack()
#
# import time
# def tick():
#     label.after(200, tick)
#     label['text'] = time.strftime('%H:%M:%S')
# label = Label(root,font='sans 20')
# label.pack()
# label.after_idle(tick)
#
# # def callback():
# # 	time_value = date_value+' '+label['text']
# # 	tr_value = entry.get()
# 	transaction_stack[time_value] = transaction
# 	transaction["value"] = tr_value
# 	print(transaction_stack)
# 	print(time_value)
#
# btn = Button(root, text = 'get',command = callback)
# btn.pack()
# root.mainloop()
'''
test  = {}
test['one'] = 'one'

for i in test:
	if test[i] == i:
		print('ok')
	else:
		print('not ok')

file = open('test.txt',"w")
file.write('{1:"hello"}')
file.close()
import ast
def read_from_file(file_name):
        file = open(file_name, 'r')
        read_file = file.read()
        file.close()
        read_file = ast.literal_eval(ead_file)
        return read_file
print read_from_file('test.txt')



my_dict = {'key' : [1,2,3]}

import json
def dict_to_binary(the_dict):
    string = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in string)
    return binary


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

bin_dict = dict_to_binary(my_dict)
print (bin_dict)

dct = binary_to_dict(bin_dict)
print (dct)
# import sys
# print (sys.version_info)

# import PySide
# from PySide.QtGui import QMessageBox, QApplication
# # Create the application object
# app = QApplication(sys.argv)
#
# # Create a simple dialog box
# msgBox = QMessageBox()
# msgBox.setText("Hello World - using PySide version " + PySide.__version__)
# msgBox.exec_()
#

data = {1:"A"}
import json
with open('data.txt', 'w') as outfile:

import tkinter as tk
root = tk.Tk()
lb = tk.Listbox(root, selectmode = 'SINGLE') 
lb.grid(row = 1, column = 1)
lb.insert(tk.END, "test")

def callback_event(e):
	print('It Works')

lb.bind('<<ListboxSelect>>', callback_event)
root.mainloop()
'''
import json
d = {1:None,2:None}
with open('test.txt',"w") as outfile:
	json.dump(d,outfile)
print (d)
