import subprocess
import sys
import time
import threading
import os

# Set root directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def start_backend():
    subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "backend.main:app", "--reload"],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def start_frontend():
    from frontend.main import DashboardWindow
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    time.sleep(2)
    start_frontend()
