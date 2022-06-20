from prettytable import PrettyTable
import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="programming"
)

active = True

while active:
    programming = koneksi.cursor()

    programming.execute('select*from mahasiswa')

    data = programming.fetchall()
    t = PrettyTable(['id', 'nama', 'nim'])

    for row in data:
        t.add_row(row)
    print(t)

    print("Pilih Aksi : ")
    print("1. Tambah Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Exit")
    inputuser = input("\nKetikkan Pilihan : ")

    if inputuser == '1':
        nama = input("Ketikkan Nama : ")
        nim = input("Ketikkan NIM  : ")

        if len(nama) == 0 and len(nim) == 0:
            print("Data Kosong")
        else:
            koneksiTest = koneksi.cursor()

            koneksiTest.execute(
                "insert into mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))

            koneksi.commit()

            print("Data Telah Ditambahkan")
        cek = input("Ingin melanjutkan program? (Yes/No) :")
        if cek == 'No':
            active = False
    if inputuser == '2':
        idbaru = input("Ketikkan Id yang ingin diperbarui : ")
        print("Pilih tabel yang ingin diperbarui : ")
        print("1. Nama")
        print("2. NIM")
        print("3. Ubah Semua")
        aksibaru = input("Pilih 1-3 : ")
        if aksibaru == '1':
            namabaru = input("Ketikkan Nama Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"baru mahasiswa set nama = '{namabaru}' where id = '{idbaru}'")
            koneksi.commit()
            print("Data Nama Berhasil Diperbarui")
        elif aksibaru == '2':
            nimbaru = input("Ketikkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"baru mahasiswa set nim = '{nimbaru}' where id = '{idbaru}'")
            koneksi.commit()
            print("Data NIM Berhasil Diperbarui")
        elif aksibaru == '3':
            namabaru = input("Ketikkan Nama Baru : ")
            nimbaru = input("Ketikkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"baru mahasiswa set nama = '{namabaru}', nim = '{nimbaru}' where id = '{idbaru}'")
            koneksi.commit()
            print("Data Berhasil Diperbarui")
        else:
            print("Ketikkan 1-3")

        cek = input("Ingin melanjutkan program? (Yes/No) : ")
        if cek == 'No':
            active = False
    if inputuser == '3':
        iddelete = input("Ketikkan ID yang ingin dihapus : ")
        koneksiTest = koneksi.cursor()
        koneksiTest.execute(
            f"delete from mahasiswa where id='{iddelete}'")
        koneksi.commit()
        print("Data Telah Dihapus")
        cek = input("Ingin melanjutkan program? (Yes/No) : ")
        if cek == 'No':
            active = False
    if inputuser == '4':
        active = False
