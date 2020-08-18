import sqlite3
from datetime import datetime
from tkinter import messagebox

toda=datetime.today()
date_today=datetime.strftime(toda,'%d/%m/%Y')



def check(val):                             #function for performing checks on date values inputted for the dictionary
    date_year=datetime.today()
    year=datetime.strftime(date_year,'%Y')
    while True:                                     #continuous loop while condition is not met
    
        net=val.split('/')                                                 #split string value in 'new_date' at the '/' character,assign new list value to 'net'

        if len(net[0]) > 2:                                                     #check that 1st value is not more than 2 string
            messagebox.showerror('Wrong input', "Please enter the date in this format, dd/mm/yyyy")   
                
        else:                                                               #if the 1st condition checks false then do these
            if len(net[0]) == 1:                                            #check that 1st value in net is 1 if true    
                net[0]='0'+net[0]                                           #do this

            if len(net[1]) == 1:                                            #check that 2nd value in net is 1 if true
                net[1]='0'+net[1]
                
            if net[2] != year:
                net[2] = year

            renew='/'.join(net)                                          #output 'record updated'
            break                                                           #exit the while loop initiated earlier
            
    return renew                                                        #return the values in 'ur_dict' 



class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY,name CHARACTER(20) NOT NULL, birthday date)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT name,birthday FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self,name, birthday):
        self.cur.execute("INSERT INTO parts VALUES(NULL, ?, ?)", (name, birthday))
        check(birthday)
        self.conn.commit()

    def removeall(self):
        self.cur.execute("DELETE FROM parts;")
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id = ?",(id,))
        self.conn.commit()

    def update(self,id, name, birthday):
        self.cur.execute("UPDATE parts SET name = ?, birthday = ? WHERE id = ?" , (name,birthday,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()



