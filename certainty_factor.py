def nilai_cf_fakta(nilai_cf):
    # Jawaban : YA
    if nilai_cf.upper() is "A":
        return 1
    # Jawaban : MUNGKIN YA
    if nilai_cf.upper() is "B":
        return 0.6
    # Jawaban : TIDAK TAHU
    if nilai_cf.upper() is "C":
        return -0.1
    # Jawaban : MUNGKIN TIDAK
    if nilai_cf.upper() is "D":
        return -0.6
    # Jawaban : TIDAK
    if nilai_cf.upper() is "E":
        return -1

def beri_jawaban():
    print("A. YA")
    print("B. MUNGKIN YA")
    print("C. TIDAK TAHU")
    print("D. MUNGKIN TIDAK")
    print("E. TIDAK")

    jawab = input('JAWABAN > ')
    print("==================================================")
    return nilai_cf_fakta(jawab)

def R1():
    cf_aturan = 0.7
    cf_fakta = []

    print("APAKAH KEBUTUHAN STORAGE ANDA TIDAK BEGITU BESAR ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH BUDGET ANDA 2 JUTAAN ?")
    cf_fakta.append(beri_jawaban())

    cf_kesimpulan = cf_fakta[0] and cf_fakta[1]

    return cf_kesimpulan * cf_aturan

def R2():
    cf_aturan = 0.6
    cf_fakta = []

    print("APAKAH KEBUTUHAN STORAGE ANDA BESAR ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH BUDGET ANDA 3 JUTAAN ?")
    cf_fakta.append(beri_jawaban())

    cf_kesimpulan = cf_fakta[0] and cf_fakta[1]

    return cf_kesimpulan * cf_aturan

def R3():
    cf_aturan = 0.9
    cf_fakta = []

    print("APAKAH GARANSI RESMI ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH MASIH GARANSI ?")
    cf_fakta.append(beri_jawaban())

    cf_kesimpulan = cf_fakta[0] and cf_fakta[1]

    if cf_fakta[1] == -1:
        print("APAKAH GARANSINYA BELUM LAMA HABIS ?")
        cf_fakta.append(beri_jawaban())

        cf_kesimpulan = cf_fakta[0] and (cf_fakta[1] or cf_fakta[2])

    return cf_kesimpulan * cf_aturan

def R4():
    cf_aturan = 0.8
    cf_fakta = []

    print("APAKAH JARINGAN SELULER NORMAL ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH TOMBOL HOME EMPUK ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH TOMBOL POWER BERFUNGSI ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH EARPHONE ORI ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH CHARGER NORMAL ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH JACK AUDIO LANCAR ?")
    cf_fakta.append(beri_jawaban())
    print("APAKAH SPEAKER NORMAL ?")
    cf_fakta.append(beri_jawaban())

    for i in range(len(cf_fakta) -1):
        cf_kesimpulan = cf_fakta[i] and cf_fakta[i+1]

    return cf_kesimpulan * cf_aturan, cf_fakta

print(R4())