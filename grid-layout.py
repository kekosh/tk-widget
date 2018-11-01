import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		
		#クラスを使用している場合はmasterオブジェクトに対してタイトルを設定する。
		self.master.title("grid-layout")
		self.createWidget()

	def clicked_by_command(self,arg):
		pass
		# #messagebox.<windowType>([title],[message]))
		dialogresult = messagebox.showinfo("message window","Click!!")
		
		if dialogresult:
			pass
			print(arg)
	def clicked_by_bind(self,event=None):
	
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
		#自クラス内の別メソッドを使用する際は「self.<method>」で記載する
		lb = tk.Listbox(selectmode=tk.MULTIPLE)
		lb.insert(1,"TOKYO")
		lb.insert(2,"KANAGAWA")
		lb.insert(3,"OSAKA")
		lb.insert(4,"HYOGO")
		lb.grid(row=1,column=0,columnspan=4,pady=5)		
		
		## ver.command
		# Buttonウィジェットのcommandで呼び出すメソッドに引数を渡す場合は、lambda式を使用する必要がある。
		#　lambda式を使わずにcommnadに引数つきの関数を渡すと、widget描画時に実行されてしまう。
		btn_click = tk.Button(text="Click",
			command=lambda:self.clicked_by_command("push by command option"))
		
		## ver.bind
		# btn_click = tk.Button(text="click_before")
		# btn_click.bind("<Button-1>",self.clicked_by_bind)
		
		##lambda pattern [lambda arg: method(arg)]
		#→btn_click.bind("<Button-1>",lambda event:self.clicked(event))

		btn_click.grid(row=0,column=0,ipadx=50)
		
		btn_quit = tk.Button(text="Quit",command=quit)
		btn_quit.grid(row=0,column=1,padx=5,ipadx=20)
		


app = Application()
app.mainloop()	