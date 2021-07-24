from PySide6.QtWidgets import QWidget, \
    QPushButton, QApplication, QLineEdit, QColormap, QTextEdit, QVBoxLayout, QHBoxLayout
import sys, json

class RegistrationForm(QWidget):
    def __init__(self):
        super(RegistrationForm, self).__init__()

        # window config
        self.setWindowTitle("Registration Form")
        self.resize(400,0)

        # window contents (widgets)
        main_layout = QVBoxLayout(self)

        #first_name
        self.first_name_field = QLineEdit()
        self.first_name_field.setPlaceholderText("Írd be a keresztneved!")
        main_layout.addWidget(self.first_name_field)

        #last_name
        self.last_name_field = QLineEdit()
        self.last_name_field.setPlaceholderText("Írd be a családi neved!")
        main_layout.addWidget(self.last_name_field)

        #phone
        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("Telószám")
        main_layout.addWidget(self.phone_field)

        #address
        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("Mi a címed?")
        main_layout.addWidget(self.address_field)


        #save_button
        save_button = QPushButton("Save")
        main_layout.addWidget(save_button)


        # connect signals
        save_button.clicked.connect(self.save_action)
        self.first_name_field.textChanged.connect(self.first_name_changed)

    def save_action(self):
        # print(f"First name: {self.first_name_field.text()}")
        # print(f"Last name: {self.last_name_field.text()}")
        data_dictionary = {
            "first_name": self.first_name_field.text(),
            "last_name": self.last_name_field.text(),
            "phone": self.phone_field.text(),
            "address": self.address_field.text(),
        }

        print(data_dictionary)


    def first_name_changed(self, value):
        print(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = RegistrationForm()
    win.show()

    app.exec()
















