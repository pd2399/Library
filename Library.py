import pandas as pd
import numpy as np


class stock:
    def __init__(self):
        # Initialize the class
        pass
        
    def add(self,bname, aname, year, genre):
        # Add book to records and return book id
        self.records = pd.read_csv("records.csv",index_col='Id')
        self.bname = bname
        self.aname = aname
        self.year = year
        self.genre = genre
        self.new_row = pd.DataFrame({'Book Name':[bname],'Author Name':[aname],'Year of Publication':[year],'Genre':[genre],'Available':['Yes']})
        self.records = self.records.append(self.new_row,ignore_index=True)
        print(self.records.iloc[-1:])
        self.records.to_csv('records.csv',index_label='Id')
    
    def delete(self,bname,id):
        # Delete book from records
        self.records = pd.read_csv("records.csv",index_col='Id')
        self.bname = bname
        self.id = id
        self.records = self.records.drop(self.id)
        self.records.to_csv('records.csv')

    def ispresent(self,bname):
        # Check if a book is available
        self.records = pd.read_csv("records.csv",index_col='Id')
        self.bname = bname
        print(self.records.loc[(self.records['Book Name'] == self.bname)])

    def show_stock(self):
        # Show all the available stock
        self.records = pd.read_csv("records.csv",index_col='Id')
        print(self.records)


class member:
    def __init__(self):
        # Initialize the class
        pass

    def add(self, fname, lname, yob, number):
        # Add member to records and return member id
        self.members = pd.read_csv("members.csv",index_col='Id')
        self.fname = fname
        self.lname = lname
        self.yob = yob
        self.number = number
        self.new_row = pd.DataFrame({'First Name':[fname],'Last Name':[lname],'Year of Birth':[yob],'Contact Number':[number]})
        self.members = self.members.append(self.new_row,ignore_index=True)
        print(self.members.iloc[-1:])
        self.members.to_csv('members.csv',index_label='Id')

    def delete(self, fname, lname, id):
        # Delete member from records
        self.members = pd.read_csv("members.csv",index_col='Id')
        self.fname = fname
        self.lname = lname
        self.id = id
        self.members = self.members.drop(int(self.id))
        self.members.to_csv('members.csv')

    def book_issue(self, bname,id):
        # Issue a book to the user and remove it from available stock
        self.issued = pd.read_csv("issued.csv")
        self.records = pd.read_csv("records.csv",index_col='Id')
        self.bname = bname
        self.id = id
        self.new_row = pd.DataFrame({'Id':[id],'Book Name':[bname],'Date':[datetime.now()]})
        self.issued = self.issued.append(self.new_row,ignore_index=True)
        print(self.issued.iloc[-1:])
        self.records.loc[self.records['Book Name'] == self.bname,'Available'] = 'No'
        self.records.to_csv('records.csv',index_label='Id')
        self.issued.to_csv('issued.csv',index = False)

    def book_return(self, bname, id):
        # Take the issued book back and add it back to available stock
        self.issued = pd.read_csv("issued.csv",index_col='Id')
        self.records = pd.read_csv("records.csv",index_col='Id')
        self.bname = bname
        self.id = id
        self.issued = self.issued.drop(self.id)
        self.records.loc[self.records['Book Name'] == self.bname,'Available'] = 'Yes'
        self.records.to_csv('records.csv',index_label='Id')
        self.issued.to_csv('issued.csv')


def switch():
    while True:
        i = int(input('1. Issue a book\n2.Return a book\n3.Add a new member\n4.Add a new book\n5.Delete a member\n6.Delete a book\n7.Check book availability\n8.See stock.\n9.Logout\n'))
        if i == 1:
            # Take book name and id to issue a book
            bname = input('Enter name of book ')
            bid = input('Enter book id ')
            issue = member()
            issue.book_issue(bname,bid)

        elif i == 2:
            # Take book name and id to return the book
            bname = input('Enter name of book ')
            id = int(input('Enter book id '))
            breturn = member()
            breturn.book_return(bname,id)

        elif i == 3:
            # Take first and last name, yob, and contact number to add member to records
            fname = input('Enter first name of the member ')
            lname = input('Enter last name of member ')
            yob = input('Enter their year of birth ')
            no = input('Enter their contact number ')
            madd = member()
            madd.add(fname,lname,yob,no)

        elif i == 4:
            # Take book name, author name, year of publication, and the genre of book to add it to records
            bname = input('Enter name of book ')
            aname = input('Enter name of author ')
            yop = input('Enter their year of publication ')
            genre = input('Enter the genre of book ')
            badd = stock()
            badd.add(bname,aname,yop,genre)

        elif i == 5:
            # Take first and last name, and id to delete member from records
            bname = input('Enter first name of member ')
            lname = input('Enter last name of member ')
            id = input('Enter member id ')
            mdelete = member()
            mdelete.delete(bname,lname,id)

        elif i == 6:
            # Take book name, author name, and book id to delete it from records
            bname = input('Enter name of book ')
            id = int(input('Enter book id '))
            bdelete = stock()
            bdelete.delete(bname,id)

        elif i == 7:
            # Take book name to check if the book is present/available
            bname = input('Enter name of book ')
            ask = stock()
            ask.ispresent(bname)

        elif i == 8:
            # Show the entire stock
            show = stock()
            show.show_stock()

        elif i == 9:
            # Logout
            print('Have a nice day!')
            return False


def login(uname, password):
    # Login function
    if uname == 'pd' and password == '123456789':
        print('Access Granted!')
        print('Welcome to the library!')
        return True
    

def work():
    # Function that actually does the work
    while True:
        uname = input("Enter username: ")
        password = input("Enter password: ")
        if login(uname,password):
            switch()
            return False
        else:
            print('Access Denied!\nEnter correct Username and Password')


work()   # Calling the work function