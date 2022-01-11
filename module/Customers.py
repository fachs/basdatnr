from pymongo import *
import sys, os, time
import datetime

merah='\033[1;31m'
putih='\033[1;37m'

class MongoDB_Python:
    def __init__(self):
        # Initialize the connection on the data base.
        self.conn = MongoClient('mongodb+srv://basdatnr:basdatnr@cluster0.45x5b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self.db = self.conn.dbzalora01       # Data Base name:  TestDB
        self.cursor = self.db.Customers # Collection name: collection
        
    def create(self, query={}):
        # Insert a new register.
        self.cursor.insert_many(query)
        
    def read(self, query={}):
        # Read all the register.
        for value in self.cursor.find(query):
            print(value)
        
    def update(self, query_1={}, query_2={}):
        
        # Change the first item on the list.
        self.cursor.update_one(query_1, query_2)
    
    def delete(self, query={}):
        self.cursor.delete_one(query)

def menu():
    print('''
%s[+]----Menu CRUD Python With MongoDB----[+]
  [01] Create Order
  [02] Read Order
  [03] Update Order
  [04] Delete Order
  [00] Exit
        ''' % (putih))
    while True:
        menu = input('%s Insert Option >> %s' % (merah,putih))
        if menu == '01' or menu == '1':
            os.system("clear")
            id = (input("id :" ))
            nama = (input("Nama : "))
            email = (input("Email : "))
            print("Tanggal Lahir")
            tahun = int(input("- Tahun : "))
            bulan = int(input("- Bulan : "))
            tanggal = int(input("- Tanggal : "))
            password = (input("password : "))
            nomor_ponsel = (input("nomor ponsel : "))
            print("\nData Alamat")
            name = (input("- atas nama : "))
            phone = (input("- nomor ponsel : "))
            alamat = (input("- alamat : "))
            kode_pos = int(input("- kode pos : "))
            print("\nData Voucher")
            id_voucher = (input("id voucher : "))
            kode = (input("kode voucher : "))
            nilai = int(input("nilai voucher : "))
            jenis = (input("jenis voucher : "))
            print("\nMasa Berlaku")
            year = int(input("- Tahun : "))
            month = int(input("- Bulan : "))
            day = int(input("- Tanggal : "))
            status = (input("status voucher : "))
            birthday = datetime.datetime(tahun, bulan, tanggal)
            expire = datetime.datetime(year, month, day)

            mongo.create([{'_id' : id, 'nama' : nama, 'email' : email, 'tanggal_lahir' : birthday, 'password' : password, 'nomor_ponsel' : nomor_ponsel, 'alamat_pengiriman': { 'nama' : name, 'nomor_ponsel' : phone, 'alamat' : alamat, 'kode_pos' : kode_pos}, 'voucher' : { 'id_voucher' : id_voucher, 'kode' : kode, 'nilai' : nilai, 'jenis': jenis, 'masa_berlaku' : expire, 'status' : status} }])
        
        elif menu == '02' or menu == '2':
            os.system("clear")
            mongo.read()
        elif menu == '03' or menu == '3':
            os.system("clear")
            id = int(input("id : "))
            key = (input("key : "))
            old = (input("old value : "))
            new = (input("new value : "))
            
            mongo.update({'_id':id, key: old}, {'$set':{key:new}})
            
        elif menu == '04' or menu == '4':
            os.system("clear")
            
            id = int(input("id yang akan dihapus : "))
            
            mongo.delete({'_id':id})
            
        elif menu == '00' or menu == '0':
            print('%sBye' % (putih))
            sys.exit(2)
        else:
            print(' Input Error %s' % (menu))


if __name__ == '__main__':
    mongo = MongoDB_Python()
    time.sleep(3)
    os.system("clear")
    menu()