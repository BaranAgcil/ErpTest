import tkinter as tk
from sql import baglanti
conn = baglanti()

def urun_ekle():
   
    urun_ismi = urun_ismi_entry.get()
    urun_adeti = urun_adeti_entry.get()
    urun_fiyati = urun_fiyati_entry.get()

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Urunler (urun_isim, adet, fiyat) VALUES (?, ?, ?)",
                   (urun_ismi, urun_adeti, urun_fiyati))
    conn.commit()

def musteri_ekle():
    
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    yas = yas_entry.get()

    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (isim, soyisim, yas) VALUES (?, ?, ?)",
                   (ad, soyad, yas))
    conn.commit()


root = tk.Tk()
root.title("Ürün ve Müşteri Ekle")


urun_frame = tk.Frame(root)
urun_frame.pack()
root.geometry("600x400")
urun_ismi_label = tk.Label(urun_frame, text="Ürün İsmi:")
urun_ismi_label.pack()
urun_ismi_entry = tk.Entry(urun_frame)
urun_ismi_entry.pack()

urun_adeti_label = tk.Label(urun_frame, text="Ürün Adeti:")
urun_adeti_label.pack()
urun_adeti_entry = tk.Entry(urun_frame)
urun_adeti_entry.pack()

urun_fiyati_label = tk.Label(urun_frame, text="Ürün Fiyatı:")
urun_fiyati_label.pack()
urun_fiyati_entry = tk.Entry(urun_frame)
urun_fiyati_entry.pack()

urun_ekle_btn = tk.Button(urun_frame, text="Ekle", command=urun_ekle)
urun_ekle_btn.pack()


musteri_frame = tk.Frame(root)
musteri_frame.pack()

ad_label = tk.Label(musteri_frame, text="Ad:")
ad_label.pack()
ad_entry = tk.Entry(musteri_frame)
ad_entry.pack()

soyad_label = tk.Label(musteri_frame, text="Soyad:")
soyad_label.pack()
soyad_entry = tk.Entry(musteri_frame)
soyad_entry.pack()

yas_label = tk.Label(musteri_frame, text="Yaş:")
yas_label.pack()
yas_entry = tk.Entry(musteri_frame)
yas_entry.pack()

musteri_ekle_btn = tk.Button(musteri_frame, text="Ekle", command=musteri_ekle)
musteri_ekle_btn.pack()

root.mainloop()
