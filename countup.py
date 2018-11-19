import tkinter as tk
from tkinter import messagebox
import os
import json
import datetime
import collections as cl

#---------------------------------
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()
        self.create_widgets(master)

    def create_widgets(self, master):
        #sample-start
        # self.bk = tk.Button(text="Button")
        # self.bk.pack()
        #sample-end

        self.frame = tk.Frame(master, width="150", height="100", relief=tk.SOLID, borderwidth="1")
        self.frame.propagate(False)
        self.frame.grid(row=0)



    def load_json(self):
        data = load.json()

#---------------------------------


#---------------------------------
root = tk.Tk()
root.title("count up")
root.geometry("300x200")
app = Application(master=root)
app.mainloop()