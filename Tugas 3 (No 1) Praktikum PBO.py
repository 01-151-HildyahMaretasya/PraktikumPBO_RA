#Tugas 3 No 1 Praktikum PBO
#Hildyah Maretasya Araffad
#123140151

import math

# Fungsi untuk menampilkan menu operasi
def tampilkan_menu():
    print("\nPilih operasi matematika:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Eksponen")
    print("6. Logaritma (natural)")
    print("7. Keluar")

# Fungsi utama program
def kalkulator():
    while True:  # Loop utama program untuk menjalankan kalkulator
        tampilkan_menu()  # Menampilkan menu operasi
        pilihan = input("Masukkan pilihan (1-7): ")  # Meminta input dari pengguna
        
        # Periksa apakah pengguna ingin keluar
        if pilihan == "7":
            print("Terima kasih telah menggunakan kalkulator! Sampai jumpa.")
            break  # Menghentikan loop dan keluar dari program
        
        # Meminta input angka dari pengguna
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            if pilihan != "6":  # Hanya meminta angka kedua jika bukan logaritma
                angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Harap masukkan angka yang valid!")
            continue  # Kembali ke awal loop
        
        # Melakukan operasi berdasarkan pilihan pengguna
        if pilihan == "1":  # Penjumlahan
            hasil = angka1 + angka2
            print(f"Hasil penjumlahan: {hasil}")
        elif pilihan == "2":  # Pengurangan
            hasil = angka1 - angka2
            print(f"Hasil pengurangan: {hasil}")
        elif pilihan == "3":  # Perkalian
            hasil = angka1 * angka2
            print(f"Hasil perkalian: {hasil}")
        elif pilihan == "4":  # Pembagian
            if angka2 != 0:  # Cek pembagian dengan nol
                hasil = angka1 / angka2
                print(f"Hasil pembagian: {hasil}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan!")
        elif pilihan == "5":  # Eksponen
            hasil = angka1 ** angka2
            print(f"Hasil eksponen: {hasil}")
        elif pilihan == "6":  # Logaritma
            if angka1 > 0:  # Logaritma hanya untuk angka positif
                hasil = math.log(angka1)
                print(f"Hasil logaritma natural: {hasil}")
            else:
                print("Error: Tidak dapat menghitung logaritma dari angka non-positif!")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memulai program
print("Selamat datang di program Kalkulator Sederhana!")
kalkulator()
