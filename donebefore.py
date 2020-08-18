import os,ast
from tkinter import *
from datetime import datetime


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("BIRTHDAY REMINDER APP")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        label = Label(
        text="BIRTHDAY REMINDER APP",
        foreground="blue", 
        background="white")
        label.place(x=110, y=30)

        label = Label(
        text="CREATE AND MANAGE YOUR BIRTHDAYS, KEEP THE DATES",
        foreground="blue", 
        background="white")
        label.place(x=10, y=80)


        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=250, y=300)

        AddButton = Button(self, text="Add a new birthday",command = self.addbirth)
        AddButton.place(x=30,y=170)

        EditButton = Button(self, text="Update Birthday",command = self.edit_birth)
        EditButton.place(x=250,y=170)

        viewButton=Button(self, text='View all Birthdays',command=self.viewbirth)
        viewButton.place(x=250, y=230)

        SearchButton = Button(self, text="Birthdays today", command=self.today_view)
        SearchButton.place(x=30, y=230)

        deleteButton = Button(self, text = "Delete Birthday", command = self.delete_birth)
        deleteButton.place(x=30, y=300)
       

    def client_exit(self):
      exit()

    
    # def addbirth(self):
    #   if os.path.isfile('./birth_dict.txt'):
    #     with open('birth_dict.txt','r+') as f:
    #       s=f.read()
    #       birth_dict=ast.literal_eval(s)

    #   else:
    #     birth_dict={}

    #   name= input('Enter a name or press enter to exit: ')
    #   while name != '':

    #     if name not in birth_dict:
    #       val=input('Enter the birthday in this format,dd/mm/yyyy: ')
    #       birth_dict[name]=val
    #       print('Birthday successfully added')

    #       f= open("birth_dict.txt", "w+")
    #       f.write(str(birth_dict))
    #       f.close()

    #     elif name in birth_dict:
    #       print('Sorry name already exists,please use a different name','\n')

    #     opinion = input('Do you want to add another record?, yes/no: ')
    #     if opinion.lower() == 'yes':
    #       name=input('Enter a name or press enter to exit: ')

    #     else:
    #       break

    #   return 'Thank you for using this service'

    # def edit_birth(self):
    #   with open('birth_dict.txt','r+') as f:
    #     s=f.read()
    #     birth_dict=ast.literal_eval(s)

    #   user=input('Do you wish to update a record? yes/no: ')
    #   while user.lower() == 'yes':
    #     user2=input("Enter 'date' to change a birthdate or 'name' to change a name: ")

    #     if user2.lower()== 'date':
    #       request=input("Enter the name: ")

    #       while True:
    #         response=input("Enter a new date in this format, dd/mm/yyyy: ")
    #         if response.isalpha() or response.isdecimal():
    #           print('Enter a correct birthday')

    #         else: 
    #           birth_dict[request]=response
    #           print('The database has been updated')
    #           break

    #     elif user2.lower() == 'name':

    #       username= input("Enter the name: ")
    #       if username in birth_dict:
    #         print("Is this the record you want to update?, ",username,'  ',birth_dict[username])
    #         opinion = input('Enter yes/no: ')

    #         if opinion.lower() == 'yes':
    #           del birth_dict[username]

    #           new_name=input('Enter the new name: ')
    #           while True:
    #             new_date=input('Enter the new birthdate in this format, dd/mm/yyyy: ')
    #             if new_date.isalpha() or new_date.isdecimal():
    #               print('You have entered a wrong birthday')

    #             else:
    #               birth_dict[new_name]=new_date
    #               print("Database Updated")
    #               break

    #         else:
    #           print('Please check the name and try again')


    #       elif username not in birth_dict:
    #           print('The record you are seeking to update does not exist, Please check again')
              
    #     else:
    #       print("You have entered a wrong input")

    #     user=input('Do you want to make any other update? yes/no: ')

    #   f = open("birth_dict.txt","w+")
    #   f.write(str(birth_dict))
    #   f.close()

    #   print()
    #   return('Thank you for using this service')

    # def viewbirth(self):

    #   with open('birth_dict.txt','r+') as f:
    #     s=f.read()
    #     birth_dict = ast.literal_eval(s)
        
    #   print("   BIRTHDAY RECORD")
     
    #   print("{:<12}{:<12}".format("Name","Birthday"))
    #   for key,value in birth_dict.items():
    #     name=key
    #     Birthday=value
    #     print("{:<12}{:<12}".format(name,Birthday))

    # def today_view(self):
    #   with open('birth_dict.txt','r+')as f:
    #     s=f.read()
    #     birth_dict=ast.literal_eval(s)
        
    #   todai=datetime.today()
    #   date_today=datetime.strftime(todai,'%d/%m/%Y')
      
    #   if date_today in birth_dict.values():
        
    #     formatt="{:<19}{:<10}"
    #     print('BIRTHDAYS TODAY,',date_today)
    #     print(formatt.format('NAME','BIRTHDAY'))

    #     for key,value in birth_dict.items():
    #       if date_today == value:
    #         name,Birthday=key,value
    #         print(formatt.format(name,Birthday))

    #   else:
    #     print('You have no birthdays for today',date_today)

    # def delete_birth(self):
    #   with open('birth_dict.txt','r+') as f:
    #     s=f.read()
    #     birth_dict = ast.literal_eval(s)

    #   person_name=input('Enter the name for the birthday you want to delete: ')
    #   while person_name != "":

    #     if person_name in birth_dict:

    #       print('Is this the record you want to delete?,  ',person_name,birth_dict[person_name])

    #       answer=input('Enter y/n: ')
    #       if answer.lower() == 'y':
    #         del birth_dict[person_name]
    #         print('Birthday successfully deleted')

    #         f=open('birth_dict.txt','w+')
    #         f.write(str(birth_dict))
    #         f.close()

    #       elif answer.lower() == 'n':
    #         print('Check the name again')

    #       else:
    #         print('You have entered a wrong input')

    #     elif person_name not in birth_dict:
    #       print('Sorry the name does not exist')

    #     choice=input('Do you wish to delete another birthday? Enter y to continue: ')
    #     if choice.lower() == 'y':
    #       person_name =input('Enter the name for the birthday to be deleted: ')

    #     else:
    #       break

def addbirth(self):
      if os.path.isfile('./birth_dict.txt'):
        with open('birth_dict.txt','r+') as f:
          s=f.read()
          birth_dict=ast.literal_eval(s)

      else:
        birth_dict={}

      name= input('Enter a name or press enter to exit: ')
      while name != '':

        if name not in birth_dict:
          val=input('Enter the birthday in this format,dd/mm/yyyy: ')
          birth_dict[name]=val
          print('Birthday successfully added')

          f= open("birth_dict.txt", "w+")
          f.write(str(birth_dict))
          f.close()

        elif name in birth_dict:
          print('Sorry name already exists,please use a different name','\n')

        opinion = input('Do you want to add another record?, yes/no: ')
        if opinion.lower() == 'yes':
          name=input('Enter a name or press enter to exit: ')

        else:
          break

      return 'Thank you for using this service'

    def edit_birth(self):
      with open('birth_dict.txt','r+') as f:
        s=f.read()
        birth_dict=ast.literal_eval(s)

      user=input('Do you wish to update a record? yes/no: ')
      while user.lower() == 'yes':
        user2=input("Enter 'date' to change a birthdate or 'name' to change a name: ")

        if user2.lower()== 'date':
          request=input("Enter the name: ")

          while True:
            response=input("Enter a new date in this format, dd/mm/yyyy: ")
            if response.isalpha() or response.isdecimal():
              print('Enter a correct birthday')

            else: 
              birth_dict[request]=response
              print('The database has been updated')
              break

        elif user2.lower() == 'name':

          username= input("Enter the name: ")
          if username in birth_dict:
            print("Is this the record you want to update?, ",username,'  ',birth_dict[username])
            opinion = input('Enter yes/no: ')

            if opinion.lower() == 'yes':
              del birth_dict[username]

              new_name=input('Enter the new name: ')
              while True:
                new_date=input('Enter the new birthdate in this format, dd/mm/yyyy: ')
                if new_date.isalpha() or new_date.isdecimal():
                  print('You have entered a wrong birthday')

                else:
                  birth_dict[new_name]=new_date
                  print("Database Updated")
                  break

            else:
              print('Please check the name and try again')


          elif username not in birth_dict:
              print('The record you are seeking to update does not exist, Please check again')
              
        else:
          print("You have entered a wrong input")

        user=input('Do you want to make any other update? yes/no: ')

      f = open("birth_dict.txt","w+")
      f.write(str(birth_dict))
      f.close()

      print()
      return('Thank you for using this service')

    def viewbirth(self):

      with open('birth_dict.txt','r+') as f:
        s=f.read()
        birth_dict = ast.literal_eval(s)
        
      print("   BIRTHDAY RECORD")
     
      print("{:<12}{:<12}".format("Name","Birthday"))
      for key,value in birth_dict.items():
        name=key
        Birthday=value
        print("{:<12}{:<12}".format(name,Birthday))

    def today_view(self):
      with open('birth_dict.txt','r+')as f:
        s=f.read()
        birth_dict=ast.literal_eval(s)
        
      todai=datetime.today()
      date_today=datetime.strftime(todai,'%d/%m/%Y')
      
      if date_today in birth_dict.values():
        
        formatt="{:<19}{:<10}"
        print('BIRTHDAYS TODAY,',date_today)
        print(formatt.format('NAME','BIRTHDAY'))

        for key,value in birth_dict.items():
          if date_today == value:
            name,Birthday=key,value
            print(formatt.format(name,Birthday))

      else:
        print('You have no birthdays for today',date_today)

    def delete_birth(self):
      with open('birth_dict.txt','r+') as f:
        s=f.read()
        birth_dict = ast.literal_eval(s)

      person_name=input('Enter the name for the birthday you want to delete: ')
      while person_name != "":

        if person_name in birth_dict:

          print('Is this the record you want to delete?,  ',person_name,birth_dict[person_name])

          answer=input('Enter y/n: ')
          if answer.lower() == 'y':
            del birth_dict[person_name]
            print('Birthday successfully deleted')

            f=open('birth_dict.txt','w+')
            f.write(str(birth_dict))
            f.close()

          elif answer.lower() == 'n':
            print('Check the name again')

          else:
            print('You have entered a wrong input')

        elif person_name not in birth_dict:
          print('Sorry the name does not exist')

        choice=input('Do you wish to delete another birthday? Enter y to continue: ')
        if choice.lower() == 'y':
          person_name =input('Enter the name for the birthday to be deleted: ')

        else:
          break







      
        



              







      





    


    

    
    



# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("500x400")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  