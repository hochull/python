import random, sys, os, shutil, glob
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class main(QWidget):
    def __init__(self):
        super(main, self).__init__()
        self.srcDir = 'C:\\Program Files\\'
        self.filetype = "*.txt"  # 찾고자 하는 확장자
        self.btnSet = QPushButton("검색 설정 완료")
        self.btnFnd = QPushButton("파일 찾기")
        self.btnClr = QPushButton("로그 지우기")
        self.le_type = QLineEdit()
        self.le_dir = QLineEdit()
        self.le = QLineEdit()
        self.tb = QTextBrowser()
        self.lb_type = QLabel('검색 타입. ex: *.jpg, *.txt', self)
        self.lb_dir = QLabel('검색 위치. ex: c:/temp/', self)
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("QTableView")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lb_type)
        hbox1.addWidget(self.le_type)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.lb_dir)
        hbox2.addWidget(self.le_dir)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.lb_dir)
        vbox.addWidget(self.btnSet)
        vbox.addWidget(self.btnFnd)
        vbox.addWidget(self.le)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.btnClr)
        self.setLayout(vbox)

    def setSlot(self):
        self.btnFnd.clicked.connect(self.findPicture)
        self.btnSet.clicked.connect(self.setParam)
        # self.btnFnd.clicked.connect(lambda: print("it's button"))  # 이건 되네..
        # self.btnFnd.clicked.connect(lambda x="_hi": print("it's button"+x))  # 이건 안되네..
        # self.btnFnd.clicked.connect(print("it's button"))  #이건 안되네..
        self.le.returnPressed.connect(self.le_append_text)
        self.btnClr.clicked.connect(self.clear_text)

    def setParam(self):
        strA = self.le_dir.text()
        strB = self.le_type.text()
        self.srcDir = strA
        self.filetype = strB
        """line editor에서 받아오는 값의 유효성을 체크해야 한다. 향후 업데이트 필요"""

    def le_append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()

    def fast_scandir(self, dirname):
        try:
            subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
            # 아주 중요한 문법. 위와 같이 list를 만들 수 있다.
            # [x for x in range(1, 5)] <-- 단순 for 문
            # or [x for x in range(1,5) if x > 2] <-- for문 + if 문
        except Exception as e:
            print(e)
            self.tb.append(e.__str__())
            #print(type(e))
            return []
        else:
            for dirname in list(subfolders):
                subfolders.extend(self.fast_scandir(dirname))
            return subfolders

    def findPicture(self):
        # 찾는 디렉토리. picDir
        #filelist = glob.glob(self.picDir + filetype)
        filelist = glob.glob(self.srcDir + self.filetype)
        print("root folder's target file number is " + len(filelist).__str__())
        self.tb.append("root folder's target file number is " + len(filelist).__str__())
        #folderlist = self.fast_scandir(self.picDir)
        folderlist = self.fast_scandir(self.srcDir)
        print("all folder count is " + len(folderlist).__str__())
        self.tb.append("all folder count is " + len(folderlist).__str__())
        for folder in folderlist:
            result = len(glob.glob(folder + '\\' + self.filetype))
            if result > 0:
                print(folder + " sub folder has " + result.__str__())
                self.tb.append(folder + " sub folder has " + result.__str__())
            else:
                pass
        # b = os.listdir(self.picDir)
        # a = len(b)
        # # 카운트
        # # 프린트 카운트
        # print("file count is " + a.__str__())
        # cnt = 0
        # for iidx, i in enumerate(b):
        #     print((iidx+1).__str__() + " is " + i)
        #     if os.path.isfile(self.picDir+i):
        #         print(i + " is file")
        #         if i[-4:] == '.txt':
        #             print("it's text file")
        #             cnt += 1
        #         else:
        #             print("'it's not text file")
        #     else:
        #         print(i + " is folder")
        # print("total matching file count is " + cnt.__str__())

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())
