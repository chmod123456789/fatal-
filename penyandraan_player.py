import os
import time
import random

def clear_screen():
    os.system('clear')  # Membersihkan pola slot yg telah ditentukan player di system android

def generate_pattern(rows, columns):
    pattern = []

    # Membuat pola acak dengan karakter '*'
    for _ in range(rows):
        row = []
        for _ in range(columns):
            if random.random() > 0.5:
                row.append('*')
            else:
                row.append(' ')
        pattern.append(''.join(row))

    return pattern

def print_pattern(pattern):
    for row in pattern:
        print(row)

def main():
    clear_screen()
    print("Generating and displaying a random pattern:")
    try:
        while True:
            rows, columns = os.popen('stty size', 'r').read().split()
            rows = int(rows)
            columns = int(columns)

            pattern = generate_pattern(rows, columns)
            print_pattern(pattern)

            time.sleep(1)  # Delay 1 detik sebelum menghasilkan pola baru
            clear_screen()

    except KeyboardInterrupt:
        print("\nPattern generation stopped.")

if __name__ == "__main__":
    main()
