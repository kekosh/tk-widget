import tkinter as tk
from tkinter import messagebox
import os
import json
import collections as cl

#----------------------------------------------------
""" create text file for save input data
    if target file is nothing, make new text file.
    if same name file is exists, add new line """
def set_regist_data_file():
    #check os type（windows:nt linux:posix）
    if os.name == "nt":
        path = os.getcwd() + "\\regdata.txt"
    else:
        path = os.getcwd() + "/regdata.txt"
    return path


""" load json-file data """
def load_jsonfile(path):
    try:
        with open(path, "r") as f:
            json_data = json.load(f)

            """ if 'used' on setting is True, get settings region data.
                else if 'used' is false,get defaut region data
            """




            print(json_data["default"])

            """ json.dumps will format the output data to json style """
            # dump = json.dumps(json_data, indent=4)
            # print(dump)
    except:
        print("Error")


def save_jsonfile(path):
    o_odict = cl.OrderedDict()
    i_odict = cl.OrderedDict()

    count = lb.cget("text")
    entry = ent.cget("text")

    i_odict["count"] = count
    i_odict["entry"] = entry
    o_odict["default"] = i_odict

    #print(json.dumps(o_odict, indent=4))
    with open(path, "w+") as f:
        json.dump(o_odict, f, indent=4)


def click():
    counter = int(lb.cget("text")) + 1
    lb["text"]= counter


def click_2():
    '''　Entry-Widgetへの入力値はget()メソッドで取得する。
        if文の1行記述[変数 = Trueの場合の処理　if 条件式 else Flaseの場合の処理] '''
    input_ent = ent.get() if ent.get() != "" else "BLANK!!"

    messagebox.showinfo(title="information", message=input_ent)


#----------------------------------------------------

root = tk.Tk()
root.title("count-up")
root.geometry("400x300")

# <- Frame1 ->
frame1 = tk.Frame(root, width="3c", height="5c")
frame1.propagate(False)

lb = tk.Label(frame1, text=0)
lb.pack()

btn = tk.Button(frame1, text="Click", command=click)
btn.pack()
frame1.grid(row=0, column=0)

#<- Frame2 ->
frame2 = tk.Frame(root, width="5c", height="5c", relief="ridge", borderwidth="2")
frame2.propagate(False)
ent = tk.Entry(frame2)
ent.pack()

btn2 = tk.Button(frame2, text="Click_2", command=click_2)
btn2.pack()

""" textbox with scrollber Widget  """
# import tkinter.scrolledtext as tkscr
# scrtxt = tkscr.ScrolledText(frame2)
# scrtxt.pack()

frame2.grid(row=0, column=1)

frame3 = tk.Frame(root, width="100", height="5c")
frame3.propagate(False)
btn3 = tk.Button(frame3, text="Quit", command=lambda:root.destroy())
btn3.pack(side=tk.LEFT, padx=10)

frame3.grid(row=0, column=3)


#methods
path = set_regist_data_file()
load_jsonfile(path)
save_jsonfile(path)


root.mainloop()