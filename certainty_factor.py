
def AND(a, b):
    if a < b :
        return a
    return b

def OR(a, b):
    if a > b:
        return a
    return b

def nilai_cf_fakta(nilai_cf):
    # Jawaban : YA
    if nilai_cf.upper() == "A":
        return 1
    # Jawaban : MUNGKIN YA
    if nilai_cf.upper() == "B":
        return 0.6
    # Jawaban : TIDAK TAHU
    if nilai_cf.upper() == "C":
        return -0.1
    # Jawaban : MUNGKIN TIDAK
    if nilai_cf.upper() == "D":
        return -0.6
    # Jawaban : TIDAK
    if nilai_cf.upper() == "E":
        return -1

def beri_jawaban(tanya):
    print(tanya)
    print("A. YA")
    print("B. MUNGKIN YA")
    print("C. TIDAK TAHU")
    print("D. MUNGKIN TIDAK")
    print("E. TIDAK")

    jawab = input('JAWABAN > ')
    print("==================================================")

    if nilai_cf_fakta(jawab) is None:
        print("Jawabanmu tidak valid!")
        return beri_jawaban(tanya)

    return nilai_cf_fakta(jawab)

def R1():
    cf_aturan = 0.7
    cf_fakta = []
    tanya = []
    tanya.append("APAKAH KEBUTUHAN STORAGE ANDA TIDAK BEGITU BESAR ?")
    tanya.append("APAKAH BUDGET ANDA 2 JUTAAN ?")

    cf_fakta.append(beri_jawaban(tanya[0]))
    cf_fakta.append(beri_jawaban(tanya[1]))

    cf_kesimpulan = AND(cf_fakta[0], cf_fakta[1])

    return cf_kesimpulan * cf_aturan

def R2():
    cf_aturan = 0.6
    cf_fakta = []
    tanya = []
    tanya.append("APAKAH KEBUTUHAN STORAGE ANDA BESAR ?")
    tanya.append("APAKAH BUDGET ANDA 3 JUTAAN ?")

    cf_fakta.append(beri_jawaban(tanya[0]))
    cf_fakta.append(beri_jawaban(tanya[1]))

    cf_kesimpulan = AND(cf_fakta[0], cf_fakta[1])

    return cf_kesimpulan * cf_aturan

def R3():
    cf_aturan = 0.9
    cf_fakta = []
    tanya = []
    tanya.append("APAKAH GARANSI RESMI ?")
    tanya.append("APAKAH MASIH GARANSI ?")
    tanya.append("APAKAH GARANSINYA BELUM LAMA HABIS ?")

    cf_fakta.append(beri_jawaban(tanya[0]))
    cf_fakta.append(beri_jawaban(tanya[1]))

    cf_kesimpulan = AND(cf_fakta[0], cf_fakta[1])

    if cf_fakta[1] == -1:
        cf_fakta.append(beri_jawaban(tanya[2]))

        cf_kesimpulan = AND(cf_fakta[0], (OR(cf_fakta[1], cf_fakta[2])))

    return cf_kesimpulan * cf_aturan

def R4():
    cf_aturan = 0.8
    cf_fakta = []
    tanya = []
    tanya.append("APAKAH JARINGAN SELULER NORMAL ?")
    tanya.append("APAKAH TOMBOL HOME EMPUK ?")
    tanya.append("APAKAH TOMBOL POWER BERFUNGSI ?")
    tanya.append("APAKAH EARPHONE ORI ?")
    tanya.append("APAKAH CHARGER NORMAL ?")
    tanya.append("APAKAH JACK AUDIO LANCAR ?")
    tanya.append("APAKAH SPEAKER NORMAL ?")

    cf_fakta.append(beri_jawaban(tanya[0]))
    cf_fakta.append(beri_jawaban(tanya[1]))
    cf_fakta.append(beri_jawaban(tanya[2]))
    cf_fakta.append(beri_jawaban(tanya[3]))
    cf_fakta.append(beri_jawaban(tanya[4]))
    cf_fakta.append(beri_jawaban(tanya[5]))
    cf_fakta.append(beri_jawaban(tanya[6]))

    cf_kesimpulan = AND(AND(AND(AND(AND(AND(cf_fakta[0], cf_fakta[1]), cf_fakta[2]), cf_fakta[3]), cf_fakta[4]), cf_fakta[5]), cf_fakta[6])

    return cf_kesimpulan * cf_aturan

print(R1())
print(R2())
print(R3())
print(R4())