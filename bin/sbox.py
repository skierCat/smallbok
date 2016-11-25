# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\1.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        self.idNum=1
        self.stop=1
        Form.setObjectName("Form")
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.resize(229, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        tmp_img=QtGui.QPixmap('cover/cover_'+str(self.idNum)+'.png')
        self.label.setPixmap(tmp_img)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.timer = QtCore.QTimer(Form)
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.updateUI)
        self.timer.start()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
    def updateUI(self):
        if(self.idNum==5):self.idNum=1
        tmp_img=QtGui.QPixmap('cover/cover_'+str(self.idNum)+'.png')
        self.label.setPixmap(tmp_img)
        self.idNum=self.idNum+1
        self.stop=self.stop+1
        if(self.stop==10):
            self.timer.stop()
            self.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

