from PyQt5.QtWidgets import QApplication

from pages.app import App

app = QApplication([])
window = App()
app.exec_()