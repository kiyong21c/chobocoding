# 로그인

from tkinter import *

def log_in():
    pass

def show_option():
    if pw.get() == 0:
        ent2.config()
        print(pw.get())
    if pw.get() == 1:
        ent2.config(show="*")
        print(pw.get())

root = Tk()     # T대문자 k소문자
root.title("JK 심리센터")      # 제목 설정
root.geometry("800x600")
root.option_add("*Font", "궁서 20")
###### img 라벨 ######
img_lab = Label(root)
background_image=PhotoImage(file="/Users/kiyongseo/Documents/Python_Programming/python_chobocoding/스크린샷 2021-09-12 오후 10.27.02.png", master=root)
background_image = background_image.subsample(2)
img_lab.config(image=background_image)

img_lab.pack()

###### id 프레임 ######
lab1_frame = Frame(root)
lab1_frame.pack(fill="x", padx=5, pady=5)   # 가로로 채워짐
# id 입력창
ent1 = Entry(lab1_frame)
ent1.pack(fill="x", side="right")
# id 라벨
lab1 = Label(lab1_frame)
lab1.config(text = "ID")
lab1.pack(side="right")
####################

###### pw 프레임 #####
lab2_frame = Frame(root)
lab2_frame.pack(fill="x", padx=5, pady=5)   # 가로로 채워짐
# pw 입력창
ent2 = Entry(lab2_frame)

ent2.pack(fill="x", side="right")
# pw 라벨
lab2 = Label(lab2_frame)
lab2.config(text = "Password")
lab2.pack(side="right")
####################

###### 로그인 프레임 #####
log_in_frame = Frame(root)
log_in_frame.pack(fill="x", padx=5, pady=5)   # 가로로 채워짐
# 로그인 버튼
log_in_btn = Button(log_in_frame)
log_in_btn.config(padx=5, pady=5, width=12, text="로그인", command=log_in)
log_in_btn.pack(side="right")
# 비밀번호 노출/비노출 버튼(체크박스)
# pw = IntVar()
pw = IntVar()
pw_btn = Checkbutton(log_in_frame)
pw_btn.config(text="암호화", variable=pw, onvalue=1, offvalue=0, command=show_option)
pw_btn.pack(side="right")


root.resizable(False, False) # x(너비), y(높이)값 변경 불가: 창 크기 변경 불가
root.mainloop() # 창이 닫히지 않도록하는 mainloop()