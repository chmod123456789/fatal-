import subprocess

def block_ip(ip_address):
    # Menggunakan subprocess untuk menjalankan perintah shell
    try:
        subprocess.run(['iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'], check=True)
        print(f"IP address {ip_address} berhasil diblokir.")
    except subprocess.CalledProcessError as e:
        print(f"Gagal memblokir IP address {ip_address}. Kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    ip_to_block = "41.255.199.18 - 130.211.38.47"  # Ganti dengan IP address yang ingin diblokir
    block_ip(ip_to_block)
