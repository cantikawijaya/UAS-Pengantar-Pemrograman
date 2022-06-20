dataMahasiswa = [
    {
        "Nama": "Putri Ayu Cantika Wijaya",
        "NIM": "421313248",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "Nama": "Irensa Bandaso",
        "NIM": "82131335",
        "Jurusan": "Ilmu Komunikasi"
    },
    {
        "Nama": "I Gede Jaya Kumala",
        "NIM": "121114124",
        "Jurusan": "Akuntansi"
    }

]

print("Pilihlah Nama Mahasiswa di bawah ini : ")
print("1. Putri Ayu Cantika Wijaya")
print("2. Irensa Bandaso")
print("3. I Gede Jaya Kumala")

input = input("\nKetik Angka 1 atau 2 atau 3 :")

if input == '1':
    print("Nama = ", dataMahasiswa[0]['Nama'])
    print("Nim = ", dataMahasiswa[0]['NIM'])
    print("Jurusan = ", dataMahasiswa[0]['Jurusan'])

elif input == '2':
    print("Nama = ", dataMahasiswa[1]['Nama'])
    print("Nim = ", dataMahasiswa[1]['NIM'])
    print("Jurusan = ", dataMahasiswa[1]['Jurusan'])
else:
    print("Nama = ", dataMahasiswa[2]['Nama'])
    print("Nim = ", dataMahasiswa[2]['NIM'])
    print("Jurusan = ", dataMahasiswa[2]['Jurusan'])
