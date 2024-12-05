from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QWidget):
    def __init__(self, server_instance):
        self.server_instance = server_instance

        super().__init__()
        self.setWindowTitle('Loading Window')
        self.resize(200, 100)

        self.label = QLabel('loading...', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        QTimer.singleShot(3000, self.create_browser_self)

    def create_browser_self(self):
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
