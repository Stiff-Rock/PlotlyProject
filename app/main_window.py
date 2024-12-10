from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self, server_instance):
        self.server_instance = server_instance

        super().__init__()
        self.resize(1024, 720)
        self.setWindowTitle("Plotly Project")
        self.setWindowIcon(QIcon('app/static/img/icon.png'))

        webview = QWebEngineView()
        webview.setUrl("http://127.0.0.1:5000")

        layout = QVBoxLayout()
        layout.addWidget(webview)
        self.setLayout(layout)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        self.closeEvent = lambda event : self.server_instance.stop_server(event)
