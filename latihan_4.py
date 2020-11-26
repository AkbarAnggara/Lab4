print("Nama\t: Bangkit Akbar Anggara ")
print("NIM\t: 312010148")
print("Kelas\t: TI.20.B.1")
print('\n')

list1 = [1,2,3,4,5]
print('\nAkses List:')
print(list1[2])
print(list1[1:4])
print(list1[4])
print(list1[3])
print()

print('\nUbah Elemen List:')
list1[3] = 10
print(list1[3])
print()

list1[3:5] = [7,8]
print(list1)
print()

print('\nTambah Elemen List:')
list2 = list1[3:5]
print(list2)
print()

list2.append("angka")
print(list2)
print()

list2.append([10, 11, "puluhan"])
print(list2)
print()

list3 = list1 + list2
print(list3)
