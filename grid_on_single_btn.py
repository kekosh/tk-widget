import tkinter as tk

#引数にtk.Frameは必須
class app(tk.Frame):
	#コンストラクタ
	#master は親Widgetを指す
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		
		self.grid()
		self.createWidgets()
	
	def createWidgets(self):
		quitbtn = tk.Button(text="Quit",command=quit)
		quitbtn.grid()

app = app()
app.master.title("Sample App")
app.mainloop()