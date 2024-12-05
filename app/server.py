import logging
from multiprocessing import Process
from waitress import serve

class Server:
    def __init__(self, app):
        self.app = app
        self.server_process = Process(target=self.run_server)
        self.server_process.start()

    def run_server(self):
        serve(self.app, host='127.0.0.1', port=5000)

    def stop_server(self, event):
        if self.server_process.is_alive():
            self.server_process.terminate()
            self.server_process.join()
            logging.info("Server has stopped.")
        event.accept()
