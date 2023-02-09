# Date : 2023-02-09
# Author : kimjihyeon-angela
# Desc : PyQt (윈도우 창닫기)

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(320, 170)
        btn.resize(btn.sizeHint()) # 글자크기에 맞춰 알아서 크기 조절해줌
        # 버튼에 툴팁 넣기
        btn.setToolTip('이거 누르면 그냥 꺼져요. <b>조심</b>하세요!!')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('Quit Button')
        self.setGeometry(800, 300, 400, 200) #(x, y, w, h)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
