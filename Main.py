from module.Merchants import *
from module.Products import *
from module.customers import *
from module.Payments import *
from module.Orders import *
from module.fun import *
import sys, os, time
from pymongo import *

merah='\033[1;31m'
putih='\033[1;37m'

def menu():
    print('''
%s[+]----Menu CRUD Python With MongoDB----[+]
  [01] Merchants
  [02] Products
  [03] Customers
  [04] Payments
  [05] Orders
  [00] Exit
        ''' % (putih))
    while True:
        menu = input('%s Insert Option >> %s' % (merah,putih))
        if menu == '01' or menu == '1':
            os.system("clear")
            Merchants()
        elif menu == '02' or menu == '2':
            os.system("clear")
            Products()
        elif menu == '03' or menu == '3':
            os.system("clear")
            customers()
        elif menu == '04' or menu == '4':
            os.system("clear")

        elif menu == '05' or menu == '5':
            os.system("clear")
            
        elif menu == '00' or menu == '0':
            print('%sBye' % (putih))
            sys.exit(2)
        else:
            print(' Input Error %s' % (menu))


if __name__ == '__main__':
    time.sleep(3)
    os.system("clear")
    menu()