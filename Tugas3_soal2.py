import random

class Ayah:
    def __init__(self, alel1, alel2):
        self.golongan_darah = [alel1, alel2]

class Ibu:
    def __init__(self, alel1, alel2):
        self.golongan_darah = [alel1, alel2]

class Anak:
    def __init__(self, ayah, ibu):
        self.alel_diturunkan1 = random.choice(ayah.golongan_darah)
        self.alel_diturunkan2 = random.choice(ibu.golongan_darah)

    def tentukan_golongan_darah(self):
        alel = {self.alel_diturunkan1, self.alel_diturunkan2}
        if 'A' in alel and 'B' in alel:
            return "AB"
        elif 'A' in alel:
            return "A"
        elif 'B' in alel:
            return "B"
        else:
            return "O"

if __name__ == "__main__":
    a1, a2 = input("Masukkan alel ayah (contoh: A O): ").split()
    i1, i2 = input("Masukkan alel ibu (contoh: B O): ").split()
    
    ayah = Ayah(a1, a2)
    ibu = Ibu(i1, i2)
    anak = Anak(ayah, ibu)
    
    print("Golongan darah anak:", anak.tentukan_golongan_darah())
