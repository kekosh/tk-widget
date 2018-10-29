import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		
		#クラスを使用している場合はmasterオブジェクトに対してタイトルを設定する。
		self.master.title("grid-layout")
		self.createWidget()

	# def clicked(self):
		# #messagebox.<windowType>([title],[message]))
		# messagebox.showinfo("message window","Click!!")
		
	def clicked(self,event=None):
		#messagebox.<windowType>([title],[message]))
		#選択したボタンを判別する場合(Dialogresult)は呼び出しを直接変数に入れる
		#[Bug]messageboxを表示するとボタンが押下後もへこんだままとなる
		#dialigresult = messagebox.showinfo("message window","Click!!")
		#print(dialigresult)
		
		if event is None:
			print("no event")
		else:
			if event.widget["text"]=="click_after":
				event.widget["text"] = "click_before"
			else:
				event.widget["text"] = "click_after"

	def createWidget(self):
		#自クラス内のクラスメソッドを使用する際は「self.<method>」で記載する
		
		lb = tk.Listbox(selectmode=tk.MULTIPLE)
		lb.insert(1,"TOKYO")
		lb.insert(2,"KANAGAWA")
		lb.insert(3,"OSAKA")
		lb.insert(4,"HYOGO")
		lb.grid(row=1,column=0,columnspan=4,pady=5)		
		
		## command
		#btn_click = tk.Button(text="Click",command=self.clicked)
		
		##bind
		btn_click = tk.Button(text="click_before")
		btn_click.bind("<Button-1>",self.clicked)
		
		##lambda pattern [lambda arg: method(arg)]
		#→btn_click.bind("<Button-1>",lambda event:self.clicked(event))

		btn_click.grid(row=0,column=0,ipadx=50)
		
		btn_quit = tk.Button(text="Quit",command=quit)
		btn_quit.grid(row=0,column=1,padx=5,ipadx=20)
		


app = Application()
app.mainloop()	