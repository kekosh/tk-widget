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
        #sample-start
        # self.bk = tk.Button(text="Button")
        # self.bk.pack()
        #sample-end
        odict = cl.OrderedDict()
        odict = json_data["data"]
        for value in odict.values():
            print(value)
            self.frame = tk.Frame(master, width="780", height="80",relief=tk.SOLID, borderwidth="1")
            self.frame.propagate(False)
            self.frame.pack(pady = 10)

            self.label = tk.Label(self.frame, text=str(value["count"]))
            self.label.pack(side="left")
#---------------------------------


#---------------------------------
root = tk.Tk()
root.title("count up")
root.geometry("800x400")
root.resizable(0,1)
app = Application(master=root)
app.mainloop()