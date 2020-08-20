from tkinter import *
from tkinter import messagebox
from db import Database

#import database
db=Database('Store records.db')

#add new entries
def addbirth():       
    if (name_text.get() == '') or (birthday_text.get() == ''):
        messagebox.showerror('Required Fields', "Please include all fields")   
        return                                   
    db.insert(name_text.get(), birthday_text.get())
    list_box.delete(0, END)
    list_box.insert(END, name_text.get(), birthday_text.get())
    view_birth()

#select item from entries
def select_item(event):
    try:
        global selected_item
        index = list_box.curselection()[0]
        selected_item = list_box.get(index)

        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        birthday_entry.delete(0, END)
        birthday_entry.insert(END, selected_item[2])
    except IndexError:
        pass

#remove birthday    
def delete_birth():
    db.remove(selected_item[0])
    clear_item()
    view_birth()

#function for updating and editing records
def update_birth():
    db.update(selected_item[0], name_text.get(), birthday_text.get())
    view_birth()

#show all entries
def view_birth():
    list_box.delete(0, END)
    count = 0
    for NAME,DATE in db.fetch():
        count+=1
        new_row = count, NAME, DATE
        list_box.insert(END,new_row)

#show only entries for today      
def today_view():#yet to be designed??????
    print('okay')    

def client_exit():
      exit()

#clear input
def clear_item():
    name_entry.delete(0, END)
    birthday_entry.delete(0, END)
   
app=Tk()
#widget 
name_text = StringVar()
name_label = Label(app, text = 'Name', font=('bold',14), pady = 5, padx=20)
name_label.grid(row = 0, column=0, sticky=W)
#text entry box
name_entry = Entry(app,textvariable=name_text)
name_entry.grid(row=0, column=1)

#widget for birthday
birthday_text = StringVar()
birthday_label = Label(app, text = 'Birth Date', font=('bold',14),padx =5, pady = 20)
birthday_label.grid(row = 0, column=2, sticky=W)
#text entry box
birthday_entry = Entry(app,textvariable=birthday_text)
birthday_entry.grid(row=0, column=3)

#listbox widget
list_box=Listbox(app, height=11, width=45, border=0)
list_box.grid(row=3, column=1, columnspan=2, rowspan=4, padx=2, pady=20)

#scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,column=3)
#set scrollbar to listbox
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)
#bind select
list_box.bind('<<ListboxSelect>>',select_item)

#buttons
add_btn=Button(app, text='Add Birthday', width=11, command=addbirth)
add_btn.grid(row=2, column=0,padx=12, pady=20)

update_btn=Button(app, text='Update Birthday', width=11, command=update_birth)
update_btn.grid(row=2, column=1, pady=20)

delete_btn=Button(app, text='Delete Birthday', width=11, command=delete_birth)
delete_btn.grid(row=2, column=2, pady=20)

today_btn=Button(app, text='Birthdays Today', width=11, command=today_view)
today_btn.grid(row=2, column=3, pady=20)

clear_btn=Button(app, text='Clear Input', width=11, command=clear_item)
clear_btn.grid(row=8, column=1, pady =10)

exit_btn=Button(app, text='Exit', width=10, command=client_exit)
exit_btn.grid(row=8, column=2, pady=10)

#view birthday
view_birth()

app.title('Birthday App')  
app.geometry('690x520')

app.mainloop()
