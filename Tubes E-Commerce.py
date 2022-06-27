#=============================== TUBES E-COMMERCE ===============================#
import time

#LIST PRODUK====================================================
listvariasi_p =[{"Id":10001,"Nama               ": "Makaroni asin pedas   ", "Stok ":20, "Harga":15000},
                {"Id":10002,"Nama               ": "Makaroni balado       ", "Stok ":10, "Harga":13000},
                {"Id":10003,"Nama               ": "Makaroni keju         ", "Stok ":8 , "Harga":13000},
                {"Id":10004,"Nama               ": "Makaroni rendang      ", "Stok ":20, "Harga":15000},
                {"Id":20001,"Nama               ": "Basreng asin pedas    ", "Stok ":17, "Harga":15000},
                {"Id":20002,"Nama               ": "Basreng balado        ", "Stok ":8 , "Harga":13000},
                {"Id":20003,"Nama               ": "Basreng keju          ", "Stok ":5 , "Harga":13000},
                {"Id":20004,"Nama               ": "Basreng rendang       ", "Stok ":20, "Harga":15000},
                {"Id":30001,"Nama               ": "Kripik kaca asin pedas", "Stok ":25, "Harga":15000},
                {"Id":30002,"Nama               ": "Kripik kaca balado    ", "Stok ":15, "Harga":13000},
                {"Id":30003,"Nama               ": "Kripik kaca keju      ", "Stok ":10, "Harga":13000},
                {"Id":30004,"Nama               ": "Kripik kaca rendang   ", "Stok ":8 , "Harga":15000}]

temp=[]

#LOG IN========================================================

def register():
    username = input("Please enter a username: ")
    print('')
    password = input("Please enter a password: ")
    print('')
    file = open("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\accountfile3.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("Selamat! Kamu berhasil Log In")
    else:
        print("Selamat! Kamu berhasil Log In")

def login():
    x = False
    while x == False:
        username = input("Please enter your username: ")
        print('')
        password = input("Please enter your password: ")
        print('')
        for line in open("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\accountfile3.txt","r").readlines():
            login_info = line.split() 
        if username == login_info[0] and password == login_info[1]:
            print("Log In Anda berhasil!")
            return True
        
        else:
            print("Maaf, Anda gagal Log In")
            loginutama()
    print('')

def loginutama():
    print("\n", "="*25, "URNEEDS.ID", "="*25)
    print('')
    time.sleep(1)
    print(' >>Selamat Datang Kembali!Apakabar hari ini?\U0001F929<<')
    print('')
    print('-'*63)
    print('                       1. Register                      ')
    print('                                                        ')
    print('                       2. Login                         ')
    print('                                                        ')
    print('                       3. Exit                          ')
    print('-'*63)
    y = True
    while y == True:
        pilihanLoginSeller = input('Mohon masukkan no pilihan: ')
        print('')
        if pilihanLoginSeller == '1':
            register()
            break
        elif pilihanLoginSeller == '2':
            login()
            break
        elif pilihanLoginSeller == '3':
            break
        else:
            print('Hanya bisa di isi oleh 1/2/3')
            print('')

#SELLER=============================================================================

#PRODUK SELLER
def variasisel():
    print("\n")
    print("Id\tNama\t\t\tStok \t\tHarga\t")
    print("******************************************************")
    for p in listvariasi_p:
        print(f'{p["Id"]}\t{p["Nama               "]}\t{p["Stok "]}\t\t{p["Harga"]}\t')
    produksel()
    
def removeproduk(): #hanya bisa mengurangi stok nya saja 1 per1
    print("\n")
    listvariasi_Id= int(input("Masukkan Id produk yang ingin Anda hapus : "))
    found=False
    for p in listvariasi_p:
        found= p["Id"]==listvariasi_Id
        if found !=True:
            temp.append(p)
            continue
        if found==True:
            p["Stok "]-=1
    print("Menghapus....")
    if len(temp)==p:
        print(f"{listvariasi_p} data tidak ditemukan")
    else:
        print(f"{listvariasi_p} salah satu data produk telah dihapus dari list produk")
    variasisel()

def totalproduk():
    print("\n")
    Total=0
    print("\n")
    for p in listvariasi_p:
        print(f'{p["Nama               "]} = {p["Stok "]}')
        Total+=(p["Stok "])
    print("\nTotal keseluruhan stok produk Anda : ",Total)
    produksel()

def produksel():
    print("*********************")
    print("1.List produk Anda")
    print("2.Tambah produk")
    print("3.Remove produk")
    print("4.Total produk yang Anda miliki")
    print("5.Back to main room")
    print("*********************")

    pilproduk= int(input("Mohon masukkan pilihan Anda: "))
    if pilproduk==1:
        variasisel()
    elif pilproduk==2:
        n=int(input("Berapa banyak produk yang ingin Anda tambahkan? : "))
        for p in range(n):
            new_Id=int(input("Masukkan Id : "))
            new_Nama=input("Masukkan nama produk : ")
            new_Stok=int(input("Masukkan jumlah stok : "))
            new_Harga=int(input("Masukkan harga : "))
            p=[{"Id":new_Id,"Nama               ":new_Nama,"Stok ":new_Stok,"Harga":new_Harga}]
        listvariasi_p.extend(p)
        variasisel()
    elif pilproduk==3:
        removeproduk()
    elif pilproduk==4:
        totalproduk()
    elif pilproduk==5:
        return mainroom_seller() 
    else:
        print("Mohon masukkan pilihan Anda dengan benar")

#MAINROOM SELLER
def mainroom_seller():
    print("\n")
    print("="*25," >>MAIN ROOM<< ", "="*25)
    print("\n")
                
    print('''
    1. Profil toko
    2. Produk anda
    3. Pesanan hari ini
    0. EXIT (Log Out)    
    ''')
    mainroomsel =int(input("Masukkan pilihan mu: "))
    if mainroomsel== 1:
        print("\n")
        open_profil = open("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\Tubes\\profiltoko_seller.txt","r")
        read_profil = open_profil.read()

        print(read_profil)
        open_profil.close()
        mainroom_seller()
    elif mainroomsel== 2:
        produksel()
        mainroom_seller()
    elif mainroomsel== 3: #masi bermasalah disini, yg keluar malah profil toko
        open_pesanan = open("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\Tubes\\pesanan_harian.txt", "r" )
        read_pesanan = open_pesanan.read()

        print(read_pesanan)
        open_pesanan.close()
        
    elif mainroomsel==0:
        print("="*25,">>HALO! SELAMAT DATANG\U0001F929<<","="*25)

        pilihanLogIn=input("Kamu adalah?\n\nSELLER(penjual)\nBUYER(pembeli)\n:")
        if pilihanLogIn=="SELLER" or pilihanLogIn=="seller":
            loginutama()
            print("\n")
            print("*"*50)
            mainroom_seller()

        elif pilihanLogIn=="BUYER" or pilihanLogIn=="buyer":
            loginutama()
            print("\n")
            print("*"*50)
            mainroom_buyer()
    else:
        print("Mohon masukkan pilihan dengan benar")

#BUYER==============================================================================

#PILIHAN BUYER
def variasibuy():
    print("\n")
    print("Id\tNama\t\t\tStok \t\tHarga\t")
    print("******************************************************")
    for p in listvariasi_p:
        print(f'{p["Id"]}\t{p["Nama               "]}\t{p["Stok "]}\t\t{p["Harga"]}\t')
    wishlist()

def pulsa():
    print("\n")
    print("-"*10,">>Pembelian Pulsa<<","-"*10)
    nomorhp=input("Masukkan nomor hp Anda:")
    print("\n")
    nominal=input("Masukkan nominal pulsa yang Anda inginkan:")
    print("\n")
    filepulsa= open ("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\Tubes\\pulsa.txt", "a")
    filepulsa.write(nomorhp)
    filepulsa.write("\n")
    filepulsa.write(nominal)
    filepulsa.write("\n")
    filepulsa.close()
    print("Baiklah pemesanan Anda akan diproses")
    checkout()

def tiket():
    print("\n")
    print("-"*10,">>Pembelian Tiket<<","-"*10)
    tiketapa= input("Masukkan yang akan Anda pesan (pesawat/kereta api/kapal):")
    print("\n")
    asal    = input("Masukkan tempat keberangkatan Anda:")
    print("\n")
    tujuan  = input("Masukkan tempat tujuan Anda:")
    print("\n")
    filetiket= open ("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\Tubes\\pulsa.txt", "a")
    filetiket.write(tiketapa)
    filetiket.write("\n")
    filetiket.write(asal)
    filetiket.write("\n")
    filetiket.write(tujuan)
    filetiket.write("\n")
    filetiket.close()
    print("Baiklah pemesanan Anda akan diproses")
    checkout()

def checkout():
    print("\n")
    print("-"*30, ">CHECKOUT<", "-"*30)
    print('''
    -Pilih metode pembayaran Anda-
    1. PayIt
    2. BNI
    3. BRI
    4. Alfamart   
    ''')
    metode= input("Masukkan metode pembayaran yang Anda inginkan:")
    print("\n")
    noid= input("Masukkan no id Anda:")
    print("\n")
    filecheckout= open ("C:\\Users\\Indry\\OneDrive - Telkom University\\Documents\\Tubes\\pesanan_harian.txt", "w")
    filecheckout.write(metode)
    filecheckout.write("\n")
    filecheckout.write(noid)
    filecheckout.write("\n")
    filecheckout.close()
    print("Baiklah pembayaran Anda akan diproses")
    print("Terimakasih sudah membeli :)")
    return mainroom_buyer()

def nopesanan():
    variasibuy()
    p_id=int(input("\nMasukkan nomor pesanan Anda:"))

def placeOrder():
    print("\n")
    nopesan=10
    p_id=int(input("\nMasukkan no Id : "))
    
    for p in listvariasi_p:
        if p["Id"]==p_id:
            print("\nId\tNama\tStok\tHarga")
            print("***************************************************")
            print(f'{p["Id"]}\t{p["Nama               "]}\t{p["Stok "]}\t\t{p["Harga"]}')
            order='{p["Id"]}\t{p["Nama               "]}\t{p["Stok "]}\t\t{p["Harga"]}'
            conform=input("\nApakah kamu ingin memasukkan produk tersebut ke keranjang? : Y/N ")
            
            if conform=='Y' or conform=='y':
                print("\nProduk tersebut berhasil dimasukkan {} {}".format(p["Id"],p["Nama               "]))
                nopesan+=1
                print("Nomor pesanan Anda : ",nopesan)
                p["Stok "]-=1
                break
                
            elif conform=='N' or conform=='n' :
                print("Produk tidak ditambahkan ke keranjang")
                break
            else:
                print("\nKamu salah dalam memasukkan pilihan. Mohon pilih kembali\n")
                conform=input("\nApakah kamu ingin memasukkan produk tersebut ke keranjang? : Y/N")
                break
                
    if p["Id"]!=p_id:
        print("\nKamu memasukkan Id yang salah. Mohon masukkan Id yang valid\n")
        nopesanan()            
    print("\nStok : \n")    
    
    variasibuy()

def cancelOrder():
    print("\n")
    found=False
    temp=[]
    nopesanan=input("Masukkan nomor pesanan : ")
    for p in listvariasi_p:
        found=p["Id"]== nopesanan
        if found!=True:
            temp.append(p)
    if len(temp)==p:
        print(f'{nopesanan} tidak ditemukan')
    else:
        print(f'{nopesanan} sudah dihapus dari pesanan Anda')

def wishlist():
    status = True
    while status == True :
        print("\n")
        print("-"*18,">>UR WISHLIST<<", "-"*18)
        print(" "*10,"Kelola produk yang akan kamu checkout", " "*10)
        print("Menu:\n    1.Tambahkan produk\n    2.Menghapus produk\n    0.CheckOut\n")
                        
        pilihan = input("Masukkan pilihan anda:")
        if pilihan == "1":
            placeOrder()
        elif pilihan =="2":
            cancelOrder()
        elif pilihan =="0":
            checkout()
            print("Terimakasih, selanjutnya Anda akan diarahkan pada proses pembayaran")
        else:
            status = False
            print("Mohon masukkan pilihan dengan benar")
            

#MAINROOM BUYER    
def mainroom_buyer():
    print("\n")
    print("="*25," >>MAIN ROOM<< ", "="*25)
    print("\n")               
    print('''
    1. Makanan
    2. Pulsa 
    3. Tiket
    0. EXIT (Log Out)   
    ''')
    
    mainroombuy=input("Masukkan pilihan mu: ")
    if mainroombuy=="1":
        variasibuy()
    elif mainroombuy=="2":
        pulsa()
    elif mainroombuy=="3":
        tiket()
    elif mainroombuy=="0":
        print("="*25,">>HALO! SELAMAT DATANG\U0001F929<<","="*25)

        pilihanLogIn=input("Kamu adalah?\n\nSELLER(penjual)\nBUYER(pembeli)\n:")
        if pilihanLogIn=="SELLER" or pilihanLogIn=="seller":
            loginutama()
            print("\n")
            print("*"*50)
            mainroom_seller()

        elif pilihanLogIn=="BUYER" or pilihanLogIn=="buyer":
            loginutama()
            print("\n")
            print("*"*50)
            mainroom_buyer()
    else:
        print("\nMohon masukkan pilihan anda dalam bentuk angka\U0001F600")

#RUN SEMUANYA======================================================================

print("="*25,">>HALO! SELAMAT DATANG\U0001F929<<","="*25)

pilihanLogIn=input("Kamu adalah?\n\nSELLER(penjual)\nBUYER(pembeli)\n:")
if pilihanLogIn=="SELLER" or pilihanLogIn=="seller":
    loginutama()
    print("\n")
    print("*"*50)
    mainroom_seller()

elif pilihanLogIn=="BUYER" or pilihanLogIn=="buyer":
    loginutama()
    print("\n")
    print("*"*50)
    mainroom_buyer()

#VISUALISASI=======================================================================
Makaroni_asin_pedas = 20
Makaroni_balado = 10
Makaroni_keju = 8
Makaroni_rendang = 20
Basreng_asin_pedas = 17
Basreng_balado = 8 
Basreng_keju = 5 
Basreng_rendang = 20
Kripik_kaca_asin_pedas = 25
Kripik_kaca_balado = 15
Kripik_kaca_keju = 10
Kripik_kaca_rendang = 8 

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [20, 10, 8, 20, 17, 8, 5, 20, 25, 15, 10, 8]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Stok Produk Makanan')
ax.set_ylabel('Jumlah Stock')
ax.set_xlabel('Nama Produk')

ax.set_xticks(x)
ax.set_xticklabels(("MAP", "MB", "MK", "MR", "BA", "BB", "BK", "BR", "KA", "KB", "KK", "KR"))

plt.show()

#Notes : 
#MAP(MakaroniAsinPedas),MB(MakaroniBalado),MK(MakaroniKeju),MR(MakaroniRendang),
#BAP(BasrengAsin),BB(Basreng Balado),BK(BasrengKeju),BR(BasrengRendang),
#KKAP(KeripikKacaAsinPedas),KKB(KeripikKaca),KKK(KeripikKacaKeju),KKR(KeripikKacaRendang)

#SELESAI===========================================================================