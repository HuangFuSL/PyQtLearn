import sys

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow

from .ui_form import Ui_Main


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.counter = 0

    def repaint(self):
        self.ui.label.setText(f'{self.counter}')

    @Slot()
    def on_pushButton_clicked(self):
        self.counter += 1
        self.repaint()

    @Slot()
    def on_pushButton2_clicked(self):
        self.counter = 0
        self.repaint()

    @Slot()
    def on_pushButton3_clicked(self):
        self.counter -= 1
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
