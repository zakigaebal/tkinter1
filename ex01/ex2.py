#위젯사용
#위젯은 객체를 생성하여 필요한 속성들을 지정하여 사용한다. 위젯은 부모 컨테이너와 연관하여 어떤 상대적 위치에 놓이게 되는데, 앞에 설명한 Geometry Manager를 사용하여 각 위젯의 위치를 정하게 된다.
#  아래 예제는 레이블 안에 이미지를 넣고 화면에 보여주는 코드로서, MyFrame 이라는 클래스를 만들고 생성자에서 필요한 위젯들을 배치하고 있다. 우선 main() 에서는 Tk 객체 root를 만들고 title()을 사용하여 윈도우 제목을 설정하고, geometry()를 사용하여 윈도우의 크기와 좌표를 정해주었다. geometry() 안의 문자열은 윈도우 크기 및 좌표를 "가로x세로+X+Y" 형식으로 표현한다. MyFrame 클래스는 Frame으로부터 상속된 파생클래스이고, 생성자에서 Label 하나를 추가하고 있다. Label은 좌표 (0,0)에 위치(place)하게 되고, 레이블 안에는 이미지를 넣고 있다. 이미지는 tkinter의 PhotoImage 클래스를 사용하고 있는데, 이 클래스는 .gif 파일 (혹은 PGM) 만을 읽을 수 있다. 다른 이미지 포맷을 사용하기 위해서는 외부 모듈을 사용해야 한다. PhotoImage() 에 이미지 파일을 적고 리턴된 객체를 레이블에 지정하면 되는데, 특히 가비지 컬렉션으로부터 삭제되는 것을 방지하기 위해 lbl.image = img 처럼 레퍼런스를 증가시켜 준다.
from tkinter import *
 
class MyFrame(Frame):
    def __init__(self, master):
        img = PhotoImage(file='test.gif')
        lbl = Label(image=img)
        lbl.image = img  # 레퍼런스 추가
        lbl.place(x=0, y=0)
 
def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('500x400+10+10')
    myframe = MyFrame(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()