#Latihan Prakitum PBO
#Hildyah Maretasya Araffad
#123140151

# Kelas induk kendaraan
class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        # Inisialisasi properti jenis dan kecepatan maksimum
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        # Menampilkan informasi kendaraan
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")

    def bergerak(self):
        # Menampilkan pesan 
        print(f"Kendaraan {self.jenis} sedang bergerak.")

#Kelas turunan mobil
class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        #Memanggil konstruktor kelas induk dan menganlisis properti tambhan
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        #Menampilkan informasi mobil dengan memanggil method dari kelas induk
        self.info_kendaraan()  #Memanggil method dari kelas induk
        print(f"Merek Mobil: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

    def bunyikan_klakson(self):
        # Menampilkan suara klakson mobil
        print("BEEP BEEP!")

# Kelas turunan Mobil Sport
class MobilSport(Mobil):
    # Memanggil konstruktor kelas mobil dan menganalisis properti private
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda  # Private property
        self.__harga = harga  #Private Property

    # Getter untuk mengambil nilai tenaga kuda
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
 # Setter untuk mengatur nilai tenaga kuda
    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value

    # Getter untuk mengambil nilai harga
    def get_harga(self):
        return self.__harga
    # Getter untuk mengambil nilai harga
    def set_harga(self, value):
        self.__harga = value

    def info_mobil_sport(self):
        #Menampilkan informasi mobil sport dengan memanggil method dari kelas mbil
        self.info_mobil()  
        print(f"Tenaga Kuda: {self.__tenaga_kuda}")
        print(f"Harga: {self.__harga} juta rupiah")

    def mode_balap(self):
        #Menampilkan pesan 
        print("Mobil sport masuk ke mode balap!")

# Contoh Penggunaan
if __name__ == "__main__":
    #Membuat objek dari kelas mobil sport
    mobil_sport = MobilSport("Darat", 300, "Ferrari", 2, 800, 5000)

   #Menampilkan informasi mobil sport
    mobil_sport.info_mobil_sport()
    
   #Menggunakan metode lain
    mobil_sport.bergerak()
    mobil_sport.bunyikan_klakson()
    mobil_sport.mode_balap()

    # Menggunakan getter dan setter
    print(f"Tenaga Kuda Sebelum: {mobil_sport.get_tenaga_kuda()}")
    mobil_sport.set_tenaga_kuda(850)
    print(f"Tenaga Kuda Setelah: {mobil_sport.get_tenaga_kuda()}")

    print(f"Harga Sebelum: {mobil_sport.get_harga()} juta") # Menampilkan harga sebelum dirubah
    mobil_sport.set_harga(5500) # Mengubah harga
    print(f"Harga Setelah: {mobil_sport.get_harga()} juta") #Menampilkan harga setelah dirubah


