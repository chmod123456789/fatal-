import random
import time

# Simbol-simbol yang ada dalam slot
symbols = ['Olympus', 'Princes', 'Bonanza', 'Mahjong', 'Wild West', 'Sugar']

# Tabel pembayaran berdasarkan kombinasi simbol
pay_table = {
    ('1', '1', '1'): 10,
    ('2', '2', '2'): 20,
    ('3', '3', '3'): 30,
    ('4', '4', '4'): 40,
    ('5', '5', '5'): 50,
    ('6', '6', '6'): 100
}

def spin_slot():
    # Putar slot
    return random.choices(symbols, k=3)

def calculate_payout(result):
    # Hitung pembayaran berdasarkan hasil spin
    if tuple(result) in pay_table:
        return pay_table[tuple(result)]
    else:
        return 0

def main():
    print("Welcome to Online Slot Gacor!")

    while True:
        input("Press Enter to spin the slot...")
        
        # Spin slot
        result = spin_slot()
        
        # Tampilkan hasil spin
        print(f"Spinning... {result}")
        time.sleep(2)  # Tunggu sebentar sebelum menampilkan hasil
        
        # Hitung dan tampilkan pembayaran
        payout = calculate_payout(result)
        if payout > 0:
            print(f"Congratulations! You won {payout} coins!")
        else:
            print("Try again! No win this time.")

        # Tanya pengguna apakah ingin bermain lagi
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("thank you, don't forget to deposit again")

if __name__ == "__main__":
    main()
