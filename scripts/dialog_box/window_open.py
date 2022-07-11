from tkinter import ttk
import mysql.connector
import tkinter as tk
from tkinter import *
from scripts.project_scripts.twitter import run
    
def show():
    conn = mysql.connector.connect(user='root', 
                                       password="aishwary2001??", 
                                       host='localhost',
                                       port=3306,
                                       database='data_scrapper',
                                       )
    curr=conn.cursor()
    curr.execute("SELECT * FROM scrapped_data")
    rows=curr.fetchall()
    
    
    data_box=tk.Tk()
    data_box.geometry("1050x700")
    data_box.title(string="DATA")
    
    
    global i
    i=0 
    for student in rows : 
        for j in range(len(student)):
            e = Label(data_box,height=2,width=10, text=student[j],
                relief='ridge', anchor="w")  
            e.grid(row=i, column=j)
            # scrollbar = ttk.Scrollbar(e, orient='vertical', command=e.yview)
            # scrollbar.grid(row=0, column=1, sticky=tk.NS)
            # e['yscrollcommand'] = scrollbar.set 
        i=i+1
        
    # scroll_bar = ttk.Scrollbar(data_box)
    # scroll_bar.pack(side=tk.RIGHT)
    # data_box.config(yscrollcommand=scroll_bar.set)
    # scroll_bar.config(command=data_box.yview)   
    tk.Button(data_box,
                   text = "OK",
                   command = data_box.destroy,
                   width=10
                   ).place(x=900, y=600)
    
def fetch():
    run(True)


def open_box():
    top = tk.Tk()
    top.title(string="Data Scrap")
    top.geometry("300x300")
    e1=tk.Label(top, 
            text="No. of Tweets :"
            )
    e1.place(relx = 0.11,
                 rely = 0.4
            )
    B1=tk.Button(top,
                text = "Fetch Data",
                command=fetch
                ).place(x=150,y=200)
    B2=tk.Button(top,
              text="Show Data",
              command=show
              ).place(x=80,y=200)
    
    top.mainloop()