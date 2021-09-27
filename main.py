#imports
from tkinter import *

from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Databases
# Create a databases or connect to one
conn = sqlite3.connect('address_book1.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute(""" CREATE TABLE addresses(
        ref_no integer,
        company_name text,
        med_type text,
        med_name text,
        lot_no integer,
        issue_date integer,
        expiry_date integer,
        dosage integer,
        tab_price integer,
        precs_warning text,
        uses text,
        side_effects text
) """)
'''

root = Toplevel()
root.title("Pharmacy Management System")
root.iconbitmap('pill.png')
root.geometry("1280x680")

# top title
title = Label(root, text="Pharmacy Management System", bg="black", fg="red", font=("Bradley Hand ITC", 50, "bold"))
title.pack(side=TOP, fill=X, padx=10, pady=10)

mainloop()