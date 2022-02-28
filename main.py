import sys

from ui_main import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget


class SimpleN2N(QWidget, Ui_Form):
    def __init__(self):
        super(SimpleN2N, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SimpleN2N()
    main.show()
    sys.exit(app.exec())
