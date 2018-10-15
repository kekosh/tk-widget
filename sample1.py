import tkinter 

#ウィンドウ作成
#-------- FIXED -----------
root = tkinter.Tk()
root.title("Sample1")
root.geometry("250x150")
#-------- FIXED -----------

#ラベル
label = tkinter.Label(text="label")
label.pack()

#Entry（一行入力）
## insert(デフォルト入力として代用)
entry_input = tkinter.Entry()
entry_input.insert(tkinter.END,"default")
entry_input.pack()

## show(password blind)
entry_showtype = tkinter.Entry(show="*",width=20)
entry_showtype.pack()

## state（normal or readonly）
entry_state = tkinter.Entry(state="normal",width=20)
entry_state.pack()

##ボタン押下時の処理
def GetEntryValue(event):
	'''
	Entryの値を更新する際はdeleteしてからInsertを行う。
	state=readonlyのEntryフォームは操作できない。
	'''
	val = entry_input.get()

	#obj.delete(start,end)
	entry_state.delete(0,tkinter.END)
	
	#obj.insert(start,value)
	entry_state.insert(0,val)
	

#ボタン
button = tkinter.Button(text="py/tkinter",foreground="white",background="red",border="5px")

## オブジェクト作成後にオプションを設定、変更する場合はobj.configure(option=setting)
#button.configure(state='disable')

## Entryの値を取得
### obj.bind(event-key,function)
'''
keybindの参考URL
http://www.rouge.gr.jp/~fuku/tips/python-tkinter/bind.shtml
'''
button.bind("<Button-1>",GetEntryValue)
button.pack()
#button.place(x=95,y=75)

#Checkbutton変更時の処理
def GetCheckbuttonVal():
	'''
	Checkbuttonの設定値はオブジェクトから取得することはできない。
	オブジェクトのvariableオプションに代入している変数から直接get()で取得する必要がある。
	'''
	if var.get() == 1:
		print("checked")
	else:
		print("unchecked")

#チェックボックス(tkではCheckbuttonと呼ぶ)
##Checkbuttonの設定値はtkinterオブジェクト(～Var())を使用する必要がある。
var = tkinter.IntVar()
chkbtn = tkinter.Checkbutton(text="check1",variable=var,command=GetCheckbuttonVal)
chkbtn.pack()



#-------- FIXED -----------
root.mainloop()
#-------- FIXED -----------