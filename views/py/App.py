# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_App.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 683)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("#side_menu {\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"#side_menu QPushButton {\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"    color: rgb(255, 255, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"#side_menu QPushButton:checked {\n"
"    padding-left: 8px;\n"
"    background-color: rgb(73, 0, 131);\n"
"    border-left: 4px solid rgb(133, 0, 237);\n"
"}\n"
"\n"
"#side_menu QPushButton:hover {\n"
"    background-color: rgb(88, 0, 169) !important;\n"
"}\n"
"\n"
"#main_page {\n"
"    background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: none;\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.side_menu.setStyleSheet("")
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 24)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wimotor = QtWidgets.QLabel(self.side_menu)
        self.wimotor.setText("")
        self.wimotor.setTextFormat(QtCore.Qt.AutoText)
        self.wimotor.setPixmap(QtGui.QPixmap(":/Menu/assets/wimotor.jpeg"))
        self.wimotor.setObjectName("wimotor")
        self.verticalLayout.addWidget(self.wimotor)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.menu_list = QtWidgets.QWidget(self.side_menu)
        self.menu_list.setObjectName("menu_list")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_list)
        self.verticalLayout_2.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gudang_menu = QtWidgets.QPushButton(self.menu_list)
        self.gudang_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Menu/assets/Warehouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gudang_menu.setIcon(icon)
        self.gudang_menu.setCheckable(True)
        self.gudang_menu.setAutoExclusive(True)
        self.gudang_menu.setObjectName("gudang_menu")
        self.verticalLayout_2.addWidget(self.gudang_menu)
        self.bon_menu = QtWidgets.QPushButton(self.menu_list)
        self.bon_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Menu/assets/Recipe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bon_menu.setIcon(icon1)
        self.bon_menu.setCheckable(True)
        self.bon_menu.setAutoExclusive(True)
        self.bon_menu.setObjectName("bon_menu")
        self.verticalLayout_2.addWidget(self.bon_menu)
        self.mekanik_menu = QtWidgets.QPushButton(self.menu_list)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Menu/assets/Mechanic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mekanik_menu.setIcon(icon2)
        self.mekanik_menu.setCheckable(True)
        self.mekanik_menu.setAutoExclusive(True)
        self.mekanik_menu.setObjectName("mekanik_menu")
        self.verticalLayout_2.addWidget(self.mekanik_menu)
        self.verticalLayout.addWidget(self.menu_list)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_page = QtWidgets.QStackedWidget(self.centralwidget)
        self.main_page.setObjectName("main_page")
        self.gudang_page = QtWidgets.QWidget()
        self.gudang_page.setStyleSheet("#cari_barang_label {\n"
"    font-size: 14px;\n"
"    color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"#cari_barang_input {\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"#cari_barang_input:hover {\n"
"    border: 1px solid rgb(73, 0, 131);\n"
"}\n"
"\n"
"#cari_barang_input:focus {\n"
"    border: 1px solid rgb(133, 0, 237);\n"
"}\n"
"\n"
"#tambah_barang_btn {\n"
"    padding: 5px 0;\n"
"    font-size: 14px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(88, 0, 169);\n"
"    border: 1px solid  rgb(88, 0, 169);\n"
"}\n"
"\n"
"#tambah_barang_btn:hover {\n"
"    background-color: rgb(69, 0, 133);\n"
"}\n"
"\n"
"#gudang_table_header {\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"#gudang_table_header QLabel {\n"
"    font-size: 14px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.gudang_page.setObjectName("gudang_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gudang_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gudang_scroll = QtWidgets.QScrollArea(self.gudang_page)
        self.gudang_scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gudang_scroll.setWidgetResizable(True)
        self.gudang_scroll.setObjectName("gudang_scroll")
        self.gudang_scroll_area = QtWidgets.QWidget()
        self.gudang_scroll_area.setGeometry(QtCore.QRect(0, 0, 820, 683))
        self.gudang_scroll_area.setObjectName("gudang_scroll_area")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gudang_scroll_area)
        self.verticalLayout_6.setContentsMargins(32, 32, 32, 32)
        self.verticalLayout_6.setSpacing(24)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gudang_header = QtWidgets.QWidget(self.gudang_scroll_area)
        self.gudang_header.setObjectName("gudang_header")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.gudang_header)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cari_barang_label = QtWidgets.QLabel(self.gudang_header)
        self.cari_barang_label.setObjectName("cari_barang_label")
        self.horizontalLayout_5.addWidget(self.cari_barang_label)
        self.cari_barang_input = QtWidgets.QLineEdit(self.gudang_header)
        self.cari_barang_input.setMinimumSize(QtCore.QSize(200, 0))
        self.cari_barang_input.setInputMask("")
        self.cari_barang_input.setObjectName("cari_barang_input")
        self.horizontalLayout_5.addWidget(self.cari_barang_input)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.tambah_barang_btn = QtWidgets.QPushButton(self.gudang_header)
        self.tambah_barang_btn.setMinimumSize(QtCore.QSize(160, 0))
        self.tambah_barang_btn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.tambah_barang_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tambah_barang_btn.setObjectName("tambah_barang_btn")
        self.horizontalLayout_5.addWidget(self.tambah_barang_btn)
        self.verticalLayout_6.addWidget(self.gudang_header)
        self.gudang_body = QtWidgets.QWidget(self.gudang_scroll_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gudang_body.sizePolicy().hasHeightForWidth())
        self.gudang_body.setSizePolicy(sizePolicy)
        self.gudang_body.setObjectName("gudang_body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gudang_body)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gudang_table_header = QtWidgets.QWidget(self.gudang_body)
        self.gudang_table_header.setMinimumSize(QtCore.QSize(0, 0))
        self.gudang_table_header.setObjectName("gudang_table_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gudang_table_header)
        self.horizontalLayout_2.setContentsMargins(8, 11, 8, 11)
        self.horizontalLayout_2.setSpacing(32)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.no_label = QtWidgets.QLabel(self.gudang_table_header)
        self.no_label.setMinimumSize(QtCore.QSize(40, 0))
        self.no_label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.no_label.setObjectName("no_label")
        self.horizontalLayout_2.addWidget(self.no_label)
        self.kode_label = QtWidgets.QLabel(self.gudang_table_header)
        self.kode_label.setMinimumSize(QtCore.QSize(90, 0))
        self.kode_label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.kode_label.setObjectName("kode_label")
        self.horizontalLayout_2.addWidget(self.kode_label)
        self.nama_label = QtWidgets.QLabel(self.gudang_table_header)
        self.nama_label.setMinimumSize(QtCore.QSize(250, 0))
        self.nama_label.setObjectName("nama_label")
        self.horizontalLayout_2.addWidget(self.nama_label)
        self.kuantiti_label = QtWidgets.QLabel(self.gudang_table_header)
        self.kuantiti_label.setMinimumSize(QtCore.QSize(70, 0))
        self.kuantiti_label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.kuantiti_label.setObjectName("kuantiti_label")
        self.horizontalLayout_2.addWidget(self.kuantiti_label)
        self.kelola_label = QtWidgets.QLabel(self.gudang_table_header)
        self.kelola_label.setMinimumSize(QtCore.QSize(160, 0))
        self.kelola_label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.kelola_label.setObjectName("kelola_label")
        self.horizontalLayout_2.addWidget(self.kelola_label)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout_4.addWidget(self.gudang_table_header)
        self.gudang_table_body = QtWidgets.QVBoxLayout()
        self.gudang_table_body.setSpacing(0)
        self.gudang_table_body.setObjectName("gudang_table_body")
        self.verticalLayout_4.addLayout(self.gudang_table_body)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addWidget(self.gudang_body)
        self.gudang_scroll.setWidget(self.gudang_scroll_area)
        self.verticalLayout_3.addWidget(self.gudang_scroll)
        self.main_page.addWidget(self.gudang_page)
        self.bon_page = QtWidgets.QWidget()
        self.bon_page.setStyleSheet("#bon_page_label {\n"
"    font-size: 24px;\n"
"    color: rgb(150, 150, 150);\n"
"}")
        self.bon_page.setObjectName("bon_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bon_page)
        self.horizontalLayout_3.setContentsMargins(32, 32, 32, 32)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bon_page_label = QtWidgets.QLabel(self.bon_page)
        self.bon_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bon_page_label.setObjectName("bon_page_label")
        self.horizontalLayout_3.addWidget(self.bon_page_label)
        self.main_page.addWidget(self.bon_page)
        self.mekanik_page = QtWidgets.QWidget()
        self.mekanik_page.setStyleSheet("#mekanik_page_label {\n"
"    font-size: 24px;\n"
"    color: rgb(150, 150, 150);\n"
"}")
        self.mekanik_page.setObjectName("mekanik_page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.mekanik_page)
        self.horizontalLayout_4.setContentsMargins(32, 32, 32, 32)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mekanik_page_label = QtWidgets.QLabel(self.mekanik_page)
        self.mekanik_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mekanik_page_label.setObjectName("mekanik_page_label")
        self.horizontalLayout_4.addWidget(self.mekanik_page_label)
        self.main_page.addWidget(self.mekanik_page)
        self.horizontalLayout.addWidget(self.main_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wi Motor"))
        self.gudang_menu.setText(_translate("MainWindow", "Gudang"))
        self.bon_menu.setText(_translate("MainWindow", "Bon"))
        self.mekanik_menu.setText(_translate("MainWindow", "Mekanik"))
        self.cari_barang_label.setText(_translate("MainWindow", "Cari barang"))
        self.cari_barang_input.setPlaceholderText(_translate("MainWindow", "Minimal 3 huruf"))
        self.tambah_barang_btn.setText(_translate("MainWindow", "Tambah barang"))
        self.no_label.setText(_translate("MainWindow", "No"))
        self.kode_label.setText(_translate("MainWindow", "Kode barang"))
        self.nama_label.setText(_translate("MainWindow", "Nama barang"))
        self.kuantiti_label.setText(_translate("MainWindow", "Kuantiti"))
        self.kelola_label.setText(_translate("MainWindow", "Kelola"))
        self.bon_page_label.setText(_translate("MainWindow", "Halaman belum tersedia 1"))
        self.mekanik_page_label.setText(_translate("MainWindow", "Halaman belum tersedia 2"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_App()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
