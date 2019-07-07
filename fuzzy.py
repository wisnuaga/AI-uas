def mobil_sedikit(x):
    if x >= 20:
        return "sedikit", 0
    if x == 0:
        return "sedikit", 1
    if 0 < x < 20:
        return "sedikit", (20 - x) / (20 - 0)

def mobil_lumayan(x):
    if 10 >= x or x >= 50:
        return "lumayan", 0
    if x == 30:
        return "lumayan", 1
    if 10 < x < 30:
        return "lumayan", (x - 10) / (30 - 10)
    if 30 < x < 50:
        return "lumayan", (50 - x) / (50 - 30)

def mobil_banyak(x):
    if x <= 40:
        return "banyak", 0
    if x >= 60:
        return "banyak", 1
    if 40 < x < 60:
        return "banyak", (x - 40) / (60 - 40)

def motor_sedikit(x):
    if x >= 40:
        return "sedikit", 0
    if x == 0:
        return "sedikit", 1
    if 0 < x < 40:
        return "sedikit", (40 - x) / (40 - 0)

def motor_lumayan(x):
    if 20 >= x or x >= 100:
        return "lumayan", 0
    if x == 60:
        return "lumayan", 1
    if 20 < x < 60:
        return "lumayan", (x - 20) / (60 - 20)
    if 60 < x < 100:
        return "lumayan", (100 - x) / (100 - 60)

def motor_banyak(x):
    if x <= 80:
        return "banyak", 0
    if x >= 120:
        return "banyak", 1
    if 80 < x < 120:
        return "banyak", (x - 80) / (120 - 80)

def jml_mobil(x):
    return mobil_sedikit(x), mobil_lumayan(x), mobil_banyak(x)

def jml_motor(x):
    return motor_sedikit(x), motor_lumayan(x), motor_banyak(x)

def aturan(mobil, motor):
    if mobil[0] == "sedikit" and motor[0] == "sedikit":
        return "sebentar", (mobil[1] and motor[1])
    if mobil[0] == "lumayan" and motor[0] == "sedikit":
        return "sedang", (mobil[1] and motor[1])
    if mobil[0] == "banyak" and motor[0] == "sedikit":
        return "lama", (mobil[1] and motor[1])

    if mobil[0] == "sedikit" and motor[0] == "lumayan":
        return "sedang", (mobil[1] and motor[1])
    if mobil[0] == "lumayan" and motor[0] == "lumayan":
        return "sedang", (mobil[1] and motor[1])
    if mobil[0] == "banyak" and motor[0] == "lumayan":
        return "lama", (mobil[1] and motor[1])

    if mobil[0] == "sedikit" and motor[0] == "banyak":
        return "lama", (mobil[1] and motor[1])
    if mobil[0] == "lumayan" and motor[0] == "banyak":
        return "lama", (mobil[1] and motor[1])
    if mobil[0] == "banyak" and motor[0] == "banyak":
        return "lama", (mobil[1] and motor[1])

def durasi_lampu(jml_mobil, jml_motor):
    sebentar = ["sebentar", 0]
    sedang = ["sedang", 0]
    lama = ["lama", 0]

    for mobil in jml_mobil:
        for motor in jml_motor:
            temp = aturan(mobil, motor)
            if temp[1] != 0:
                if temp[0] == sebentar[0] and temp[1] > sebentar[1]:
                    sebentar[1] = temp[1]
                if temp[0] == sedang[0] and temp[1] > sedang[1]:
                    sedang[1] = temp[1]
                if temp[0] == lama[0] and temp[1] > lama[1]:
                    lama[1] = temp[1]

    return sebentar, sedang, lama

def defuzzifiasi_madani(lampu_lalu_lintas):
    a, b, c = lampu_lalu_lintas
    sebentar = (5 + 10 + 15 + 20 + 25 + 30 + 35) * a[1]
    sedang = (25 + 30 + 35 + 40 + 45 + 50 + 55
            + 65 + 70 + 75 + 80 + 85 + 90 + 95) * b[1]
    lama = (85 + 90 + 95 + 100 + 105 + 110 + 115) * c[1]
    pembagi = (7 * a[1]) + (14 * b[1]) + (7 * c[1])

    durasi_lampu = (sebentar + sedang + lama) / pembagi

    return round(durasi_lampu)

mobil = 54
motor = 112

get_mobil = jml_mobil(mobil)
get_motor = jml_motor(motor)

lampu_lalu_lintas = durasi_lampu(get_mobil, get_motor)
durasi = defuzzifiasi_madani(lampu_lalu_lintas)
print(durasi)

for mobil in get_mobil:
    for motor in get_motor:
        temp = aturan(mobil, motor)
        print("mobil: " + str(mobil) + " | motor: " + str(motor) + " -> " + str(temp))