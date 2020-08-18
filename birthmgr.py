#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from db import Database

#import database
db=Database('Store records.db')


def clear_search(event):
    b = Entry(app,width=100)
    b.insert(0,"Enter the birthdate in this format dd/mm/yyyy") 
    search.delete(0, END)
    search = Entry(app, width=100)
    search.insert(0, "Enter the birthdate in this format dd/mm/yyyy")
    search.pack()
    search.bind("<Button-1>", clear_search)
 

#add new entries
def addbirth():       
  
    if part_text.get() == '' or birthday_text.get() == '':
        messagebox.showerror('Required Fields', "Please include all fields")   
        return                                   
    db.insert(part_text.get(), birthday_text.get())
    list_box.delete(0, END)
    list_box.insert(END, part_text.get(), birthday_text.get())
    view_birth()

#select item from entries
def select_item(event):
    try:
        global selected_item
        index = list_box.curselection()[0]
        selected_item = list_box.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
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
    db.update(selected_item[0], part_text.get(), birthday_text.get())
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
def today_view():
    print('okay')    

def client_exit():
      exit()

#clear input
def clear_item():
    part_entry.delete(0, END)
    birthday_entry.delete(0, END)
   
#create window object
app=Tk()


#widget 
part_text = StringVar()
part_label = Label(app, text = 'Name', font=('bold',14), pady = 20, padx=10)
part_label.grid(row = 0, column=0, sticky=W)
#text entry box
part_entry = Entry(app,textvariable=part_text)
part_entry.grid(row=0, column=1)

#widget for birthday
birthday_text = StringVar()
birthday_label = Label(app, text = 'Birth Date', font=('bold',14), pady = 20)
birthday_label.grid(row = 0, column=2, sticky=W)
#text entry box
birthday_entry = Entry(app,textvariable=birthday_text)
birthday_entry.grid(row=0, column=3)

#listbox widget
list_box=Listbox(app, height=11, width=45, border=0)
list_box.grid(row=3, column=0, columnspan=3, rowspan=4, pady=20, padx=20)

#scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4,column=3)
#set scrollbar to listbox
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)
#bind select
list_box.bind('<<ListboxSelect>>',select_item)

#buttons
add_btn=Button(app, text='Add Birthday', width=11, command=addbirth)
add_btn.grid(row=2, column=0, pady=20, padx=5)

update_btn=Button(app, text='Update Birthday', width=11, command=update_birth)
update_btn.grid(row=2, column=1, pady=20)

delete_btn=Button(app, text='Delete Birthday', width=11, command=delete_birth)
delete_btn.grid(row=2, column=2, pady=20)

today_btn=Button(app, text='Birthdays Today', width=11, command=today_view)
today_btn.grid(row=2, column=3, pady=20)

clear_btn=Button(app, text='Clear Input', width=11, command=clear_item)
clear_btn.grid(row=8, column=1, pady =20)

exit_btn=Button(app, text='Exit', width=10, command=client_exit)
exit_btn.grid(row=8, column=3, pady=10)

#view birthday
view_birth()



app.title('Birthday App')  
app.geometry('550x470')



app.mainloop()
