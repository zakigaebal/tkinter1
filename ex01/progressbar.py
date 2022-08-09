# 이글에서 소개할 tkinter에서 다룰 위젯은 프로그레스 바 다
# 프로그레스바는 진행바로 부르며 웹사이트 및 앱 웹 개발 등 많은 개발에서 다양하게 쓰인다
# 모든 작업이 단순히 1초~5초 만에 뚝딱하고 지시한 내용대로 이뤄질 수 없다
# 서비스를 제공받는 사용자는 단순히 현재 작업을 무기한 기다릴 것이 아니라 얼마나 진행되었는지
# 표시해주면 보다 사용자 친화적이고 좋은 서비스 제공이 가능하다
# 프로그레스 바는 이러한 기능을 수행하는 위젯이다.
# 주로 파일을 내려받거나 전송하는 등 작업에서 얼만큼 진행되었는지 알려주는
# gui의 위젯 중 하나다
# 퍼센트 단위로 표시하거나 단순히 현재 작업이 멈추지 않고 진행 중이라고 알려주는
# 움직임의 표현으로도 사용할 수 있다.
# progress bar widgert exmaple

# tkinter.ttk
# 프로그레스 바 위젯은 tkinter.ttk 모듈에서
# progressbar() 함수를 호출해 사용할 수 있다
# tkinter.ttk 모듈은 Tk 8.5에 도입된 Tk 테마 위젯 모음으로 Themed Tk의 준말이다.
# Gui 위젯을 기느과 UI로 분리해 UI를 쉽게 변경할 수 있도록 하는 toolkt이다.
# 기존 Tkinter으이 확장으로 더 많은 위젯을 포괄한단고 보면 되겠다.

# 상단에 import tkinter.ttk를 사용하여 ttk 모듈을 불러와 사용한다
# tkinter.ttk 를 이용하여 tkinter.ttk함수를 모두 불러와 사용할 수도 있다.

# ttk 모듈 호출
import tkinter.ttk
import tkinter.ttk as ttk

# ttk 모듈의 함수 모두 전체 호출
import tkinter.ttk



# 사용형식
# ttk에서 Progressbar() 함수를 불러와 사용한다
# maximum 값으로 프로그레스바의 최대값을 설정한다
# mode 값을 indeterminate으로 주어 표시 막대가 처음부터 끝까지 반복해 이동하도록 설정한다.

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry("200x150")
window.resizable(False, False)

current_var = tk.DoubleVar()
# StringVar  : string 변수를 선언
# IntVar     : Integer (정수) 변수 선언
# DoubleVar  : float (실수) 변수 선언
# BooleanVar : True Flase 변수 선언

progress_bar = ttk.Progressbar(window, variable=current_var, maximum=100)
progress_bar.pack()

def loop_test():
    btn['state'] = tk.DISABLED

btn = tk.Button(window, text="Test", command=loop_test)
btn.pack()

end_point = 100000
for idx in range(end_point):
    current_var.set(idx/end_point * 100)
    progress_bar.update()

    # messagebox.showinfo("성공", "완료되었습니다!")
    # btn['state'] = tk.NORMAL
    # current_var.set(0)
    # progress_bar.update()

window.mainloop()
