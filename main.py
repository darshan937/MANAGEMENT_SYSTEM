#imports
from tkinter import *
from PIL import Image,ImageTk
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

# logo image
img1 = Image.open("logo.png")
img1 = img1.resize((80, 80), Image.ANTIALIAS)
photoimg1 = ImageTk.PhotoImage(img1)
btn = Button(root, image=photoimg1, borderwidth=0)
btn.place(x=40, y=14)

# dataframe
DataFrame = Frame(root, bd=10, bg="black", relief=RIDGE, padx=20, pady=20)
DataFrame.place(x=0, y=110, width=1280, height=420)

# dataframe left
DataFrameLeft = LabelFrame(DataFrame, bd=10, bg="lightblue", relief=RIDGE, padx=20, text="Medicine Information",
                           fg="black", font=("arial", 16, "bold"))
DataFrameLeft.place(x=0, y=5, width=900, height=355)

# images in left dataframe
img2 = Image.open("tab.png")
img2 = img2.resize((100, 80), Image.ANTIALIAS)
photoimg2 = ImageTk.PhotoImage(img2)
btn = Button(root, image=photoimg2, borderwidth=0)
btn.place(x=800, y=177)

img3 = Image.open("doc.png")
img3 = img3.resize((430, 200), Image.ANTIALIAS)
photoimg3 = ImageTk.PhotoImage(img3)
btn = Button(root, image=photoimg3, borderwidth=0)
btn.place(x=470, y=270)

mainloop()