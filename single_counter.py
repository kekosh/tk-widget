import os
import tkinter as tk
import json
import collections as cl
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets(master)

    def get_jsonfile(self):
        "os.nameが「nt」の場合はwindows環境"
        separator = "\\" if os.name == "nt" else "/"
        return "{0}{1}data.json".format(os.getcwd(), separator)

    def json_load(self):
        jsonfile = self.get_jsonfile()

        with open(jsonfile, "r") as f:
            json_data = json.load(f, object_pairs_hook=cl.OrderedDict)

        odict = cl.OrderedDict()
        odict = json_data["data"]
        return odict

    def save_jsonfile(self):
        ###入力済データ取得
        count = self.count_entry.get()
        task_name = self.task_name_entry.get()
        description = self.description_entry.get()

        ###データ登録用オブジェクト作成
        odict_data = cl.OrderedDict()
        odict_data = {"count":int(count), "memo":description}

        odict_shell = cl.OrderedDict()
        odict_shell["data"] = odict_data

        ###データ登録のために現時点のJsonファイルを読み込む
        jsonfile = self.get_jsonfile()
        load_data = None
        with open(jsonfile, "r") as f:
            load_data = json.load(f)

        ###新規データの場合はリストボックスにkeyを追加する
        if task_name not in load_data["data"]:
            self.data_listbox.insert(tk.END, task_name)

        load_data["data"][task_name] = odict_data
        with open(jsonfile, "w") as f:
            json.dump(load_data, f, indent=4)

    def get_selected(self, event):
        select_IDX = self.data_listbox.curselection()
        select_data_key = self.data_listbox.get(select_IDX)

        ###キーを使用してjsonファイルを読み込み、該当データを抜き出し
        jsonfile = self.get_jsonfile()

        with open(jsonfile, "r") as f:
            json_data = json.load(f, object_pairs_hook=cl.OrderedDict)

        ###反映前に既存データを削除
        self.clear_entry()

        ###抜き出したデータを項目別に変数に格納
        self.count_entry.insert(tk.END, json_data["data"][select_data_key]["count"])
        self.task_name_entry.insert(tk.END, select_data_key)
        self.description_entry.insert(tk.END, json_data["data"][select_data_key]["memo"])

    #[Note]選択データ削除処理実装中
    def delete_record(self):
        None

    def clear_entry(self):
        self.count_entry.delete(0, tk.END)
        self.task_name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def update_count(self, key):
        input = self.count_entry.get()

        if input.isdigit():
            if key == 1:
                count = int(input) + 1
            else:
                count = int(input) - 1
                count = 0 if count < 0 else count
        else:
            count = ""

        self.count_entry.delete(0, tk.END)
        self.count_entry.insert(tk.END, count)

    def create_widgets(self, master):
        self.OuterFrame = tk.Frame(master, relief=tk.SOLID, borderwidth="1")
        self.OuterFrame.pack(padx=5, pady=10, fill=tk.X)

        ####-----------------------------------------------------------------------------------
        self.list_Frame = tk.Frame(
            self.OuterFrame, relief=tk.SOLID, borderwidth="1")
        self.list_Frame.pack(padx=5, pady=10, fill=tk.X)

        """
        ListBox-Widgetに表示するデータは配列をStringVarサブクラス型の変数に変換する必要がある。
        """
        #jsonファイルを読み込んで第一改装のキー情報をリスト型変数にいったん格納する。
        json_data = self.json_load()
        #リスト内包表記：式 for 任意変数 in イテラブルオブジェクト
        value_list = [i for i in json_data.keys()]

        list_value = tk.StringVar(value=value_list)

        self.data_listbox = tk.Listbox(
            self.list_Frame, listvariable=list_value, width="76")
        self.data_listbox.bind("<Double-1>", self.get_selected)
        #self.data_listbox.bind("<Double-1>", self.get_selected)
        self.data_listbox.pack(side=tk.LEFT, fill=tk.X)

        """
        ScrollBarはスクロールを必要とするウィジェットとは別に定義する必要がある。
        また、ウィジェットとスクロールバーウィジェットの紐づけには、
        ScrollBarのcommandオプションと紐づけ先ウィジェットのscrollcommandオプションを
        設定する必要がある。
        """
        sb_y = tk.Scrollbar(self.list_Frame, orient='v',
                            command=self.data_listbox.yview)
        sb_x = tk.Scrollbar(self.list_Frame, orient='h',
                            command=self.data_listbox.xview)
        self.data_listbox.configure(yscrollcommand=sb_y.set)
        self.data_listbox.configure(xscrollcommand=sb_x.set)
        sb_y.pack(side=tk.LEFT, fill=tk.Y)

        ####-----------------------------------------------------------------------------------
        self.input_frame = tk.Frame(
            self.OuterFrame, relief=tk.SOLID, borderwidth="1")
        self.input_frame.pack(padx=5, pady=10, ipady=5, fill=tk.X)

        self.lbl_1 = tk.Label(self.input_frame, text="count")
        self.lbl_1.grid(row=0, column=0)
        self.count_entry = tk.Entry(
            self.input_frame, width=10, borderwidth="1", relief=tk.SOLID)
        self.count_entry.grid(row=1, column=0, padx=5)

        self.lbl_2 = tk.Label(self.input_frame, text="name")
        self.lbl_2.grid(row=0, column=1)
        self.task_name_entry = tk.Entry(
            self.input_frame, width=25, borderwidth="1", relief=tk.SOLID)
        self.task_name_entry.grid(row=1, column=1, padx=5)

        self.lbl_3 = tk.Label(self.input_frame, text="description")
        self.lbl_3.grid(row=0, column=2)
        self.description_entry = tk.Entry(
            self.input_frame, width=35, borderwidth="1", relief=tk.SOLID)
        self.description_entry.grid(row=1, column=2, padx=5)

        self.func_btn_frame = tk.Frame(self.input_frame)
        self.func_btn_frame.grid(row=3, column=2, pady=10)

        self.btn_up = tk.Button(self.func_btn_frame, text="Up",
                                     width=8, command=lambda: self.update_count(1))
        self.btn_up.grid(row=0, column=0, padx=5, pady=5)
        self.btn_down = tk.Button(self.func_btn_frame, text="Down",
                                     width=8, command=lambda: self.update_count(2))
        self.btn_down.grid(row=0, column=1, padx=5, pady=5)
        self.btn_clear = tk.Button(self.func_btn_frame, text="Clear",
                                     width=8, bg="lightgray", command=self.clear_entry)
        self.btn_clear.grid(row=0, column=2, padx=5, pady=5)
        self.btn_save = tk.Button(self.func_btn_frame, text="Save",
                                     width=8, command=self.save_jsonfile)
        self.btn_save.grid(row=1, column=1)
        self.btn_delete = tk.Button(self.func_btn_frame, text="Delete", width=8, command=self.delete_record)

root = tk.Tk()
root.title("single_counter")
root.geometry("500x500")
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()
