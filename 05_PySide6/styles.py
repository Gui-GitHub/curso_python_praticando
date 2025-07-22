# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
# pip install pyqtdarktheme

import qdarktheme

qss = """
QPushButton {
    background-color: #1e8eb0;
    color: #fff;
    border-radius: 8px;
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #16488a;
}
QLineEdit {
    padding: 6px;
    border: 1px solid #1e8eb0;
    border-radius: 6px;
    font-size: 16px;
}
QListWidget {
    background: #222;
    color: #fff;
    font-size: 16px;
}
"""

def setupTheme():
    from PySide6.QtWidgets import QApplication
    QApplication.instance().setStyleSheet(
        qdarktheme.load_stylesheet() + qss
    )