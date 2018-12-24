import os
import sys
import json
import datetime as dt
import collections as cl
import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets(master)

    def get_jsonfile(self):
        "os.nameが「nt」の場合はwindows環境"
        separator = "\\" if os.name == "nt" else "/"
        json_path = "{0}{1}data.json".format(os.getcwd(), separator)

        isexist = os.path.exists(json_path)
        if isexist:
            pass
        else:
            sampledata = {"data":
                          {"sampleXXX":
                           {"count": 3, "memo": "No data Sample.", "from": "1900/01/01", "to": "3999/12/31"}}}

            with open(json_path, "w+") as f:
                json.dump(sampledata, f, indent=4)

        return isexist, json_path

    def json_load(self):
        isexist, jsonfile = self.get_jsonfile()

        with open(jsonfile, "r") as f:
            json_data = json.load(f, object_pairs_hook=cl.OrderedDict)

        odict = cl.OrderedDict()
        odict = json_data["data"]
        return odict

    def check_and_cast_inputs(self, _count, _task_name):
        __count = 0
        __task_name = ""
        __err = ""

        if len(_count.strip()) > 0:
            try:
                __count = int(_count)
            except:
                __err = str(sys.exc_info()[1])

        if len(_task_name.strip()) > 0:
            __task_name = _task_name
        else:
            if len(__err) > 0:
                __err = __err + "\r\n"

            __err += "task_name is empty."

        return __count, __err

    def save_jsonfile(self):
        ###入力済データ取得
        count = self.count_entry.get()
        task_name = self.task_name_entry.get()
        description = self.description_entry.get()
        period_from = self.period_from_entry.get()
        period_to = self.period_to_entry.get()

        ###キャストと入力チェック
        count, err = self.check_and_cast_inputs(count, task_name)
        if len(err) > 0:
            messagebox.showerror(title="Warning!!", message=err)
            return

        ###fromとtoの整合性確認
        retmsg = self.consist_tofrom(period_from, period_to)
        if retmsg is not None:
            messagebox.showwarning("Warning!!", retmsg)
            return

        #check_input_date_format
        retmsg = self.cast_str_to_dtobj(period_from)
        if retmsg is not None:
            messagebox.showerror("Error!!", retmsg)
            return

        retmsg = self.cast_str_to_dtobj(period_to)
        if retmsg is not None:
            messagebox.showerror("Error!!", retmsg)
            return

        _remains = self.calc_remains(period_from, period_to)

        self.period_remains_entry.delete(0, tk.END)
        self.period_remains_entry.insert(tk.END, _remains)

        ###データ登録用オブジェクト作成
        odict_data = cl.OrderedDict()
        odict_data = {"count": int(count), "memo": description,
                      "from": period_from, "to": period_to, "remians": _remains}

        odict_shell = cl.OrderedDict()
        odict_shell["data"] = odict_data

        ###データ登録のために現時点のJsonファイルを読み込む
        isexist, jsonfile = self.get_jsonfile()
        load_data = None
        with open(jsonfile, "r") as f:
            load_data = json.load(f)

        ###新規データの場合はリストボックスにkeyを追加する
        if task_name not in load_data["data"]:
            self.data_listbox.insert(tk.END, task_name)

        load_data["data"][task_name] = odict_data
        with open(jsonfile, "w") as f:
            json.dump(load_data, f, indent=4)

        messagebox.showinfo(title="Infomation", message="complete!!")

    def consist_tofrom(self, _from, _to):
        errmsg = None
        date_from = dt.datetime.strptime(_from, '%Y/%m/%d')
        date_to = dt.datetime.strptime(_to, '%Y/%m/%d')

        if date_to < date_from:
            errmsg = "'To' date is ahead of 'From' "
        return errmsg

    def calc_remains(self, date_from, date_to):
        _from = dt.datetime.strptime(date_from, '%Y/%m/%d')
        _to = dt.datetime.strptime(date_to, '%Y/%m/%d')

        if _from == _to:
            return "0"
        else:
            to_minus_from = _to - _from
            parse_str = str(to_minus_from).split(" ")
        return str(parse_str[0])

    def cast_str_to_dtobj(self, str_date):
        try:
            #stringをdatetimeにパースすると時分秒が付与される(00:00:00)
            cast_date = dt.datetime.strptime(str_date, '%Y/%m/%d')
            date_ymd, date_time = str(cast_date).split(" ")
            date_ymd = date_ymd.replace("-", "/")
            errmsg = None
        except:
            #変換でエラーが発生した場合は入力値をそのまま返す
            date_ymd = str_date
            errmsg = "error is occured on string to date parse function.＜{0}＞".format(
                str_date)
        finally:
            return errmsg
    """ ここまで """

    def get_oncursor(self):
        index = select_data_key = errmsg = ""
        try:
            index = self.data_listbox.curselection()
            select_data_key = self.data_listbox.get(index)
        except:
            errmsg = str(sys.exc_info()[1])
        return index, select_data_key, errmsg

    def get_selected(self, event):
        index, select_data_key, errmsg = self.get_oncursor()

        if len(errmsg) > 0:
            messagebox.showerror(title="Error!!", message=errmsg)
            return

        ###キーを使用してjsonファイルを読み込み、該当データを抜き出し
        isexist, jsonfile = self.get_jsonfile()

        with open(jsonfile, "r") as f:
            json_data = json.load(f, object_pairs_hook=cl.OrderedDict)

        ###反映前に既存データを削除
        self.clear_entry()

        ###抜き出したデータを項目別に変数に格納
        self.count_entry.insert(
            tk.END, json_data["data"][select_data_key]["count"])
        self.task_name_entry.insert(tk.END, select_data_key)
        self.description_entry.insert(
            tk.END, json_data["data"][select_data_key]["memo"])
        self.period_from_entry.insert(
            tk.END, json_data["data"][select_data_key]["from"])
        self.period_to_entry.insert(
            tk.END, json_data["data"][select_data_key]["to"])

    def delete_record(self):
        index, key, errmsg = self.get_oncursor()

        if len(errmsg) > 0:
            messagebox.showerror(title="Error!!", message=errmsg)
            return

        isexist, jsonfile = self.get_jsonfile()

        with open(jsonfile, "r") as f:
            json_data = json.load(f, object_pairs_hook=cl.OrderedDict)
            del json_data["data"][key]

        self.data_listbox.delete(index, index)

        with open(jsonfile, "w") as f:
            json.dump(json_data, f, indent=4)

    def clear_entry(self):
        self.count_entry.delete(0, tk.END)
        self.task_name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.period_from_entry.delete(0, tk.END)
        self.period_to_entry.delete(0, tk.END)
        self.period_remains_entry.delete(0, tk.END)

    def update_count(self, key):
        """
        key -- 1:UP 2:Down
        """
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

    def quit_app(self):
        root.destroy()

    def create_widgets(self, master):
        self.OuterFrame = tk.Frame(master, relief=tk.SOLID, borderwidth=1)
        self.OuterFrame.pack(padx=5, pady=10, fill=tk.X)

        ####-----------------------------------------------------------------------------------
        self.list_Frame = tk.Frame(
            self.OuterFrame, relief=tk.SOLID, borderwidth=1)
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
        ###[input data]
        self.input_frame = tk.Frame(
            self.OuterFrame, relief=tk.SOLID, borderwidth=1)
        self.input_frame.pack(padx=5, pady=10, ipady=5, fill=tk.X)

        self.lbl_1 = tk.Label(self.input_frame, text="count")
        self.lbl_1.grid(row=0, column=0)
        self.count_entry = tk.Entry(
            self.input_frame, width=10, borderwidth=1, relief=tk.SOLID)
        self.count_entry.grid(row=1, column=0, padx=5)

        self.lbl_2 = tk.Label(self.input_frame, text="name")
        self.lbl_2.grid(row=0, column=1)
        self.task_name_entry = tk.Entry(
            self.input_frame, width=25, borderwidth=1, relief=tk.SOLID)
        self.task_name_entry.grid(row=1, column=1, padx=5)

        self.lbl_3 = tk.Label(self.input_frame, text="description")
        self.lbl_3.grid(row=0, column=2)
        self.description_entry = tk.Entry(
            self.input_frame, width=35, borderwidth=1, relief=tk.SOLID)
        self.description_entry.grid(row=1, column=2, padx=5)
        ###-----------

        ###[Period]-----
        self.period_frame = tk.Frame(self.input_frame)
        self.period_frame.grid(row=3, column=0, columnspan=2, sticky=tk.E+tk.W)
        self.lbl_pf = tk.Label(self.period_frame, text="From")
        self.lbl_pf.grid(row=0, column=0)
        self.period_from_entry = tk.Entry(
            self.period_frame, width=12, borderwidth=1, relief=tk.SOLID)
        self.period_from_entry.grid(row=1, column=0, padx=5)
        self.lbl_pt = tk.Label(self.period_frame, text="To")
        self.lbl_pt.grid(row=0, column=1)
        self.period_to_entry = tk.Entry(
            self.period_frame, width=12, borderwidth=1, relief=tk.SOLID)
        self.period_to_entry.grid(row=1, column=1, padx=5)
        self.lbl_period = tk.Label(self.period_frame, text="Period")
        self.lbl_period.grid(row=0, column=2)
        self.period_remains_entry = tk.Entry(
            self.period_frame, width=5, borderwidth=1, relief=tk.SOLID)
        self.period_remains_entry.grid(row=1, column=2, padx=5)
        self.lbl_remains = tk.Label(self.period_frame, text="Remain")
        self.lbl_remains.grid(row=0, column=3)
        self.period_remains_entry = tk.Entry(
            self.period_frame, width=5, borderwidth=1, relief=tk.SOLID)
        self.period_remains_entry.grid(row=1, column=3, padx=5)
        ###-----------

        ###[Function Button]
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
        self.btn_save.grid(row=1, column=0)
        self.btn_delete = tk.Button(
            self.func_btn_frame, text="Delete", width=8, command=lambda: self.delete_record())
        self.btn_delete.grid(row=1, column=1)
        self.btn_quit = tk.Button(
            self.func_btn_frame, text="Quit", width=8, command=self.quit_app)
        self.btn_quit.grid(row=1, column=2)
        ###-----------


root = tk.Tk()
root.title("single_counter")
#root.geometry("500x400")
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()
