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
        data_file = self.get_filepath(os.name)

        with open(data_file,"r") as f:
            json_data = json.load(f)
            
        self.create_widgets(master,json_data)


    def get_filepath(self, os_name):
        dirkey = "\\" if os_name == "nt" else "/"
        return "{0}{1}data.json".format(os.getcwd(),dirkey)


    def create_widgets(self, master, json_data):
        #sample-start
        # self.bk = tk.Button(text="Button")
        # self.bk.pack()
        #sample-end

        self.frame = tk.Frame(master, width="800", height="80", relief=tk.SOLID, borderwidth="1")
        self.frame.propagate(False)
        self.frame.grid(row=0)





    def load_json(self):
        data = load.json()

#---------------------------------


#---------------------------------
root = tk.Tk()
root.title("count up")
root.geometry("800x400")
root.resizable(0,1)
app = Application(master=root)
app.mainloop()