import logging
import sys
from PySide6.QtWidgets import QApplication
from app import create_app
from app.server import Server
from app.main_window import MainWindow

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app = create_app()
    server_instance = Server(app)

    app_qt = QApplication(sys.argv)

    main_window = MainWindow(server_instance)
    main_window.show()

    sys.exit(app_qt.exec())
