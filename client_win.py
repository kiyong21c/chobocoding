from tkinter import *
from account import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk 
import datetime
from openpyxl import Workbook
from openpyxl import load_workbook  # 파일 불러오기




# def client_window():
root = Tk()
root.title("JK 심리센터")      # 제목 설정
root.geometry("900x600")
root.option_add("*Font", "궁서 20")


########### Tree view ###########
frame1 = Frame(root)
frame1.pack(side="top", fill="both", expand=True)
treeview = ttk.Treeview(root, columns=["1","2","3"], displaycolumns=["1","2","3"])
treeview.pack()
client_lbl = Label(frame1, text="고객정보")
client_lbl.pack(side="left", ipadx=30)

# treeview.column("#0", width=100, anchor="center")
# treeview.heading("#0", text="번호", anchor="center")

treeview.column("#0", width=200, anchor="center")
treeview.heading("#0", text="이름", anchor="center")

treeview.column("#1", width=100, anchor="center")
treeview.heading("1", text="나이", anchor="center")

treeview.column("#2", width=300, anchor="center")
treeview.heading("2", text="전화번호", anchor="center")

treeview.column("#3", width=300, anchor="center")
treeview.heading("3", text="최근방문일", anchor="center")

#################################


########### client apply ########
frame2 = Frame(root)
frame2.pack(side="top", fill="both", expand=True)
add_lbl = Label(frame2, text="고객등록")
add_lbl.pack(side="left", ipadx=30)
##################################

########### client info ##########
# name입력 라벨
frame3 = Frame(root)
frame3.pack(side="top", fill="both", expand=True)
name_label = Label(frame3)
name_label.config(text = "이름")
name_label.pack(side="left")
# name입력 Entry
name = Entry(frame3, width=7, justify='center')
name.pack(fill="x", side="left")
# age입력 라벨
age_label = Label(frame3)
age_label.config(text = "나이")
age_label.pack(side="left")
# age입력 Entry
age = Entry(frame3, width=7, justify='center')
age.pack(fill="x", side="left")
# cell입력 라벨
cell_label = Label(frame3)
cell_label.config(text = "전화번호")
cell_label.pack(side="left")
# cell입력 Entry
cell = Entry(frame3, width=7, justify='center')
cell.pack(fill="x", side="left")
# age입력 Entry/라벨 : 클래스 활용
# class MkEntry():
#     def __init__(self, name, root=root, wid=5):
#         # Label 생성
#         self = Label(root)
#         self.config(text = "{}".format(name))
#         self.pack(side="left")
#         # Entry 생성
#         self = Entry(root, width=wid, justify='center')
#         self.pack(fill="x", side="left")
# age_entry = MkEntry("나이",frame3, 5)
# cell_entry = MkEntry("전화번호",frame3, 13)
# date 라벨
date_label = Label(frame3)
date_label.config(text = "방문일자")
date_label.pack(side="left")
# date 입력 Entry
date_ent = Entry(frame3, width=10)
date_ent.pack(fill="x", side="left")
empty_date = str("{}".format(datetime.datetime.now().strftime('%Y-%m-%d')))
date_ent.insert(0, empty_date)
# def clear(event):   # event를 입력변수로 반드시 넣어줘야 함
#     if date_ent.get() == empty_date:        
#         date_ent.delete(0, len(date_ent.get()))
# date_ent.bind("<Button-1>", clear) # bind() 함수는 지정된 입력이 감지되었을 떄 미리 만들어진 함수를 실행
# 전화번호 라벨/입력
#####################################################


###### 추가 버튼 ######
def add_client():
    location = "/Users/kiyongseo/Documents/Python_Programming/python_chobocoding/tkinter/client_list.xlsx"
    wb = load_workbook(location)   # sample.xlsx 파일을 불러옴
    ws = wb.active  # 현재 활성화된 Sheet를 가져옴
    ws.append([name.get(),age.get(),cell.get(),date_ent.get()])   # 한줄씩 넣기 : 리스트 or 튜플 형태로 넣어줄수 있음
    wb.save(location)  # 워크북의 이름 지정하여 저장 
    wb.close()      # 열려있는 워크북 저장
    print("등록이 완료되었습니다.")
add_btn = Button(frame3)
add_btn.config(padx=5, pady=5, width=10, text="등록", command=add_client)
add_btn.pack(side="left")


root.mainloop() # 창이 닫히지 않도록하는 mainloop()