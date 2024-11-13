# -*- coding: utf-8 -*-
"""
Progammer: Raihan Ata Putra
Jurusan Teknik Elektro
Politeknik Negeri Semarang
Dibuat pada Wed Nov 13 09:44:53 2024

"""
def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    
    while guess < guess_limit:
        user = int(input("masukkan angka > "))
        if user == secret_number:
            print("selamat, anda berhasil menemukan ")
            break
        else:
            print("salah")
            guess += 1
    else:
        print(f"gagal, angkanya adalah {secret_number}")