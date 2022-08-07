from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
# 파이썬 tkinter 는 Python 에서 기본적으로 제공하며 Unix, Windows, MacOS 를 지원하는 표준 GUI 프로그래밍 라이브러리 입니다. 
# 사실 엄밀히 따지면 tcl 을 이용한 tk 라이브러리 라고도 하는데 파이썬의 GUI 프로그래밍을 위해 그리 복잡한 내용까지는 알 필요 없으니 tkinter 를 어떻게 사용하는지에 대한 사용방법 위주로 알아보도록 하겠습니다.
#일단 가장 먼저 파이썬 tkinter 를 사용하기 위해선 위의 코드에서 처럼 라이브러리를 불러와야 합니다. 
# 파이썬 공식사이트에 표기된 위의 2가지 형식중 편한 방법을 사용하면 됩니다. 
# 윗줄의 from tkinter import * 의 의미는 tkinter 폴더의 * (모든) 내용을 import 한다는 의미이고 
# 아래의 코드는 tkinter 폴더에서 원하는(여기서는 ttk) 라이브러리를 import 한다는 의미로 보면 됩니다. 
# 여기서는 위의 코드에서 처럼 단순히 import tkinter 로 라이브러리를 불러오고 필요에 따른 세부 항목들로 접근해서 사용하는 방법으로 진행하도록 하겠습니다

import tkinter
win = tkinter.Tk()
win.geometry("300x150") 
# Tkinter Label() 을 생성할때 첫번째 매개변수에는 라벨의 부모가 될 상위 위젯을 넘겨줘야 합니다. 
# 여기서는 메인 윈도우에 라벨을 출력할 것이기 때문에 메인 윈도우인 win 변수를 넘겨주었고 
# text= 매개변수에는 라벨에 최초 표기될 문자열 값을 설정합니다.
#  이렇게 라벨 객체를 생성했으면 실제 위젯에 라벨을 출력해야하는데 이때 pack() 함수를 사용합니다.
label = tkinter.Label(win, text="라벨입니다")
button = tkinter.Button(win, text="버튼1")
text = tkinter.Entry(win)
#보통 에디트박스, 인풋박스 등의 이름을 불리는 입력상자는 Tkinter 에서는 Entry 라는 이름으로 사용됩니다. 물론 라벨이나 버튼과 사용법은 다를게 없습니다.





win = tkinter.Tk()
win.geometry('300x150')

label.place(x=5, y=5, width=290, height=30)
text.place(x=5, y=35, width=290, height=30)
button.place(x=5, y=70, width=290, height=30)

win.mainloop()


