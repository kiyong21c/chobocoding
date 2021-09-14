from tkinter import *
from account import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk 

def client_window():
    root = Tk()
    root.title("JK 심리센터")      # 제목 설정
    root.geometry("900x600")
    root.option_add("*Font", "궁서 20")


    ########### Tree view ###########
    frame1 = Frame(root)
    frame1.pack(side="top", fill="both", expand=True)
    treeview = ttk.Treeview(root, columns=["1", "2","3","4"], displaycolumns=["1","2","3","4"])
    treeview.pack()
    client_lbl = Label(frame1, text="고객정보")
    client_lbl.pack(side="left", ipadx=30)

    treeview.column("#0", width=100, anchor="center")
    treeview.heading("#0", text="번호", anchor="center")

    treeview.column("#1", width=200, anchor="center")
    treeview.heading("1", text="이름", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("2", text="나이", anchor="center")

    treeview.column("#3", width=300, anchor="center")
    treeview.heading("3", text="최근방문일", anchor="center")

    treeview.column("#4", width=300, anchor="center")
    treeview.heading("4", text="전화번호", anchor="center")
    #################################


    ########### client insert, modified, delete ########
    frame2 = Frame(root)
    frame2.pack(side="bottom", fill="both", expand=True)
    ####################################################

    root.mainloop() # 창이 닫히지 않도록하는 mainloop()