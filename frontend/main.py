from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
import sys
from frontend.config import SUBSCRIPTION_ENABLED
from frontend.services import get_tip_of_the_day, get_screen_time

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Wellness Tracker")
        self.setFixedSize(420, 300)

        self.layout = QVBoxLayout()
        self.screen_time_label = QLabel("Screen Time: Loading...")
        self.tip_label = QLabel("Tip of the Day: Loading...")
        self.refresh_button = QPushButton("Refresh")
        self.settings_button = QPushButton("Subscription Status")

        self.layout.addWidget(self.screen_time_label)
        self.layout.addWidget(self.tip_label)
        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.settings_button)
        self.setLayout(self.layout)

        self.refresh_button.clicked.connect(self.update_dashboard)
        self.settings_button.clicked.connect(self.show_subscription_status)

        self.update_dashboard()

    def update_dashboard(self):
        self.screen_time_label.setText(f"Screen Time: {get_screen_time()}")
        self.tip_label.setText(f"Tip of the Day: {get_tip_of_the_day()}")



    def show_subscription_status(self):
        current = get_premium_status()
        updated = toggle_premium()
        QMessageBox.information(self, "Subscription", f"Toggled: {'ON' if updated else 'OFF'}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())
