import math

while True:
    try:
        angka = float(input("Masukkan angka: "))

        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif angka == 0:
            raise ValueError("Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            hasil = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {hasil}")
            break

    except ValueError as e:
        if str(e) == "Akar kuadrat dari nol tidak diperbolehkan.":
            print(f"Error: {e}")
        else:
            print("Input tidak valid. Harap masukkan angka yang valid.")
