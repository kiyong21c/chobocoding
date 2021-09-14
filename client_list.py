# pip install openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook  # 파일 불러오기

location = "/Users/kiyongseo/Documents/Python_Programming/python_chobocoding/tkinter/client_list.xlsx"
wb = load_workbook(location)   # sample.xlsx 파일을 불러옴
ws = wb.active  # 현재 활성화된 Sheet를 가져옴

ws.append(["번호","이름","나이","최근방문일","전화번호"])   # 한줄씩 넣기 : 리스트 or 튜플 형태로 넣어줄수 있음
ws.append(["1","김지경","35","20210914","010-2083-8890"])
# for i in range(1, 11):  # 10줄 넣기
#     ws.append([i, randint(0,100), randint(0,100)])
print(ws["A2"].value) # A1 셀의 값을 출력


wb.save(location)  # 워크북의 이름 지정하여 저장 
wb.close()      # 열려있는 워크북 저장