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
button = tkinter.Button(text="py/tkinter",foreground="white",background="red",border="4")

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
	# if var_box1.get() == 1:
		# print("v_1 is checked")
	# else:
		# print("v_1 is unchecked")

	# if var_box2.get() == 1:
		# print("v_2 is checked")
	# else:
		# print("v_2 is unchecked")

#チェックボックス(tkではCheckbuttonと呼ぶ)
##Checkbuttonの設定値はtkinterオブジェクト(～Var())を使用する必要がある。
var_box1 = tkinter.IntVar()
var_box2 = tkinter.IntVar()

chkbtn_1 = tkinter.Checkbutton(text="check1",variable=var_box1,command=GetCheckbuttonVal)
chkbtn_2 = tkinter.Checkbutton(text="check2",variable=var_box2,command=
GetCheckbuttonVal)

chkbtn_1.pack()
chkbtn_2.pack()

#ラジオボタン
'''
tkinter.Radiobuttonのvariableオプションの値が一致するものがグループ化される。
valueオプションには数字を指定し、「0」がON、「1」がOFF
'''
category = tkinter.IntVar()
radiobtn_1 = tkinter.Radiobutton(text="radio1",variable=category,value=0)
radiobtn_2 = tkinter.Radiobutton(text="radio2",variable=category,value=1)

radiobtn_1.pack(side='left')
radiobtn_2.pack(side='right')


#-------- FIXED -----------
root.mainloop()
#-------- FIXED -----------