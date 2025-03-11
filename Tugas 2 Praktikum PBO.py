#Tugas 2 Praktikum PBO
#Hildyah Maretasya Araffad
#123140151

import random

class Robot:
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack
        self.defense = 5  # Nilai pertahanan default setiap robot

    def attack_enemy(self, lawan):
        # Mengurangi HP lawan dengan serangan, dikurangi nilai pertahanan lawan
        lawan.hp -= max(0, self.attack - lawan.defense)
        print(f"{self.nama} menyerang {lawan.nama}!")

    def defend(self):
        # Meningkatkan nilai pertahanan robot
        self.defense += 5
        print(f"{self.nama} bertahan!")

    def surrender(self):
        # Robot menyerah dengan mengatur HP menjadi 0
        self.hp = 0
        print(f"{self.nama} menyerah!")

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = 1  # Ronde permainan dimulai dari 1

    def mulai_permainan(self):
        # Memulai loop permainan hingga salah satu robot kehabisan HP
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            print(f"\n--- Ronde {self.ronde} ---")
            self.tampilkan_status()
            self.pilih_aksi(self.robot1, self.robot2)
            if self.robot2.hp > 0:  # Pastikan robot2 masih hidup sebelum gilirannya
                self.pilih_aksi(self.robot2, self.robot1)
            self.ronde += 1  # Berpindah ke ronde berikutnya
            self.reset_defense()  # Reset nilai pertahanan setiap ronde

        print("\n--- Permainan Berakhir ---")
        # Menampilkan pemenang berdasarkan HP yang tersisa
        if self.robot1.hp > 0:
            print(f"{self.robot1.nama} menang!")
        else:
            print(f"{self.robot2.nama} menang!")

    def tampilkan_status(self):
        # Menampilkan status HP dari kedua robot
        print(f"{self.robot1.nama}: HP = {self.robot1.hp}")
        print(f"{self.robot2.nama}: HP = {self.robot2.hp}")

    def pilih_aksi(self, robot, lawan):
        # Memilih aksi yang akan dilakukan oleh robot
        print(f"\nGiliran {robot.nama}:")
        print("1. Serang")
        print("2. Bertahan")
        print("3. Menyerah")
        pilihan = input("Pilih aksi: ")

        if pilihan == "1":
            robot.attack_enemy(lawan)
        elif pilihan == "2":
            robot.defend()
        elif pilihan == "3":
            robot.surrender()

    def reset_defense(self):
        # Reset nilai pertahanan kedua robot menjadi nilai default
        self.robot1.defense = 5
        self.robot2.defense = 5

# Contoh penggunaan
robot1 = Robot("Aurora", 500, 150)
robot2 = Robot("Athena", 670, 120)
game = Game(robot1, robot2)
game.mulai_permainan()  # Memulai permainan
