i = 0
a_tugas = float(0.3)
a_uts = float(0.35)
a_uas = float(0.35)
nama = []
nim = []
tugas = []
uts = []
uas = []
total = []


while True :
    s_nama = input("Nama\t\t: ")
    nama.append(s_nama)
    s_nim = int(input("NIM\t\t: "))
    nim.append(s_nim)
    i_tugas = int(input("Nilai Tugas\t: "))
    tugas.append(i_tugas)
    i_uts = int(input("Nilai UTS\t: "))
    uts.append(i_uts)
    i_uas = int(input("Nilai UAS\t: "))
    uas.append(i_uas)

    rata = (a_tugas*i_tugas) + (a_uts*i_uts) + (a_uas*i_uas)
    total.append(rata)

    ulang = ""
    while ulang!="y" and ulang!="t" :
        ulang = input("Tambah data [y/t] ? :")
    i=i+1
    if ulang == "t" :
        break

print("==========================\tDaftar Mahasiswa\t================================")
print("==============================================================================")
print("  No  |   Nama   |   NIM   |   Tugas   |    UTS   |   UAS   |   Akhir   | ")
print("==========================================================================")
n:int
for n in range(i):
    print("" ,n+1, "|\t" ,nama[n],"  |   ",nim[n],"  |   ",tugas[n],"   |   ",uts[n],"  |   ",uas[n]," |   ",total[n],"  |")
print("==========================================================================")
