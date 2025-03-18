#Tugas 3 No 2 Praktikum PBO
#Hildyah Maretasya Araffad
#123140151

import random

# Dictionary untuk memetakan kombinasi alel ke golongan darah
golongan_darah = {
    ("A", "A"): "A",
    ("A", "O"): "A",
    ("O", "A"): "A",
    ("B", "B"): "B",
    ("B", "O"): "B",
    ("O", "B"): "B",
    ("A", "B"): "AB",
    ("B", "A"): "AB",
    ("O", "O"): "O",
}

# Fungsi untuk menghitung golongan darah anak berdasarkan alel orang tua
def tentukan_golongan_darah(ayah_alleles, ibu_alleles):
    # Memilih satu alel secara acak dari ayah dan ibu
    alel_ayah = random.choice(ayah_alleles)
    alel_ibu = random.choice(ibu_alleles)

    # Mencari golongan darah berdasarkan kombinasi alel
    kombinasi = (alel_ayah, alel_ibu)
    return golongan_darah.get(kombinasi, "Kombinasi tidak valid")

# Fungsi untuk mengonversi golongan darah menjadi daftar alel
def konversi_golongan_darah_ke_alel(golongan_darah_input):
    if golongan_darah_input == "A":
        return ["A", "O"]
    elif golongan_darah_input == "B":
        return ["B", "O"]
    elif golongan_darah_input == "O":
        return ["O", "O"]
    elif golongan_darah_input == "AB":
        return ["A", "B"]
    else:
        return None

# Input dari pengguna
print("Masukkan golongan darah ayah (contoh: A, B, O, AB): ")
golongan_ayah = input().strip().upper()

print("Masukkan golongan darah ibu (contoh: A, B, O, AB): ")
golongan_ibu = input().strip().upper()

# Konversi golongan darah ke daftar alel
ayah_alleles = konversi_golongan_darah_ke_alel(golongan_ayah)
ibu_alleles = konversi_golongan_darah_ke_alel(golongan_ibu)

# Validasi input
if ayah_alleles is None or ibu_alleles is None:
    print("Error: Golongan darah harus berupa A, B, O, atau AB.")
else:
    # Menentukan golongan darah anak
    golongan_darah_anak = tentukan_golongan_darah(ayah_alleles, ibu_alleles)
    print("Golongan darah anak yang mungkin berdasarkan pewarisan adalah:", golongan_darah_anak)
