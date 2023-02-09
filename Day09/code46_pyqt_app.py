# Date : 2023-02-09
# Author : kimjihyeon-angela
# Desc : PyQt(윈도우 폼 만들기)

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window')
        # self.move(400,200) # self.move 안하면 정중앙 표시함
        self.resize(400, 200)
        self.show() # 핵심 (show 없으면 화면 안나옴)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())