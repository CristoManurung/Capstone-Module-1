import tabulate

list_RentalMotor = [
   
   
   
    {
        'kode' : 'm1' ,
        'Nama' : 'HD Softiel Classic',
        'Tipe' : 'SPORT',
        'Stock': 2,
        'Harga': 3000000
    },
    {
        'kode' : 'm2' ,
        'Nama': 'HD Street 500 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1300000
    },
    {
        'kode' : 'm3' ,
        'Nama' : 'BMW F800GS',
        'Tipe' : 'SPORT',
        'Stock': 2,
        'Harga': 2000000
    },
    {
        'kode' : 'm4' ,
        'Nama': 'BWM G310',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1200000
    },
    {
        'kode' : 'm5' ,
        'Nama': 'Kawasaki Z900',
        'Tipe' : 'SPORT',
        'Stock': 2,
        'Harga': 2000000
    },
    {
        'kode' : 'm6' ,
        'Nama': 'Kawasaki Z800',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1300000
    },
    {
        'kode' : 'm7' ,
        'Nama': 'Kawasaki Versys 650 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1200000
    },
    {
        'kode' : 'm8' ,
        'Nama': 'Kawasaki ZX25R',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 800000
    },
    {
        'kode' : 'm9' ,
        'Nama': 'Ducati Monster',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1500000
    },
    {
        'kode' : 'm10' ,
        'Nama': 'Ducati Scrambler 400 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1300000
    },
    {
        'kode' : 'm11' ,
        'Nama': 'Honda Rebel 500 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1300000
    },
    {
        'kode' : 'm12' ,
        'Nama': 'KTM 390 Adventure',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 1200000
    },
    {
        'kode' : 'm13' ,
        'Nama': 'Royal Enfield Himalayan 500 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 850000
    },
    {
        'kode' : 'm14' ,
        'Nama': 'Royal Enfield Classic 500 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 800000
    },
    {
        'kode' : 'm15' ,
        'Nama': 'Royal Enfield Classic 350 cc',
        'Tipe' : 'SPORT',
        'Stock': 5,
        'Harga': 800000
    },
    {
        'kode' : 'm16' ,
        'Nama': 'Kawasaki Ninja 250 cc',
        'Tipe' : 'SPORT',
        'Stock': 8,
        'Harga': 400000
    },
    {
        'kode' : 'm17' ,
        'Nama': 'Kawasaki Versys 250 cc',
        'Tipe' : 'SPORT',
        'Stock': 8,
        'Harga': 400000
    },
    {
        'kode' : 'm18' ,
        'Nama': 'Kawasaki W175',
        'Tipe' : 'SPORT',
        'Stock': 8,
        'Harga': 300000
    },
    {
        'kode' : 'm19' ,
        'Nama': 'Vespa',
        'Tipe' : 'Matic',
        'Stock': 10,
        'Harga': 250000
    }
    
    
]






def tampilkanSemuaMotor():
    print(tabulate.tabulate(list_RentalMotor, headers = 'keys',tablefmt= 'fancy_grid')) 

# cek data duplikat
def jikaDataDuplicate(primary_key):
    return any(entry['kode'] == primary_key for entry in list_RentalMotor)

def jikaDataAda(primary_key):
     print(tabulate.tabulate(list_RentalMotor, headers = 'keys',tablefmt= 'fancy_grid'))

def cari_barang_berdasarkan_PKey2(primary_key):
    result = [entry for entry in list_RentalMotor if entry['kode'].lower() == primary_key.lower()]
    return result

def cari_barang_berdasarkan_PKey3(primary_key):
    result = [entry for entry in list_RentalMotor if entry['kode'].lower() == primary_key.lower()]
    return result   

# delelte data
def deleteDataMotor():
    print(" Konfrimasi Final Delete Data")
    p_key2 = str(input("Input ulang kode yang ingin dihapus sekali lagi : "))
    for motor in list_RentalMotor:
        if motor["kode"] == p_key2:
            list_RentalMotor.remove(motor)

# Update data
def editKolomData():
    primary_key = input("Enter Kode (Primary Key) to edit: ")
    hasil_pencarian = cari_barang_berdasarkan_PKey2(primary_key)
    
    if (hasil_pencarian) :

                print(tabulate.tabulate(hasil_pencarian, headers="keys", tablefmt="fancy_grid"))
                kolomdiubah = input("Masukan kolom yang ingin diedit: ")
                if kolomdiubah in hasil_pencarian[0]:
                    new_value = input(f"masukkan value untuk {kolomdiubah} : ")
                    for motor in list_RentalMotor:
                        if motor['kode'] == primary_key:
                            if new_value:  
                                motor[kolomdiubah] = new_value
                    print("Data successfully updated!")
                    tampilkanSemuaMotor()
                
                    menuUpdate2_DataMotor()
                    choice3_1 = int(input("Enter : "))
                    if (choice3_1 == 1):
                        
                        print(" Data Succesfully Updated")
                    elif choice3_1 == 2:
                        print("Data not saved.")
                    else:
                        print("Invalid option.")
    





# LIST MENU
def menu():
    print('''Menu utama:
        1. List Motor
        2. Tambah Data Motor
        3. Edit Data Motor
        4. Delete Data Motor   
        5. Exit
          ''')


def menuListMotor():
    print('''Menu utama:
        1. Tampilkan semua data motor
        2. Cari Data Motor
        3. Kembali ke halaman utama
          ''')
# Cari data motor
def cari_barang_berdasarkan_brand(nama):
    return list(filter(lambda x: 'Nama' in x and nama.lower() in x['Nama'].lower(), list_RentalMotor))

def cari_barang_berdasarkan_PKey(nama):
    return list(filter(lambda x: 'kode' in x and nama.lower() in x['kode'].lower(), list_RentalMotor))

def  menuTambahDataMotor():
    print('''Menu Tambah Data Motor:
          1. Menambah Data Motor
          2. Kembali ke halaman utama
            ''')
    


def menuSavingNewData():
    print(''' 
           1. Save Data?
           2. Exit 
            ''')
    choice = int(input("Enter your option: "))
    return choice




def menuUpdateDataMotor():
    print(''' 
        1. Update Data
        2. Kembali ke halaman utama

            ''')

def menuContinueUpdate():
    print(''' 
        1. Continue Update
        2. Kembali ke halaman Update Data Motor

            ''')

def menuUpdate2_DataMotor():
    print(''' 
        1. saving & Update Data
        2. Kembali ke halaman utama

            ''')
def menuDelete():
    print(''' 
        1. Delete Data
        2. Kembali ke halaman utama

            ''')
    
def menuDelete2():
    print(''' 
          Apakah Anda akan Delete Data Diatas?
        1. Ya, Delete Data Diatas
        2. Tidak, Kembali ke halaman utama
          

            ''')






# Menu UTAMA
menu()
option = int(input("Enter your option :"))

while option != 0:
# Validasi Menu UTAMA
    if option == 1:
        menuListMotor() 
        option1 = int(input("Enter your option :"))
        # Menu List motor
        if (option1 == 1):
            tampilkanSemuaMotor()
        elif (option1 == 2):
            search_namabarang = input("Data Motor yang ingin di cari :")
            hasil_pencarian = cari_barang_berdasarkan_brand(search_namabarang)
            if (hasil_pencarian):
                #    print(hasil_pencarian)
                   print(tabulate.tabulate(hasil_pencarian, headers= "keys", tablefmt="fancy_grid"))
            else :
                print("Data Not Exist!")
            
        elif option1 == 3:
            menu()
            option = int(input("Enter your option :"))
        else:
            print("Menu tidak ditemukan") and menuListMotor()
# Menu CREATE
    elif option == 2:
        menuTambahDataMotor()
        option2 = int(input("Enter your option :"))

        if (option2 == 1):
            
            primary_key = (input("Enter Kode (Primary Key): "))

        # Check exist atau tidak
            if jikaDataDuplicate(primary_key):
                print("There's data with the same primary key. Please enter a unique primary key.")
                continue  

        # Continue to get other data if the primary key is unique
            tambah_Barang = {
            'kode': primary_key,
            'Nama': input("Enter Nama: "),
            'Tipe': input("Enter Tipe: "),
            'Stock': int(input("Enter Stock: ")),
            'Harga': int(input("Enter Harga: "))
            }

        # Append data ke list baru
            list_RentalMotor.append(tambah_Barang)
            print(tabulate.tabulate(list_RentalMotor, headers= "keys", tablefmt="fancy_grid"))


            choice = menuSavingNewData()

    
            if choice == 1:
                print("Data saved successfully!")
            elif choice == 2:
                print("Data not saved.")
            else:
                print("Invalid option.")

        elif (option2) == 2:

            menu()
            option = int(input("Enter your option: "))
        else:
            print("Menu tidak ditemukan") and menuTambahDataMotor()
           
# Menu Update    
    elif option == 3:
        menuUpdateDataMotor()
        option3 = int(input("Enter your option :"))
        
        if (option3 == 1):
            
             editKolomData()
        
        elif (option2) == 2:

            menu()
            option = int(input("Enter your option: "))
        else:
            print("Menu tidak ditemukan") and menuUpdateDataMotor()
            
            











# Menu DELETE    
    elif option == 4:
        menuDelete()
        option4 = int(input("Enter your option :"))
        if (option4 == 1):
            primary_key = (input("Input Barang yang ingin di Delete: "))
            hasil_pencarian = cari_barang_berdasarkan_PKey3(primary_key)
            if (hasil_pencarian) :
                print(tabulate.tabulate(hasil_pencarian, headers= "keys", tablefmt="fancy_grid"))
                menuDelete2()
                choice4 = int(input(' Enter option? '))
                if choice4 == 1:
                    deleteDataMotor()
                    print(tabulate.tabulate(list_RentalMotor, headers= "keys", tablefmt="fancy_grid"))
                    print(' Data Succesfully Deleted')
                           
            
               
        elif (option2) == 2:

            menuDelete()
            option = int(input("Enter your option: "))

        else:
            print("Menu tidak ditemukan") 
                    
# Menu Exit    
    elif option == 5:
        print("Exit")
        break
    else:
        print("Invalid Option")





















