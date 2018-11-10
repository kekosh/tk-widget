import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("count-up")
root.geometry("300x200")

# <- Frame1 ->
frame1 = tk.Frame(root, width="3c", height="5c")
frame1.propagate(False)

lb = tk.Label(frame1, text=0)
lb.pack()

def click():
    counter = int(lb.cget("text")) + 1
    lb["text"]= counter

btn = tk.Button(frame1, text="Click", command=click)
btn.pack()
frame1.grid(row=0, column=0)

#<- Frame2 ->
frame2 = tk.Frame(root, width="3c", height="5c")
frame2.propagate(False)
ent = tk.Entry(frame2)
ent.pack()

def click_2():
    '''　Entry-Widgetへの入力値はget()メソッドで取得する。　'''
    # if ent.get() == "":
        # input_ent = "Blank!"
    # else:
        # input_ent = ent.get()
    
    ''' if文の1行記述[変数 = Trueの場合の処理　if 条件式 else Flaseの場合の処理]    '''
    input_ent = ent.get() if ent.get() != "" else "BLANK!!"
    
    messagebox.showinfo(title="information", message=input_ent)


btn2 = tk.Button(frame2, text="Click_2", command=click_2)
btn2.pack()

import tkinter.scrolledtext as tkscr
scrtxt = tkscr.ScrolledText(frame2)
scrtxt.pack()

frame2.grid(row=0, column=1)

root.mainloop()