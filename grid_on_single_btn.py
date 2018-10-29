import tkinter as tk
from tkinter import messagebox

#引数にtk.Frameは必須
class app(tk.Frame):
	#コンストラクタ
	#master は親Widgetを指す
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		
		self.grid()
		self.createWidgets()
	
	def clicked(self,event):
		messagebox.showinfo("info","Btn is Clicked")
		return
		
	def createWidgets(self):
		plane_btn = tk.Button(text="Button")
		plane_btn.bind("<Button-1>",self.clicked)
		plane_btn.grid(row=1,column=1)
		
		quitbtn = tk.Button(text="Quit",command=quit)
		quitbtn.grid(row=1,column=2)

app = app()
app.master.title("Sample App")
app.mainloop()