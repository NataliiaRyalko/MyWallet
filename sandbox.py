import tkinter as tk
from wallet_app import *


class App_GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #input fields
        self.input_transaction_value = tk.Entry(self)
        self.input_transaction_value.grid(row = 9, column = 1)

        self.input_account_value = tk.Entry(self)
        self.input_account_value.grid(row=4, column=1)

        self.input_account_name = tk.Entry(self)
        self.input_account_name.grid(row=2, column=1)
        #lebels
        self.input_account_name_label = tk.Label(self, text ="Enter Account name:")
        self.input_account_name_label.grid(row = 1, column = 1)

        self.input_account_name_label = tk.Label(self, text="Enter Account value:")
        self.input_account_name_label.grid(row=3, column=1)

        self.input_transaction_value_label = tk.Label(self, text="Enter Transaction value:")
        self.input_transaction_value_label.grid(row=8, column=1)

        self.input_transaction_value_label = tk.Label(self, text="Select account:")
        self.input_transaction_value_label.grid(row=6, column=1)


        #buttons
        self.add_account_btn = tk.Button(self, text="Add Account", command=self.account_callback)
        self.add_account_btn.grid(row=5, column=1)

        self.add_transaction_btn = tk.Button(self, text="Add Transaction", command=self.transaction_callback)
        self.add_transaction_btn.grid(row=10, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.grid(row=11, column=1)
        #listboxes
        self.listbox=tk.Listbox(self,height=5,selectmode='SINGLE',yscrollcommand = True)
        self.listbox.grid(row = 7,column = 1)
        #window settings
        self.master.title('My wallet')
        # self.master.geometry("500x300")

    """
    account_callback function responsibilities:
       -gets data for account creating
       -creates accounts and account list
       -add and displays account name to listbox 
    """

    def account_callback(self):
        self.entered_value = Decimal(self.input_account_value.get()).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self.entered_name = self.input_account_name.get()
        account = Account(self.entered_name, self.entered_value)
        wallet.add_account(account)
        account_list = wallet.account_list
        account_key = account.account_name
        self.listbox.insert(tk.END, account_key)
        print(account_list)

    """
    transaction_callback function responsibilities:
       -gets data for transaction creating
       -creates transaction 
       -make calculations with selected from listbox account
        and transaction
    """
    def transaction_callback(self):

        self.entered_value = Decimal(self.input_transaction_value.get()).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        # print(self.entered_value)
        selected_account = self.listbox.curselection()
        # print(self.listbox.get(selected_account))
        account_key = self.listbox.get(selected_account,last=None)
        print(account_key)
        curr_account = wallet.account_list[account_key]
        transaction = Transaction(self.entered_value,curr_account)
        wallet.add_transaction(transaction)
        print(curr_account.account_value)
        print(wallet.transaction_list)


root = tk.Tk()
app = App_GUI(master=root)
app.mainloop()




