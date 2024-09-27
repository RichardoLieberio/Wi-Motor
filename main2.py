from PyQt5.QtWidgets import *
from PyQt5 import uic

# class NoScrollArea(QScrollArea):
#     def wheelEvent(self, event):
#         event.ignore()

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('GUI.ui', self)

        self.showMaximized()

        # Create a widget to hold the body layout
        self.scroll_content = QWidget()
        self.body_layout = QVBoxLayout(self.scroll_content)
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_layout.setSpacing(0)

        # Set the scrollable area
        self.scroll_area = self.findChild(QScrollArea, 'scrollArea')
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setContentsMargins(0, 0, 0, 0)

        for i in range (1, 31):
            self.__generate_row__(i)

    def __generate_row__(self, i):
        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)

        no = QLabel(f'{i}')
        kode = QLabel("KODE/003")
        nama = QLabel("Oli MPX2 0.8L")
        kuantiti = QLabel("13")
        kelola = QLabel("Kelola")

        h_layout.addWidget(no)
        h_layout.addWidget(kode)
        h_layout.addWidget(nama)
        h_layout.addWidget(kuantiti)
        h_layout.addWidget(kelola)

        h_layout.setStretch(0, 0)
        h_layout.setStretch(1, 1)
        h_layout.setStretch(2, 2)
        h_layout.setStretch(3, 0)
        h_layout.setStretch(4, 0)

        no.setMinimumWidth(70)
        no.setMinimumWidth(70)
        kuantiti.setMinimumWidth(100)
        kuantiti.setMaximumWidth(100)
        kelola.setMinimumWidth(250)
        kelola.setMaximumWidth(250)

        odd_style = '''
            padding: 8px 8px;
	        font-size: 16px;
	        color: rgb(50, 50, 50);
	        background-color: rgb(255, 255, 255);
        '''

        even_style = '''
            padding: 8px 8px;
	        font-size: 16px;
	        color: rgb(50, 50, 50);
	        background-color: rgb(240, 240, 240);
        '''

        if (i % 2):
            no.setStyleSheet(odd_style)
            kode.setStyleSheet(odd_style)
            nama.setStyleSheet(odd_style)
            kuantiti.setStyleSheet(odd_style)
            kelola.setStyleSheet(odd_style)
        else:
            no.setStyleSheet(even_style)
            kode.setStyleSheet(even_style)
            nama.setStyleSheet(even_style)
            kuantiti.setStyleSheet(even_style)
            kelola.setStyleSheet(even_style)

        # self.body.addLayout(h_layout)
        self.body_layout.addLayout(h_layout)

def main():
    app = QApplication([])
    window = GUI()
    app.exec_()

if __name__ == "__main__":
    main()