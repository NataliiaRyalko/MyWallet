import tkinter as tk
from wallet_app import *


class App_GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()#row = 1, column = 1)
        self.create_widgets()

    def create_widgets(self):
        #input fields
        self.input_transaction_value = tk.Entry(self)
        self.input_transaction_value.grid(row = 5, column = 1)

        self.input_select_account = tk.Entry(self)
        self.input_select_account.grid(row=5, column=2)
        #lebels
        self.input_account_name_label = tk.Label(self, text ="Enter Account name:")
        self.input_account_name_label.grid(row = 1, column = 2)

        self.input_account_name_label = tk.Label(self, text="Enter Account value:")
        self.input_account_name_label.grid(row=1, column=1)

        self.input_transaction_value_label = tk.Label(self, text="Enter Transaction value:")
        self.input_transaction_value_label.grid(row=4, column=1)

        self.input_transaction_value_label = tk.Label(self, text="Select account(1,2):")
        self.input_transaction_value_label.grid(row=4, column=2)

        self.input_account_value = tk.Entry(self)
        self.input_account_value.grid(row=2, column=1)

        self.input_account_name = tk.Entry(self)
        self.input_account_name.grid(row=2, column=2)
        #buttons
        self.add_account_btn = tk.Button(self, text="Add Account", command=self.account_callback)
        self.add_account_btn.grid(row=3, column=1)

        self.add_transaction_btn = tk.Button(self, text="Add Transaction", command=self.transaction_callback)
        self.add_transaction_btn.grid(row=6, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.grid(row=6, column=2)
        #listboxes
        self.listbox=Listbox(self,height=5,width=15,selectmode=SINGLE)
        self.listbox.grid(row = 7,column = 1)
        #window settings
        self.master.title('Simple wallet app')
        # self.master.geometry("500x300")

    def transaction_callback(self):

        self.entered_value = int(self.input_transaction_value.get())
        print(self.entered_value)
        selected_account = self.listbox.curselection()
        print (selected_account[0])
        selected_account_value = selected_account[0]
        account_list = wallet.account_list
        curr_account = account_list[selected_account_value]
        wallet.add_transaction(Transaction(self.entered_value, curr_account))
        print(curr_account.account_value)

    def account_callback(self):

        self.entered_value = int(self.input_account_value.get())
        self.entered_name = self.input_account_name.get()
        wallet.add_account(Account(self.entered_name,self.entered_value))
        account_list = wallet.account_list
        account_list_index = len(account_list)-1
        curr_account = account_list[account_list_index]
        self.listbox.insert(END, curr_account.account_name)







root = tk.Tk()
app = App_GUI(master=root)
app.mainloop()




'''
#GUI:

#root window
root = Tk()

#timer
def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')
label = Label(root, font='sans 20')
label.grid(column = 5,row = 1)
label.after_idle(tick)

#input
input_value = Entry(root)
input_value.grid(column = 5,row = 2)

def callback():

    entered_value  = input_value.get()
    print (entered_value)
    wallet.add_transaction(Transaction(int(entered_value),wallet.account))
    print(wallet.account.account_value)


#button
button_test = Button(root, text= "test",command = callback)
button_test.grid(column = 5,row = 3)

#test_area
def make_test():
    wallet.add_account()
    print(wallet.account_list)
    print(wallet.transaction_list)

button_test_dict = Button(root,text = "dict",command = make_test)
button_test_dict.grid(column = 5,row = 5)

#  window options
root.title('Simple wallet app')
root.geometry('160x200')
root.resizable(True, False)

root.mainloop()

'''
