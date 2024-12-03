
const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const http = require('http');

const pythonPath = path.join(__dirname, '..', '..', 'run.py');
let flaskApp = null;

const checkFlaskReady = () => {
  return new Promise((resolve) => {
    const interval = setInterval(() => {
      http.get('http://127.0.0.1:5000', (res) => {
        if (res.statusCode === 200) {
          clearInterval(interval);
          resolve();
        }
      }).on('error', () => {
      });
    }, 500); 
  });
};

const startFlaskApp = () => {
    flaskApp = spawn('python', ['-m', 'waitress', '--listen=127.0.0.1:5000', 'run:app'], {
        detached: true,
        stdio: ['ignore', 'pipe', 'pipe']
    });

    flaskApp.stdout.on('data', (data) => {
        console.log(`Flask stdout: ${data}`);
    });

    flaskApp.stderr.on('data', (data) => {
        console.error(`Flask stderr: ${data}`);
    });

    flaskApp.unref();
};

const createWindow = () => {
  const win = new BrowserWindow({
    width: 1024,
    height: 768,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    }
  });

  win.loadURL('http://127.0.0.1:5000');
};

app.whenReady().then(() => {
  startFlaskApp();

  checkFlaskReady()
    .then(() => {
      createWindow();
    })
    .catch((error) => {
      console.error(`Error al conectar con Flask: ${error}`);
      app.quit();
    });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    if (flaskApp) {
      flaskApp.kill();
    }
    app.quit();
  }
});

