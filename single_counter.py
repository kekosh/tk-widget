import os
import tkinter as tk
import json
import collections as cl

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets(master)

    def get_jsonfile(self):
        "os.nameが「nt」の場合はwindows環境"
        separator = "\\" if os.name == "nt" else "/"
        return "{0}{1}data.json".format(os.getcwd(),separator)

    def json_load(self):
        jsonfile = self.get_jsonfile()

        with open(jsonfile,"r") as f:
            json_data = json.load(f)

        odict = cl.OrderedDict()
        odict = json_data["data"]
        return odict

    def create_widgets(self, master):
        self.OuterFrame = tk.Frame(master, relief=tk.SOLID, borderwidth="1")
        self.OuterFrame.pack(padx=5, pady=10, fill=tk.X)

        self.list_Frame = tk.Frame(
            self.OuterFrame, relief=tk.SOLID, borderwidth="1")
        self.list_Frame.pack(padx=5, pady=10, fill=tk.X)

        """
        リストに表示するデータは配列をStringVarサブクラス型の変数に変換する必要がある。
        """
        # list_val = tk.StringVar(value=["BTC", "BCH", "XRP", "NEM", "ETH",
        #                                "MONERO", "BNK", "LSK", "ALIS", "MONA", "GAKT", "YEN", "$"])

        #jsonファイルを読み込んで第一改装のキー情報をリスト型変数にいったん格納する。
        json_data = self.json_load()
        value_list = []
        for i in json_data.keys():
            value_list.append(i)

        list_value = tk.StringVar(value=value_list)

        self.data_listbox = tk.Listbox(
            self.list_Frame, listvariable=list_value, width="76")
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

        self.input_frame = tk.Frame(
            self.OuterFrame, relief=tk.SOLID, borderwidth="1")
        self.input_frame.pack(padx=5, pady=10, fill=tk.X)

        self.count_entry = tk.Entry(
            self.input_frame, width=30, borderwidth="1", relief=tk.SOLID)
        self.count_entry.grid(row=1, column=0)





root = tk.Tk()
root.title("single_counter")
root.geometry("500x500")
root.resizable(1, 1)
app = Application(master=root)
app.mainloop()
