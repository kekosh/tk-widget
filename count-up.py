import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)

		self.master.title("countup")
		self.create()

	def create(self):
		lb = tk.Label(text=0)
		lb.pack()

		btn = tk.Button(text="CountUp")
		btn.pack()


App = App()
App.mainloop()
