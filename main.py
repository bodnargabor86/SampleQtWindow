from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, \
    QPushButton, QVBoxLayout, QTextEdit
import sys, json, os

DATA_FILE_PATH = "user_data.json"


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        # window config
        self.setWindowTitle("Registration Form")
        self.resize(400, 0)

        # window content (widgets)
        main_layout = QVBoxLayout(self)

        # first name
        self.first_name_field = QLineEdit()
        self.first_name_field.setPlaceholderText("First name")
        main_layout.addWidget(self.first_name_field)

        # last name
        self.last_name_field = QLineEdit()
        self.last_name_field.setPlaceholderText("Last name")
        main_layout.addWidget(self.last_name_field)

        # phone
        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("Phone")
        main_layout.addWidget(self.phone_field)

        # address
        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("Address")
        main_layout.addWidget(self.address_field)

        # email
        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Email")
        main_layout.addWidget(self.email_field)

        # about
        self.about_field = QTextEdit()
        main_layout.addWidget(self.about_field)

        # save button
        save_button = QPushButton("Save")
        main_layout.addWidget(save_button)

        # load saved data
        self.load_action()

        # connect signals/slot mechanism
        save_button.clicked.connect(self.save_action)

    def save_action(self):
        # get data from fields
        data_dictionary = {
            "first_name": self.first_name_field.text(),
            "last_name": self.last_name_field.text(),
            "phone": self.phone_field.text(),
            "email": self.email_field.text(),
            "address": self.address_field.text()
        }

        # write out data
        with open(DATA_FILE_PATH, "w") as f:
            json.dump(data_dictionary, f)

        # clear fields
        self.first_name_field.clear()
        self.last_name_field.clear()
        self.phone_field.clear()
        self.email_field.clear()
        self.address_field.clear()

    def load_action(self):
        if os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH) as f:
                user_data = json.load(f)

                self.first_name_field.setText(user_data["first_name"])
                self.last_name_field.setText(user_data["last_name"])
                self.email_field.setText(user_data["email"])
                self.phone_field.setText(user_data["phone"])
                self.address_field.setText(user_data["address"])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()

    app.exec()
