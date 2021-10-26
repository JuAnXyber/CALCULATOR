print("MASUKKAN nomor PERTAMA")
a=input("")
print("pilih \n>tambah + \n>kurang - \n>kali × \n>bagi /")
x=input("")
print("MASUKKAN nomor KEDUA")
b=input("")

#penjumplahan
if x==('tambah')or('+'): c=float(a) + float(b)

#pengurangan
if x==('kurang')or('-'): c=float(a) - float(b)

#perkalian
if x==('kali')or('×'): c=float(a) * float(b)

#pembagian
if x==('bagi')or('/'): c=float(a) / float(b)

print('RESULT=',(c))
print('CLEAR y/n')
m=input("")
if m==('y'): print('KETIK clear')
if m==('n'): print('oke') 
