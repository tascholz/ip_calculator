import sys
from calculator import Calculator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QLineEdit, QWidget)

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.calculator = ""

        self.layout = QVBoxLayout(self)

        self.gui_ip_adress_label = QLabel("Ip adress")
        self.layout.addWidget(self.gui_ip_adress_label)
        self.gui_ip_adress = QLineEdit()
        self.layout.addWidget(self.gui_ip_adress)

        self.gui_suffix_label = QLabel("Cidr Suffix")
        self.layout.addWidget(self.gui_suffix_label)
        self.gui_suffix = QLineEdit()
        self.layout.addWidget(self.gui_suffix)

        self.submit = QPushButton("Calculate")
        self.submit.clicked.connect(self.calculate)
        self.layout.addWidget(self.submit)

        self.gui_subnet_mask_label = QLabel("Subnet Mask")
        self.gui_subnet_mask = QLineEdit()
        self.gui_subnet_mask.setReadOnly(True)
        self.layout.addWidget(self.gui_subnet_mask_label)
        self.layout.addWidget(self.gui_subnet_mask)

        self.gui_hosts_label = QLabel("Hosts")
        self.gui_hosts = QLineEdit()
        self.gui_hosts.setReadOnly(True)
        self.layout.addWidget(self.gui_hosts_label)
        self.layout.addWidget(self.gui_hosts)

        self.gui_network_adress_label = QLabel("Network adress")
        self.gui_network_adress = QLineEdit()
        self.gui_network_adress.setReadOnly(True)
        self.layout.addWidget(self.gui_network_adress_label)
        self.layout.addWidget(self.gui_network_adress)

        self.gui_first_host_label = QLabel("First host")
        self.gui_first_host = QLineEdit()
        self.gui_first_host.setReadOnly(True)
        self.layout.addWidget(self.gui_first_host_label)
        self.layout.addWidget(self.gui_first_host)

        self.gui_last_host_label = QLabel("Last host")
        self.gui_last_host = QLineEdit()
        self.gui_last_host.setReadOnly(True)
        self.layout.addWidget(self.gui_last_host_label)
        self.layout.addWidget(self.gui_last_host)

    def calculate(self):
        self.calculator = Calculator(self.gui_ip_adress.text() + "/" + self.gui_suffix.text())
        self.gui_subnet_mask.setText(self.calculator.calculate_subnet_mask().show())
        self.gui_hosts.setText(self.calculator.calculate_number_of_hosts())
        self.gui_network_adress.setText(self.calculator.calculate_network_adress().show())
        self.gui_first_host.setText(self.calculator.calculate_first_host().show())
        self.gui_last_host.setText(self.calculator.calculate_last_host().show())



if __name__ == '__main__':
    app = QApplication()

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())