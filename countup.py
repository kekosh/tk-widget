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
            self.frame = tk.Frame(master, relief=tk.SOLID, borderwidth="1")
            self.frame.propagate(False)
            self.frame.pack(padx=5, pady=10, fill=tk.X)

            self.header_lbl_1 = tk.Label(self.frame, text="count")
            self.header_lbl_1.grid(row=0, column=0)
            self.label = tk.Label(self.frame, text=str(value["count"]))
            self.label.grid(row=1, column=0, padx=20)

            self.header_lbl_3 = tk.Label(self.frame, text="Up/Down")
            self.header_lbl_3.grid(row=0, column=1, columnspan=2)
            self.up_btn = tk.Button(self.frame, width=5, text="↑")
            self.up_btn.grid(row=1, column=1)
            self.down_btn = tk.Button(self.frame, width=5, text="↓")
            self.down_btn.grid(row=1, column=2)

            self.header_lbl_2 = tk.Label(self.frame, text="memo")
            self.header_lbl_2.grid(row=0, column=3)
            self.entry = tk.Entry(self.frame, width=40, borderwidth="1", relief=tk.SOLID)
            self.entry.grid(row=1, column=3, padx=10)

        self.fix_frame = tk.Frame(master, relief=tk.SOLID, borderwidth="1")
        #frame's ”propagation" property is inherited first frame definition
        #self.fix_frame.propagate(False)
        self.fix_frame.pack(padx=5, pady=10, fill=tk.X)

        self.quit_btn = tk.Button(self.fix_frame, text="quit", command=lambda:master.destroy())
        self.quit_btn.pack()
#---------------------------------


#---------------------------------
root = tk.Tk()
root.title("count up")
root.geometry("550x400")
root.resizable(1,1) #0:unresizable 1: resizable
app = Application(master=root)
app.mainloop()