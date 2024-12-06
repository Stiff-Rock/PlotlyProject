from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

app = QApplication([])
window = QMainWindow()
webview = QWebEngineView()
webview.setUrl("http://127.0.0.1:5000")  # Load local HTML file
window.setCentralWidget(webview)
window.show()
app.exec()