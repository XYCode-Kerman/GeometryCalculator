# Form implementation generated from reading ui file 'ui_help.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Help)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TextEdit_help = TextEdit(parent=Help)
        self.TextEdit_help.setReadOnly(True)
        self.TextEdit_help.setObjectName("TextEdit_help")
        self.gridLayout_2.addWidget(self.TextEdit_help, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.HyperlinkButton_author = HyperlinkButton(parent=Help)
        self.HyperlinkButton_author.setUrl(QtCore.QUrl("https://space.bilibili.com/551409211"))
        self.HyperlinkButton_author.setObjectName("HyperlinkButton_author")
        self.gridLayout.addWidget(self.HyperlinkButton_author, 0, 0, 1, 1)
        self.HyperlinkButton_github = HyperlinkButton(parent=Help)
        self.HyperlinkButton_github.setUrl(QtCore.QUrl("https://github.com/zhdbk/GeometryCalculator"))
        self.HyperlinkButton_github.setObjectName("HyperlinkButton_github")
        self.gridLayout.addWidget(self.HyperlinkButton_github, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Form"))
        self.HyperlinkButton_author.setText(_translate("Help", "作者：MC着火的冰块"))
        self.HyperlinkButton_github.setText(_translate("Help", "github"))
from qfluentwidgets import HyperlinkButton, TextEdit