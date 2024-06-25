import time

def mesin_waktu(tahun):
    print("Memulai mesin waktu...")
    time.sleep(2)
    print(f"Anda berada di tahun {tahun}!")
    if tahun < 2024:
        print("Wow, Anda telah melakukan perjalanan ke masa lalu!")
    elif tahun == 2024:
        print("Anda sedang berada di tahun sekarang!")
    else:
        print("Selamat datang saat ini anda berada di tahun BlackRock!")

if __name__ == "__main__":
    tahun_tujuan = int(input("Masukkan tahun yang ingin Anda kunjungi: "))
    mesin_waktu(tahun_tujuan)
