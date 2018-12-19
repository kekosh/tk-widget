import tkinter as tk

root = tk.Tk()

#フレームは一番外側のwidgetなので、親は「root」
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

#以下はframe1配下にネストさせる
lbl = tk.Label(frame1, text="frame1配下のラベル")
lbl.grid(row=0, column=0)
btn = tk.Button(frame1, text="Button1")
btn.grid(row=0, column=1)
frame1.pack()

#以下はframe2配下にネストさせる
lbl2 = tk.Label(frame2, text="frame2配下のラベル")
lbl2.grid(row=0, column=0)
btn2 = tk.Button(frame2, text="Button2")
btn2.grid(row=0, column=1)
frame2.pack()

root.mainloop()