from PyQt5.QtWidgets import QApplication

from pages.app import App

app = QApplication([])
window = App()
window.showMaximized()
app.exec_()