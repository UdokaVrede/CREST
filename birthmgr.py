#!/usr/bin/env python3
#import modules
import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry,Calendar

from mydb import Database

#initialize the database to the db variable
db=Database('Store records.db')

#get the current date values
cur_date = datetime.datetime.today()
date_today=cur_date.strftime("%d/%m/%Y")

current_year = int(cur_date.year)
current_month=int(cur_date.month)
current_day=int(cur_date.day)

#event handler 
def kalenda(e):
    global birthday_text
    box = e.widget        #accepts widget event 'e'
    birthday_text = box.get_date().strftime("%d/%m/%Y")         # get date and format date 
     
#add new entries
def addbirth(): 
    try:     
        if (name_text.get() == '') or (birthday_text == ''):
            messagebox.showerror('Required Fields', "Please include all fields")   
            return              
        db.insert(name_text.get(), birthday_text)
        view_birth()
    except NameError:
        messagebox.showinfo("Required field","PLEASE SELECT A DATE")

#select item from entries
def select_item(event):
    try:
        global selected_item
        index = list_box.curselection()[0]
        selected_item = list_box.get(index)
        
        name_entry.delete(0, END)       #delete existing name entries
        name_entry.insert(END, selected_item[1])    #insert name value in entry box
        
    except IndexError:
        pass

#remove birthday    
def delete_birth():
    try:
        if selected_item[0] in DICT_A.keys():
            val = DICT_A[selected_item[0]]
            db.remove(val)
        clear_item()
        view_birth()
    except NameError:
        messagebox.showinfo("Error","SELECT A RECORD TO BE DELETED")
    
#function for updating and editing records
def update_birth():
    try:
        if selected_item[0] in DICT_A.keys():
            valu = DICT_A[selected_item[0]]
        db.update(valu,name_text.get(), birthday_text)
        view_birth()
    except NameError:
        messagebox.showinfo("ERROR","PLEASE SELECT A RECORD")

#show all entries
def view_birth():
    global DICT_A
    DICT_A = {}
    list_box.delete(0, END)
    for idx,(id,name,bday) in enumerate(db.fetch()):
        idx = idx+1
        DICT_A[idx]=id
        display_record = idx,name,bday     
        list_box.insert(END,display_record)

#show only entries for today      
def today_view(): 
    list_box.delete(0, END)
    today_list,Indx=[],0
    for iD,name,date in db.fetch():
        if date == date_today:
            Indx+=1
            new_value=Indx, name, date
            list_box.insert(END,new_value )
            today_list.append(list(new_value))
    if  today_list == []:
        messagebox.showinfo("","YOU HAVE NO BIRTHDAY ENTRIES TODAY")
        view_birth()

#quit window
def client_exit():
      exit()

#clear input
def view_all():
    view_birth()
    if DICT_A == {}:
        messagebox.showinfo("YOU HAVE NOT ENTERED ANY BIRTHDAY","PLEASE ENTER A BIRTHDAY DETAIL")

def clear_item():
    name_entry.delete(0, END)

app=Tk()

#initializing the calendar
cal = DateEntry(app, width =12, selectmode='day', year=current_year, month=current_month, day=current_day, 
background='darkblue', foreground='white',font ="Arial 12", borderwidth=2, date_pattern ='dd/mm/yyyy')
cal.grid(row=0, column=3,sticky='w')

#widget 
name_text = StringVar()
name_label = Label(app, text = 'Name', font=('bold',14), pady = 5, padx=5)
name_label.grid(row = 0, column=0, sticky='w')
#text entry box
name_entry = Entry(app,textvariable=name_text)
name_entry.grid(row=0, column=1,sticky = 'w')

#widget for birthdate label
birthday_label = Label(app, text = 'Birth Date', font=('bold',14),padx =5)
birthday_label.grid(row = 0, column=2, sticky='w')

#listbox widget
list_box=Listbox(app, height=11, width=45, border=0)
list_box.grid(row=3, column=1, columnspan=2, rowspan=4, padx=2, pady=20)

#scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,column=3, columnspan =2 )
#set scrollbar to listbox
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

#bind select action
list_box.bind('<<ListboxSelect>>',select_item)
#bind dateentry
cal.bind("<<DateEntrySelected>>",kalenda)

#buttons
add_btn=Button(app, text='Add Birthday', width=11, command=addbirth)
add_btn.grid(row=2, column=0,padx=12, pady=20)

update_btn=Button(app, text='Update Birthday', width=11, command=update_birth)
update_btn.grid(row=2, column=1, pady=20)

delete_btn=Button(app, text='Delete Birthday', width=11, command=delete_birth)
delete_btn.grid(row=2, column=2, pady=20)

today_btn=Button(app, text='Birthdays Today', width=11, command=today_view)
today_btn.grid(row=2, column=3, pady=20)

view_all_btn=Button(app, text='View All', width=11, command=view_all)
view_all_btn.grid(row=8, column=1, pady =10)

exit_btn=Button(app, text='Exit', width=10, command=client_exit)
exit_btn.grid(row=8, column=2, pady=10)

#view birthday
today_view()

app.title('Crest') 
app.geometry('670x420')

app.mainloop()