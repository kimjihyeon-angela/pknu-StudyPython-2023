# Date : 2023-02-09
# Author : kimjihyeon-angela
# Desc : PyQt(윈도우 폼 만들기)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        # 단축키 지정
        actExit.setShortcut('Ctrl+Q') 
        actExit.setStatusTip('앱 종료')
        # 종료 하는 이벤트 추가
        actExit.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu  = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 상태바
        self.statusBar().showMessage('Status Bar Message')
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        self.setGeometry(800, 300, 400, 200) #(x, y, w, h)
        self.show() # 핵심 show 없으면 화면 안나옴
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())