#from tkinter import *
#root= Tk()
#root.mainloop()

# 간단한 다이얼로그
# 그럼 Tkinter를 이용하여 간단한 다이얼로그를 만들어 보는데,
# 이 다이얼로그에는 하나의 레이블, 하나의 텍스트박스, 하나의 버튼이
# 있다고 가정하자
# 이러한 위젯들을 root 객체 생성(root=TK())과 rootm.mainloop()사이에 생성하게 된다.
# 아래 예제는 "이름"이라는 레이블과 중간에 텍스트박스 하나
# 그리고 맨 밑에 Ok버튼을 가지도록 한 코드다
# from tkinter import *
# root = Tk()
 
# lbl = Label(root, text="이름")
# lbl.pack()
 
# txt = Entry(root)
# txt.pack()
 
# btn = Button(root, text="OK", background="blue")

# btn.pack()
 
# root.mainloop()


from tkinter import *
root = Tk()
 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
btn = Button(root, text="OK", width=15)
btn.grid(row=1, column=1)
 
root.mainloop()