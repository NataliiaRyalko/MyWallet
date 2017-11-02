import tkinter as tk
from wallet_app import *
class App_GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()#row = 1, column = 1)
        self.create_widgets()

    def create_widgets(self):
        self.add_transaction_btn = tk.Button(self, text= "Add Transaction",command = self.callback)
        self.add_transaction_btn.grid(row = 4, column = 1)
        self.input_value = tk.Entry(self)
        self.input_value.grid(row = 3, column = 1)
        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.grid(row=4, column=2)

    def callback(self):
        self.entered_value = self.input_value.get()
        print(self.entered_value)
        wallet.add_transaction(Transaction(int(self.entered_value), wallet.account))
        print(wallet.account.account_value)



root = tk.Tk()
app = App_GUI(master=root)
app.mainloop()






# #input
# input_value = Entry(root)
# input_value.grid(column = 5,row = 2)
#
# def callback():
#
#     entered_value  = input_value.get()
#     print (entered_value)
#     wallet.add_transaction(Transaction(int(entered_value),wallet.account))
#     print(wallet.account.account_value)
#
#
# #button
# button_test = Button(root, text= "test",command = callback)
# button_test.grid(column = 5,row = 3)
#
# #test_area
# def make_test():
#     wallet.add_account()
#     print(wallet.account_list)
#     print(wallet.transaction_list)
#
# button_test_dict = Button(root,text = "dict",command = make_test)
# button_test_dict.grid(column = 5,row = 5)
#
# #  window options
# root.title('Simple wallet app')
# root.geometry('160x200')
# root.resizable(True, False)
#
# root.mainloop(

