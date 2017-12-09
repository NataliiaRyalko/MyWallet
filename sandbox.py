import tkinter as tk
from wallet_app import *
import json

class App_GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        # input fields
        self.input_transaction_value = tk.Entry(self)
        self.input_transaction_value.grid(row = 10, column = 1)
        self.input_transaction_value.insert(0, "10")

        self.input_account_value = tk.Entry(self)
        self.input_account_value.grid(row=4, column=1)
        self.input_account_value.insert(0, "100")

        self.input_account_name = tk.Entry(self)
        self.input_account_name.grid(row=2, column=1)
        self.input_account_name.insert(0, "cash")

        self.input_category_name = tk.Entry(self)
        self.input_category_name.grid(row=4, column=2)
        self.input_category_name.insert(0, "transport")
        #lebels
        self.input_account_name_label = tk.Label(self, text ="Enter Account name:")
        self.input_account_name_label.grid(row = 1, column = 1)

        self.input_account_value_label = tk.Label(self, text="Enter Account value:")
        self.input_account_value_label.grid(row=3, column=1)

        self.input_category_name_label = tk.Label(self, text="Enter Category name:")
        self.input_category_name_label.grid(row=3, column=2)

        self.input_transaction_value_label = tk.Label(self, text="Enter Transaction value:")
        self.input_transaction_value_label.grid(row=9, column=1)

        self.input_account_value_label = tk.Label(self, text="Select account:")
        self.input_account_value_label.grid(row=6, column=1)

        self.input_category_value_label = tk.Label(self, text="Select category:")
        self.input_category_value_label.grid(row=6, column=2)

        self.account_display_label = tk.Label(self, text="Current account value:")
        self.account_display_label.grid(row=1, column=2)

        self.account_display = tk.Label(self)
        self.account_display.grid(row=2, column=2)

        self.transaction_label_display = tk.Label(self, text="Last Transaction:")
        self.transaction_label_display.grid(row=9, column=2)

        self.transaction_display = tk.Label(self)
        self.transaction_display.grid(row=10, column=2)
        
        # add buttons
        self.add_account_btn = tk.Button(self, text="Add Account", command=self.account_callback)
        self.add_account_btn.grid(row=5, column=1)

        self.add_transaction_btn = tk.Button(self, text="Add Transaction", command=self.transaction_callback)
        self.add_transaction_btn.grid(row=11, column=1)
        
        self.add_category = tk.Button(self, text="Add category", command=self.category_callback)
        self.add_category.grid(row=5, column=2)
        # del buttons
        self.del_account_btn = tk.Button(self, text="Del Account", command=self.del_ac)
        self.del_account_btn.grid(row=8, column=1)

        self.del_category_btn = tk.Button(self, text="Del Category", command=self.del_cat)
        self.del_category_btn.grid(row=8, column=2)
        # quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.grid(row=12, column=1)
        
        self.transaction_view_btn = tk.Button(self, text = "View all transactions", command = self.transaction_view)
        self.transaction_view_btn.grid(row=11, column=2)
        
        def callback_event(e):
            self.display_account(wallet.account_list[self.account_listbox.get(self.account_listbox.curselection(), last=None)])


        # listboxes
        self.account_listbox=tk.Listbox(self, height=5, selectmode='SINGLE',exportselection = 0)
        self.account_listbox.grid(row = 7, column = 1)
        self.account_listbox.bind('<<ListboxSelect>>', callback_event)

        self.category_listbox = tk.Listbox(self, height=5, selectmode='SINGLE')
        self.category_listbox.grid(row=7, column=2)
        # initialisation
        self.master.title('My wallet')
        wallet.category_list = self.read_from_file('categories.json')
        wallet.transaction_list = self.read_from_file('transactions.json')
        wallet.account_list = self.read_from_file('accounts.json')
        
    def account_callback(self):
        entered_value = Decimal(self.input_account_value.get()).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        entered_name = self.input_account_name.get()
        account = Account(entered_name, entered_value)
        wallet.add_account(account)
        self.display_account(wallet.account_list[entered_name])
        self.account_listbox.insert(tk.END, entered_name)

    def transaction_callback(self):

        entered_value = Decimal(self.input_transaction_value.get()).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        selected_category = self.category_listbox.get(self.category_listbox.curselection(), last=None)
        selected_account = self.account_listbox.get(self.account_listbox.curselection(), last=None)
        transaction = Transaction(entered_value, selected_account, selected_category)
        wallet.add_transaction(transaction)
        self.display_transaction(transaction)
        wallet.account_list[selected_account] = wallet.spend(wallet.account_list[selected_account],
                                                             wallet.transaction_list[transaction.transaction_name]["value"])
        self.display_account(wallet.account_list[selected_account])
        print(wallet.transaction_list, 'this is transaction list')
        self.save_to_file('transactions.json',wallet.transaction_list)
        self.save_to_file('accounts.json',wallet.account_list)
        print(wallet.account_list)
        
    def category_callback(self):
        category_name = self.input_category_name.get()
        wallet.category_list[category_name] = None
        self.category_listbox.insert(tk.END, category_name)
        self.save_to_file('categories.json',wallet.category_list)

    def display_transaction(self,transaction):
        self.transaction_display['text'] = "%s:" % transaction.transaction_name
        l = [("\n%s:%s" % (x, y)) for x, y in wallet.transaction_list[transaction.transaction_name].items()]
        for item in l:
            self.transaction_display['text'] += "%s" % (item)
        self.transaction_display['fg'] = '#42f477'
        self.transaction_display['bg'] = "#000000"

    def del_ac(self):
        del(wallet.account_list[self.account_listbox.get(self.account_listbox.curselection(),last=None)])
        self.save_to_file('accounts.json',wallet.account_list)
        self.account_listbox.delete(self.account_listbox.curselection(),last=None)
    
    def del_cat(self):
        del(wallet.category_list[self.category_listbox.get(self.category_listbox.curselection(),last=None)])
        self.save_to_file('categories.json',wallet.category_list)
        self.category_listbox.delete(self.category_listbox.curselection()[0])

    def display_account(self,account):
        self.account_display['text'] = "%s UAH" % account 
        self.account_display['fg'] = '#42f477'
        self.account_display['bg'] = "#000000"

    def save_to_file(self,file_name,data):       
        with open(file_name, "w") as outfile:
            json.dump(data, outfile)

    def read_from_file(self,file_name):
        with open(file_name) as data_file:
            data_loaded = json.load(data_file)
            
        if file_name == "accounts.json":
            for key in data_loaded:
                self.account_listbox.insert(tk.END, key)           

        elif file_name == "categories.json":
            for key in data_loaded:
                self.category_listbox.insert(tk.END, key)
                
        return collections.OrderedDict(data_loaded)
    
    def transaction_view(self):
        self.top  = tk.Toplevel(self)
        self.top.title("test")
        self.scroll = tk.Scrollbar(self.top)
        self.scroll.grid(row = 1, column = 2, sticky='NSW')
        self.transaction_textbox = tk.Text(self.top, yscrollcommand = self.scroll.set)
        self.transaction_textbox.grid(row=1, column=1)
        for key,value in wallet.transaction_list.items():
            self.transaction_textbox.insert(tk.END,"\n"+key+"\n")
            for k,v in value.items():
                text_row = (" %s:%s\n") % (k,v)
                self.transaction_textbox.insert(tk.END,text_row)
        self.back_button = tk.Button(self.top, text = "Back",command  = self.top.destroy)
        self.back_button.grid(row = 2,column = 1)
        self.scroll.config(command=self.transaction_textbox.yview)
            
root = tk.Tk()
app = App_GUI(master=root)
app.mainloop()




