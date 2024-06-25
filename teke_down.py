import subprocess

def block_website(website):
    try:
        # Mengarahkan lalu lintas ke localhost pada port 80 (HTTP) dan 443 (HTTPS) plus 8022 (SSH)
        subprocess.run(['iptables', '-A', 'OUTPUT', '-d', website, '-p', 'tcp', '--dport', '80', '-j', 'REJECT'], check=True)
        subprocess.run(['iptables', '-A', 'OUTPUT', '-d', website, '-p', 'tcp', '--dport', '443', '-j', 'REJECT'], check=True)
        print(f"Berhasil memblokir situs {website}.")
    except subprocess.CalledProcessError as e:
        print(f"Gagal memblokir situs {website}. Kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    website_to_block = "example.com"  # Ganti dengan situs yang ingin kamu blokir
    block_website(website_to_block)
