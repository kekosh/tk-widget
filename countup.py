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

            #load Test
            #print(json.dumps(json_data, indent = 4))
            self.create_widgets(master, json_data)


    def get_filepath(self, os_name):
        dirkey = "\\" if os_name == "nt" else "/"
        return "{0}{1}data.json".format(os.getcwd(),dirkey)


    def create_widgets(self, master, json_data):
        odict = cl.OrderedDict()
        odict = json_data["data"]
        for value in odict.values():
            self.frame = tk.Frame(master, width="780",relief=tk.SOLID, borderwidth="1")
            self.frame.propagate(False)
            self.frame.pack(padx=5, pady=10, fill=tk.X)

            self.label = tk.Label(self.frame, text=str(value["count"]))
            self.label.grid(row=0, column=0, padx=20)
            self.entry = tk.Entry(self.frame, width=60, borderwidth="1", relief=tk.SOLID)
            self.entry.grid(row=0, column=1, padx=10)
            self.btn = tk.Button(self.frame, width=20, text="Up")
            self.btn.grid(row=0, column=2)


#---------------------------------


#---------------------------------
root = tk.Tk()
root.title("count up")
root.geometry("800x400")
root.resizable(1,1) #0:unresizable 1: resizable
app = Application(master=root)
app.mainloop()