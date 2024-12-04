import logging
from multiprocessing import Process
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from app import create_app
from waitress import serve
from PySide6.QtGui import QIcon

def create_browser_window():
    app = QApplication([])
    window = QMainWindow()
    webview = QWebEngineView()
    webview.setUrl("http://127.0.0.1:5000")
    window.setCentralWidget(webview)
    window.resize(1024, 720)
    window.setWindowTitle("Plotly Project")
    window.setWindowIcon(QIcon('app/static/img/icon.png'))

    screen = app.primaryScreen()
    screen_geometry = screen.availableGeometry()
    screen_center = screen_geometry.center()
    window.move(screen_center - window.rect().center())

    window.closeEvent = lambda event : stop_server(event) 

    window.show()
    app.exec()

def run_server():
    serve(app, host='0.0.0.0', port=5000)

def stop_server(event):
    logging.info("Server has stopped.")
    server_process.terminate()
    event.accept()

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    server_process = Process(target=run_server)
    server_process.start()

    create_browser_window()

    server_process.join()
    print("Application closed")
