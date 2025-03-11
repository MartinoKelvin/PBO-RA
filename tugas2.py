class Robot:
    def __init__(self, name, attack, Hp , armor):
        self.name = name
        self.attack = attack
        self.hp = Hp
        self.armor = armor

    def attack_enemy(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.hasil_attack(self, self.attack)

    def hasil_attack(self, Robot, attack_power_enemy):
        attack_diterima = attack_power_enemy/self.armor
        print("Damage attack nya : " + str(attack_diterima))
        self.hp -= attack_diterima
        print("darah " + self.name + " tersisa " + str(self.hp))

    def regen_health(self):
        self.hp += 5
        print("\n")
        print("HP " + self.name + " bertambah 5")
        print("Hp " + self.name + " sekarang adalah " + str(self.hp)) 


lance = Robot("Lance" , 80, 100, 5)
gusion = Robot("gusion", 70, 100, 15)


while True:
    print("\n=== PILIH ROBOT ===")
    print("1. Gusion")
    print("2. Lance")
    
    pilih_robot = input("Pilih robot yang akan melakukan aksi (1/2): ")

    if pilih_robot == "1":
        pemain = gusion
        lawan = lance
    elif pilih_robot == "2":
        pemain = lance
        lawan = gusion
    else:
        print("Pilihan tidak valid! Coba lagi.")
        continue 

    print("\n=== PILIH AKSI UNTUK Permainan ===")
    print("1. Attack")
    print("2. Regen")
    print("3. Give Up")

    pilihan = input(f"{pemain.name}, pilih aksi (1/2/3): ")

    if pilihan == "1":
        pemain.attack_enemy(lawan)
    elif pilihan == "2":
        pemain.regen_health()
    elif pilihan == "3":
        print(f"{pemain.name} menyerah! Permainan selesai.")
        break
    else:
        print("Pilihan tidak valid!")

    # Cek apakah ada yang kalah
    if gusion.hp <= 0 or lance.hp <= 0:
        print("Permainan berakhir!")
        break

