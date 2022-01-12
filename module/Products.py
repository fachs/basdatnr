from pymongo import *
import sys, os, time

merah='\033[1;31m'
putih='\033[1;37m'

class MongoDB_Python:
    def __init__(self):
        # Initialize the connection on the data base.
        self.conn = MongoClient('mongodb+srv://basdatnr:basdatnr@cluster0.45x5b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self.db = self.conn.dbzalora01       # Data Base name:  TestDB
        self.cursor = self.db.Products # Collection name: collection
        
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
  [01] Create Product
  [02] Read Product
  [03] Update Product
  [04] Delete Product
  [00] Exit
        ''' % (putih))
    while True:
        menu = input('%s Insert Option >> %s' % (merah,putih))
        if menu == '01' or menu == '1':
            os.system("clear")
            id_merchant = int(input("id_merchant: "))
            id = int(input("id : "))
            nama_barang = (input("nama_barang : "))
            kategori = (input("kategori : "))
            harga = int(input("harga : "))
            stok = int(input("stok : "))
            deskripsi = (input("deskripsi : "))
            gambar_barang = (input("gambar_barang : "))
            input_string = input('komentar (pisahkan dengan spasi jika lebih dari satu) : ')
            komentar = input_string.split()
            rating = float(input("rating : "))
            
            mongo.create([{ 'id_merchant': id_merchant, '_id': id, 'nama_barang': nama_barang, 'kategori': kategori, 'harga': harga,'stok' : stok,'deskripsi' : deskripsi,'gambar_barang' : gambar_barang,'ulasan':  { 'komentar': komentar, 'rating': rating} }])
        elif menu == '02' or menu == '2':
            os.system("clear")
            mongo.read()
        elif menu == '03' or menu == '3':
            os.system("clear")
            id = int(input("id : "))
            key = (input("key : "))
            new = (input("new value : "))
            
            mongo.update({'_id':id}, {'$set':{key:new}})
            
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