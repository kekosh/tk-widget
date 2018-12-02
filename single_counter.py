import os
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets(master)

    def create_widgets(self, master):
        self.OuterFrame = tk.Frame(master, relief=tk.SOLID, borderwidth="1")
        self.OuterFrame.pack(padx=5, pady=10, fill=tk.X)

        self.list_Frame = tk.Frame(master, relief=tk.SOLID, borderwidth="1")
        self.list_Frame.pack(padx=5, pady=10, fill=tk.X)

        var = value=["TEST1","TEST2","TEST3"])
        self.data_listbox = tk.Listbox(self.list_Frame, var)
        self.data_listbox.pack(fill=tk.X)


        self.input_frame =tk.Frame(self.OuterFrame, relief=tk.SOLID, borderwidth="1")
        self.input_frame.pack(fill=tk.X)

        self.count_entry = tk.Entry(self.input_frame, width=30, borderwidth="1", relief=tk.SOLID)
        self.count_entry.grid(row=0,column=0)



root = tk.Tk()
root.title("single_counter")
root.geometry("500x400")
root.resizable(1,1)
app = Application(master=root)
app.mainloop()
