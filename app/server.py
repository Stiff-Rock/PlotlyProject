from threading import Thread
from waitress import serve

class Server:
    def __init__(self, app):
        self.app = app
        self.server_thread = Thread(target=self.run_server, daemon=True)
        self.server_thread.start()

    def run_server(self):
        serve(self.app, host='127.0.0.1', port=5000)