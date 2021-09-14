from tkinter import *
from account import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk 
import datetime

# def client_window():
root = Tk()
root.title("JK 심리센터")      # 제목 설정
root.geometry("900x600")
root.option_add("*Font", "궁서 20")


########### Tree view ###########
frame1 = Frame(root)
frame1.pack(side="top", fill="both", expand=True)
treeview = ttk.Treeview(root, columns=["1","2","3","4"], displaycolumns=["1","2","3","4"])
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
treeview.heading("3", text="전화번호", anchor="center")

treeview.column("#4", width=300, anchor="center")
treeview.heading("4", text="최근방문일", anchor="center")

#################################


########### client insert, modified, delete ########
frame2 = Frame(root)
frame2.pack(side="bottom", fill="both", expand=True)
add_lbl = Label(frame2, text="고객등록")
add_lbl.pack(side="top", ipadx=30)
# name입력 라벨
name_label = Label(frame2)
name_label.config(text = "이름")
name_label.pack(side="left")
# name입력 Entry
name = Entry(frame2)
name.pack(fill="x", side="left")
# age입력 Entry/라벨 : 클래스 활용
class MkEntry():
    def __init__(self, name, root=root, side="left"):
        # Label 생성
        self = Label(root)
        self.config(text = "{}".format(name))
        self.pack(side="left")
        # Entry 생성
        self = Entry(root)
        self.pack(fill="x", side="left")
age_entry = MkEntry("나이",frame2)
cell_entry = MkEntry("전화번호",frame2)
# date 라벨
date_label = Label(frame2)
date_label.config(text = "방문일자")
date_label.pack(side="left")
# date 입력 Entry
date_ent = Entry(frame2)
date_ent.pack(fill="x", side="left")
empty_date = "{}".format(datetime.datetime.now().strftime('%Y-%m-%d'))
date_ent.insert(0, empty_date)
# def clear(event):   # event를 입력변수로 반드시 넣어줘야 함
#     if date_ent.get() == empty_date:        
#         date_ent.delete(0, len(date_ent.get()))
# date_ent.bind("<Button-1>", clear) # bind() 함수는 지정된 입력이 감지되었을 떄 미리 만들어진 함수를 실행
# 전화번호 라벨/입력
####################################################

root.mainloop() # 창이 닫히지 않도록하는 mainloop()