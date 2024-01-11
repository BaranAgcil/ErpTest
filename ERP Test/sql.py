import pyodbc
def baglanti():
    try:
        server = 'LAPTOP-3G8AC69T\SQLEXPRESS01'
        database = 'urunler'
        driver = 'ODBC Driver 17 for SQL Server'
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        baglanti = pyodbc.connect(conn_str)
        return baglanti
    except pyodbc.Error as hata:
        return None

