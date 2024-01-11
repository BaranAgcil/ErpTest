import pyodbc
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
import sys
from sql import baglanti

class CustomerTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Müşteri Takip')
        self.layout = QVBoxLayout()

        
        conn = baglanti()
        cursor = conn.cursor()

        
        cursor.execute("SELECT musteri FROM alisveris")
        customers = cursor.fetchall()

        
        for customer in customers:
            customer_button = QPushButton(customer[0])
            customer_button.clicked.connect(lambda _, cust=customer[0]: self.showProducts(cust, cursor))
            self.layout.addWidget(customer_button)

        self.setLayout(self.layout)
        self.show()

    def showProducts(self, customer, cursor):
        
        cursor.execute("SELECT urun FROM alisveris WHERE musteri = ?", (customer,))
        products = cursor.fetchall()

        
        product_list = '\n'.join([product[0] for product in products])
        QMessageBox.information(self, f"{customer}'in Aldığı Ürünler", product_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomerTracker()
    window.resize(500, 300)
    window.show()
    sys.exit(app.exec_())
    