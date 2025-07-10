# frontend/main.py

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
import sys

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Wellness Tracker")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.tip_label = QLabel("Tip of the Day: Stay hydrated.")
        self.tip_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.tip_label)

        self.screen_time_label = QLabel("Screen Time: 0h 0m")
        self.screen_time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.screen_time_label)

        self.refresh_button = QPushButton("Refresh")
        layout.addWidget(self.refresh_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())
