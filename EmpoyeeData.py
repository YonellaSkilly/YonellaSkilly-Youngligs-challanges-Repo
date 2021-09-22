# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:35:14 2019

@author: stud38
"""
from tkinter import *
import sqlite3
class Db_connect:
    def insertRec(self):
        e =int(emp_id.get())
        f = firstname.get()
        l = lastname.get() 
        s = float(salary.get())
        conn =sqlite3.connect("EmployeeDb.db")
        c=conn.cursor()
        c.execute("INSERT INTO tblEmply1 VALUES(?,?,?,?)",(e,f,l,s,))
        conn.commit()
        conn.close()
        Label(root, text = "Record successfully inserted!!!").grid(row = 8, column = 0)
    def displayRec(self):
        s = search.get()
        conn =sqlite3.connect("EmployeeDb.db")
        c=conn.cursor()
        c.execute("SELECT * FROM tblEmply1 WHERE emp_id = ?",(s,))
        res = c.fetchall()
        for y in res:
            emp_id.set(y[0])
            firstname.set(y[1])
            lastname.set(y[2])
            salary.set(y[3])   
            
        conn.commit()
        conn.close()
 
    def clear(self):
        emp_id.set('')
        firstname.set('')
        lastname.set('')
        salary.set('')
        
        conn.commit()
        conn.close()

    def update(self):
        e =int(emp_id.get())
        f = firstname.get()
        l = lastname.get() 
        s = float(salary.get())
        
        conn =sqlite3.connect("EmployeeDb.db")
        c=conn.cursor()
        c.execute("UPDATE tblEmply1 SET  Firstname = ? and Lastname = ? and Salary = ? WHERE emp_id = ?",(f,l,s,e,))
        conn.commit()
        conn.close()
        
    def deleteRec(self):  
         e =int(emp_id.get())
         f = firstname.get()
         l = lastname.get() 
         s = float(salary.get())
        
         conn =sqlite3.connect("EmployeeDb.db")
         c=conn.cursor()
         c.execute("DELETE FROM tbkEmply1  WHERE emp_id = ?",(e,))
         conn.commit()
         conn.close()
         d = Db_connect()
         d.clear(
                 )

#conn = sqlite3.connect('EmployeeDb.db')
#c = conn.cursor()
#query = """ CREATE TABlE   tblEmply1( Emp_ID int PRIMARY KEY,
 #                        Firstname text,
 #                       Lastname text,
  #                      salary decimal) """
#c.execute(query)
#conn.commit()
#conn.close()
root = Tk()
emp_id = StringVar()
search = StringVar()
firstname = StringVar()
lastname = StringVar()
salary = StringVar()


x = Db_connect()
Label(root, text = 'Empoyee Form').grid(columnspan = 5)
Entry(root, textvariable = search).grid(row = 1, column = 0)
Button(root, text ='Search', command = lambda: x.displayRec()).grid(row = 1, column = 1) 
Label(root, text = 'Record').grid(columnspan = 5)
Label(root, text = 'employee ID').grid(row = 3 ,column = 0)
Entry(root, textvariable = emp_id).grid(row = 3, column = 1)
Label(root, text = 'Firstname').grid(row = 4 ,column = 0)
Entry(root, textvariable = firstname).grid(row = 4, column = 1)
Label(root, text = 'Lastname').grid(row = 5 ,column = 0)
Entry(root, textvariable = lastname).grid(row = 5, column = 1)
Label(root, text = 'Salary').grid(row = 6 ,column = 0)
Entry(root, textvariable = salary).grid(row = 6, column = 1)
Button(root, text ='Insert', command = lambda:x.insertRec()).grid(row = 7, column = 0) 
Button(root, text ='Update',command = lambda:x.update()).grid(row = 7, column = 1) 
Button(root, text ='Delete', command = lambda:x.deleteRec()).grid(row = 7, column = 2) 
Button(root, text ='Clear', command = lambda:x.clear()).grid(row = 7, column = 3) 

root.mainloop()
