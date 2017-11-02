# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export_To_GE_dockwidget_base.ui'
#
# Created: Tue Jun 06 19:58:24 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ExportToGEDockWidgetBase(object):
    def setupUi(self, ExportToGEDockWidgetBase):
        ExportToGEDockWidgetBase.setObjectName(_fromUtf8("ExportToGEDockWidgetBase"))
        ExportToGEDockWidgetBase.resize(232, 141)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        ExportToGEDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(ExportToGEDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(ExportToGEDockWidgetBase)

    def retranslateUi(self, ExportToGEDockWidgetBase):
        ExportToGEDockWidgetBase.setWindowTitle(_translate("ExportToGEDockWidgetBase", "Export To Google Earth", None))
        self.label.setText(_translate("ExportToGEDockWidgetBase", "Replace this QLabel\n"
"with the desired\n"
"plugin content.", None))

