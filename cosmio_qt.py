import sys
from urllib import response
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout
)

import brain
import speech

class CosmioWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("COSMIO")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        self.title = QLabel("COSMIO")
        self.title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: cyan;
        """)

        self.status = QLabel("Status: Online")

        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)

        self.chat_box.append("COSMIO: Online and ready.")

        self.input_box = QLineEdit()

        self.send_button = QPushButton("Send")

        input_layout = QHBoxLayout()

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_button)

        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.chat_box)
        layout.addLayout(input_layout)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)

        self.input_box.returnPressed.connect(
            self.send_message
        )

    def send_message(self):

        user_text = self.input_box.text()

        if not user_text:
            return

        self.chat_box.append(
            
            f"You: {user_text}"
        )

        response = brain.process(user_text)

        self.chat_box.append(
            f"COSMIO: {response}\n"
        )

        QApplication.processEvents()

        speech.speak(response)


        self.input_box.clear()


app = QApplication(sys.argv)

window = CosmioWindow()

window.show()

sys.exit(app.exec())