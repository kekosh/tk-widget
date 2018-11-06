import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("count-up")
root.geometry("300x200")

frame1 = tk.Frame()

lb = tk.Label(text = 0)
lb.pack()

def click():
    counter = int(lb.cget("text")) + 1
    lb["text"]= counter

btn = tk.Button(text="Click", command=click)
btn.pack()
frame1.pack()

frame2 = tk.Frame()
ent = tk.Entry()
ent.grid(row=0,column=1)

def click_2():
    input_ent = ent.cget("text")
    messagebox.showinfo(title="information", message=input_ent)


btn2 = tk.Button(text="Click_2", command=click_2)
btn2.pack()
frame2.grid()



root.mainloop()