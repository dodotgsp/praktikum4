data=[]

while True:
    nama=input('masukkan nama:')
    nim=input('masukkan nim:')
    tugas= int(input('masukkan nilai tugas:'))
    uts= int(input('masukkan nilai UTS:'))
    uas= int(input('masukkan nilai UAS:'))
    nilaiakhir= (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)

    data.append([nama, nim, tugas, uts, uas, int(nilaiakhir)])
    lagi = input ("Tambah lagi (y/t)?")
    if(lagi =="t"):
      break

print ("==============================|======DATA MAHASISWA======|=======================")
print ("=================================================================================")
print ("| NO  |   Nama  |   NIM   | TUGAS |  UTS  |  UAS  |   NILAI AKHIR  |")
print ("=================================================================================")
i=0
for x in data:
    i+=1
    print("|{no:5d}| {nama:7s} | {nim:7s} | {tugas:7d} | {uts:6d} | {uas:6d} | {nilaiakhir:15.5f} |"
        .format (no=i, nama=x[0], nim=x[1], tugas=x[2], uts=x[3], uas=x[4], nilaiakhir=x[5]))
print ("=================================================================================")