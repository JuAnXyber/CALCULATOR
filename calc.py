def tambah(a, b):
    tambah = float(a) + float(b)
    return tambah
    
def kurang(a, b):
    kurang = float(a) - float(b)
    return kurang
    
def kali(a, b):
    kali = float(a) * float(b)
    return kali
    
def bagi(a, b):
    bagi = float(a) / float(b)
    return bagi
    
while True:
     print("              UNTUK KELUAR KETIK '5' di PILIH OPSI")
     print("")
     print("")
     print("")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("━━━━━━━━━━━━━SIMPLE CALCULATOR━━━━━━━━━━━━━━")
     print("━━━━━━━━━━━━━━━━━━━━BY━━━━━━━━━━━━━━━━━━━━━━")
     print("━━━━━━━━━━━━━━━━JUAN GAMING━━━━━━━━━━━━━━━━━")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("")
     print("")
     print("")
     
     
     a = input("MASUKKAN nomor PERTAMA:  ")
     b = input("MASUKKAN nomor KEDUA:  ")
     print("PILIH\n >TAMBAH( 1 ) \n >KURANG( 2 ) \n >KALI ( 3 ) \n >BAGI ( 4 ) \n >BATAL ( 5 )")
     c = input("PILIH OPSI (1-5)")
     if a == 'EXIT' : 
            break
     if b == 'EXIT' : 
            break
     if c == '1' :
            print("RESULT IS =", tambah(a, b))
     elif c == '2' :
             print("RESULT IS =", kurang(a, b))
     elif c == '3' :
             print("RESULT IS =", kali(a, b))
     elif c == '4' :
             print("RESULT IS =", bagi(a, b))
     elif c == '5' :
             break
     else:
         print("OPERATION DENIED")
