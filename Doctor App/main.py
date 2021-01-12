# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\doctor_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1438, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.UserLogin = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.UserLogin.setFont(font)
        self.UserLogin.setObjectName("UserLogin")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.UserLogin)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.UserName = QtWidgets.QLabel(self.UserLogin)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.UserName.setFont(font)
        self.UserName.setObjectName("UserName")
        self.gridLayout_5.addWidget(self.UserName, 0, 0, 1, 1)
        self.UserPassword = QtWidgets.QLabel(self.UserLogin)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.UserPassword.setFont(font)
        self.UserPassword.setObjectName("UserPassword")
        self.gridLayout_5.addWidget(self.UserPassword, 1, 0, 1, 1)
        self.user_enter = QtWidgets.QLineEdit(self.UserLogin)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.user_enter.setFont(font)
        self.user_enter.setObjectName("user_enter")
        self.gridLayout_5.addWidget(self.user_enter, 0, 1, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.UserLogin)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_5.addWidget(self.login_btn, 2, 1, 1, 1)
        self.pass_enter = QtWidgets.QLineEdit(self.UserLogin)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pass_enter.setFont(font)
        self.pass_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_enter.setObjectName("pass_enter")
        self.gridLayout_5.addWidget(self.pass_enter, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.login_failed = QtWidgets.QLabel(self.UserLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_failed.sizePolicy().hasHeightForWidth())
        self.login_failed.setSizePolicy(sizePolicy)
        self.login_failed.setText("")
        self.login_failed.setObjectName("login_failed")
        self.gridLayout_4.addWidget(self.login_failed, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.UserLogin, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.User = QtWidgets.QWidget()
        self.User.setObjectName("User")
        self.gridLayout = QtWidgets.QGridLayout(self.User)
        self.gridLayout.setObjectName("gridLayout")
        self.doctor_table = QtWidgets.QTableWidget(self.User)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.doctor_table.setFont(font)
        self.doctor_table.setMidLineWidth(0)
        self.doctor_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.doctor_table.setAlternatingRowColors(False)
        self.doctor_table.setObjectName("doctor_table")
        self.doctor_table.setColumnCount(3)
        self.doctor_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.doctor_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.doctor_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.doctor_table.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.doctor_table, 0, 0, 2, 1)
        self.AccessInfo = QtWidgets.QGroupBox(self.User)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AccessInfo.setFont(font)
        self.AccessInfo.setObjectName("AccessInfo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.AccessInfo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.password0 = QtWidgets.QLabel(self.AccessInfo)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password0.setFont(font)
        self.password0.setObjectName("password0")
        self.gridLayout_2.addWidget(self.password0, 1, 0, 1, 1)
        self.access_pass = QtWidgets.QLineEdit(self.AccessInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.access_pass.setFont(font)
        self.access_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.access_pass.setObjectName("access_pass")
        self.gridLayout_2.addWidget(self.access_pass, 1, 1, 1, 1)
        self.user_name0 = QtWidgets.QLabel(self.AccessInfo)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_name0.setFont(font)
        self.user_name0.setObjectName("user_name0")
        self.gridLayout_2.addWidget(self.user_name0, 0, 0, 1, 1)
        self.access_user = QtWidgets.QLineEdit(self.AccessInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.access_user.setFont(font)
        self.access_user.setObjectName("access_user")
        self.gridLayout_2.addWidget(self.access_user, 0, 1, 1, 1)
        self.user_login_btn = QtWidgets.QPushButton(self.AccessInfo)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_login_btn.setFont(font)
        self.user_login_btn.setObjectName("user_login_btn")
        self.gridLayout_2.addWidget(self.user_login_btn, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.AccessInfo, 0, 1, 1, 1)
        self.EditUser = QtWidgets.QGroupBox(self.User)
        self.EditUser.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.EditUser.setFont(font)
        self.EditUser.setObjectName("EditUser")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.EditUser)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.user_name1 = QtWidgets.QLabel(self.EditUser)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_name1.setFont(font)
        self.user_name1.setAcceptDrops(False)
        self.user_name1.setObjectName("user_name1")
        self.gridLayout_3.addWidget(self.user_name1, 0, 0, 1, 1)
        self.password1 = QtWidgets.QLabel(self.EditUser)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.password1.setFont(font)
        self.password1.setObjectName("password1")
        self.gridLayout_3.addWidget(self.password1, 2, 0, 1, 1)
        self.edit_user = QtWidgets.QLineEdit(self.EditUser)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.edit_user.setFont(font)
        self.edit_user.setObjectName("edit_user")
        self.gridLayout_3.addWidget(self.edit_user, 0, 1, 1, 1)
        self.email1 = QtWidgets.QLabel(self.EditUser)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email1.setFont(font)
        self.email1.setObjectName("email1")
        self.gridLayout_3.addWidget(self.email1, 1, 0, 1, 1)
        self.edit_email = QtWidgets.QLineEdit(self.EditUser)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.edit_email.setFont(font)
        self.edit_email.setObjectName("edit_email")
        self.gridLayout_3.addWidget(self.edit_email, 1, 1, 1, 1)
        self.edit_pass = QtWidgets.QLineEdit(self.EditUser)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.edit_pass.setFont(font)
        self.edit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_pass.setObjectName("edit_pass")
        self.gridLayout_3.addWidget(self.edit_pass, 2, 1, 1, 1)
        self.edit_user_btn = QtWidgets.QPushButton(self.EditUser)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.edit_user_btn.setFont(font)
        self.edit_user_btn.setObjectName("edit_user_btn")
        self.gridLayout_3.addWidget(self.edit_user_btn, 4, 1, 1, 1)
        self.reedit_pass = QtWidgets.QLineEdit(self.EditUser)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.reedit_pass.setFont(font)
        self.reedit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reedit_pass.setObjectName("reedit_pass")
        self.gridLayout_3.addWidget(self.reedit_pass, 3, 1, 1, 1)
        self.Repassword1 = QtWidgets.QLabel(self.EditUser)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Repassword1.setFont(font)
        self.Repassword1.setObjectName("Repassword1")
        self.gridLayout_3.addWidget(self.Repassword1, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.EditUser, 1, 1, 1, 1)
        self.tabWidget.addTab(self.User, "")
        self.Patients = QtWidgets.QWidget()
        self.Patients.setObjectName("Patients")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.Patients)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.patient_table = QtWidgets.QTableWidget(self.Patients)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.patient_table.setFont(font)
        self.patient_table.setMidLineWidth(0)
        self.patient_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.patient_table.setAlternatingRowColors(False)
        self.patient_table.setObjectName("patient_table")
        self.patient_table.setColumnCount(4)
        self.patient_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.patient_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.patient_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.patient_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.patient_table.setHorizontalHeaderItem(3, item)
        self.gridLayout_21.addWidget(self.patient_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Patients, "")
        self.Records = QtWidgets.QWidget()
        self.Records.setObjectName("Records")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Records)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.record_table = QtWidgets.QTableWidget(self.Records)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.record_table.setFont(font)
        self.record_table.setMidLineWidth(0)
        self.record_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.record_table.setAlternatingRowColors(False)
        self.record_table.setObjectName("record_table")
        self.record_table.setColumnCount(6)
        self.record_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.record_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.record_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.record_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.record_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.record_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.record_table.setHorizontalHeaderItem(5, item)
        self.gridLayout_7.addWidget(self.record_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Records, "")
        self.Reports = QtWidgets.QWidget()
        self.Reports.setObjectName("Reports")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.Reports)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.Reports)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.category_combo0 = QtWidgets.QComboBox(self.tab_10)
        self.category_combo0.setObjectName("category_combo0")
        self.category_combo0.addItem("")
        self.gridLayout_26.addWidget(self.category_combo0, 1, 0, 1, 1)
        self.Catergories0 = QtWidgets.QLabel(self.tab_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Catergories0.setFont(font)
        self.Catergories0.setObjectName("Catergories0")
        self.gridLayout_26.addWidget(self.Catergories0, 0, 0, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_26, 0, 0, 1, 1)
        self.ppm_table = QtWidgets.QTableWidget(self.tab_10)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ppm_table.setFont(font)
        self.ppm_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ppm_table.setObjectName("ppm_table")
        self.ppm_table.setColumnCount(8)
        self.ppm_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Courier New")
        item.setFont(font)
        self.ppm_table.setHorizontalHeaderItem(7, item)
        self.gridLayout_27.addWidget(self.ppm_table, 1, 0, 1, 1)
        self.ppm_save_btn = QtWidgets.QPushButton(self.tab_10)
        self.ppm_save_btn.setObjectName("ppm_save_btn")
        self.gridLayout_27.addWidget(self.ppm_save_btn, 2, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_10, "")
        self.gridLayout_28.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Reports, "")
        self.gridLayout_6.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Doctors"))
        self.UserLogin.setTitle(_translate("MainWindow", "Doctor Login"))
        self.UserName.setText(_translate("MainWindow", "Doctor Name:"))
        self.UserPassword.setText(_translate("MainWindow", "Doctor Password:"))
        self.user_enter.setPlaceholderText(_translate("MainWindow", "Enter your name"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.pass_enter.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        item = self.doctor_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.doctor_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        item = self.doctor_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        self.AccessInfo.setTitle(_translate("MainWindow", "Access User Information"))
        self.password0.setText(_translate("MainWindow", "Passward:"))
        self.access_pass.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.user_name0.setText(_translate("MainWindow", "UserName:"))
        self.access_user.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.user_login_btn.setText(_translate("MainWindow", "Login"))
        self.EditUser.setTitle(_translate("MainWindow", "Edit your data"))
        self.user_name1.setText(_translate("MainWindow", "UserName:"))
        self.password1.setText(_translate("MainWindow", "Passward:"))
        self.edit_user.setPlaceholderText(_translate("MainWindow", "Enter new username"))
        self.email1.setText(_translate("MainWindow", "E-mail:"))
        self.edit_email.setPlaceholderText(_translate("MainWindow", "Enter new email"))
        self.edit_pass.setPlaceholderText(_translate("MainWindow", "Enter new password"))
        self.edit_user_btn.setText(_translate("MainWindow", "Edit User Data"))
        self.reedit_pass.setPlaceholderText(_translate("MainWindow", "Re-enter new password"))
        self.Repassword1.setText(_translate("MainWindow", "Confirm password:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.User), _translate("MainWindow", "Doctor Details"))
        item = self.patient_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.patient_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.patient_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.patient_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Patients), _translate("MainWindow", "Patients"))
        item = self.record_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "RBC"))
        item = self.record_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "WBC"))
        item = self.record_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hgb"))
        item = self.record_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PCV"))
        item = self.record_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Platelets"))
        item = self.record_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Patient ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Records), _translate("MainWindow", "Records"))
        self.category_combo0.setItemText(0, _translate("MainWindow", "Select Category"))
        self.Catergories0.setText(_translate("MainWindow", "Categories:"))
        item = self.ppm_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Serial Number"))
        item = self.ppm_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Equipment Name"))
        item = self.ppm_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Equipment Code"))
        item = self.ppm_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Category Name"))
        item = self.ppm_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Technician Name"))
        item = self.ppm_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PPM Time"))
        item = self.ppm_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Number of PPM/Year"))
        item = self.ppm_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Error"))
        self.ppm_save_btn.setText(_translate("MainWindow", "Save"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("MainWindow", "PPM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Reports), _translate("MainWindow", "Reports"))
