import tkinter as tk
from sql import baglanti
conn = baglanti()


class ShoppingWindowTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Alışveriş Penceresi")
        self.root.geometry("400x300")
        
        self.layout = tk.Frame(root)
        self.layout.pack()
        
        self.customer_buttons = []
        self.product_buttons = []
        
        self.load_customers()
        self.load_products()
    
    def load_customers(self):
        connection = baglanti()
        cursor = connection.cursor()
        
        cursor.execute("SELECT isim FROM Customers")
        customers = cursor.fetchall()
        
        for customer in customers:
            customer_name = customer[0]
            button = tk.Button(self.layout, text=customer_name, command=lambda name=customer_name: self.customer_selected(name))
            button.pack()
            self.customer_buttons.append(button)
        
        connection.close()
    
    def load_products(self):
        connection = baglanti()
        cursor = connection.cursor()
        
        cursor.execute("SELECT urun_isim FROM Urunler")
        products = cursor.fetchall()
        
        for product in products:
            product_name = product[0]
            button = tk.Button(self.layout, text=product_name, command=lambda name=product_name: self.product_selected(name))
            button.pack()
            self.product_buttons.append(button)
        
        connection.close()
    
    def customer_selected(self, name):
        self.selected_customer = name
        print(f"Seçilen müşteri: {name}")
    
    def product_selected(self, name):
        self.selected_product = name
        print(f"Seçilen ürün: {name}")
        
        self.insert_into_shopping_table()
    
    def insert_into_shopping_table(self):
        connection = baglanti()
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO alisveris (musteri, urun) VALUES (?, ?)", (self.selected_customer, self.selected_product))
        connection.commit()
        connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    window = ShoppingWindowTkinter(root)
    root.mainloop()
