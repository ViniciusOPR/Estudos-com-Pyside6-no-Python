import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

# from styles import setupTheme

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)


    display = Display()
    window.addWidgetToVLayout(display)


    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    buttonsgrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsgrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()