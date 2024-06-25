import subprocess
import os

def find_pid(package_name):
    # Mencari PID aplikasi berdasarkan nama paket
    try:
        result = subprocess.run(['pgrep', '-f', package_name], capture_output=True, text=True)
        pid = int(result.stdout.strip())
        return pid
    except subprocess.CalledProcessError:
        print(f"Tidak dapat menemukan PID untuk {package_name}")
        return None

def kill_application(package_name):
    # Menghentikan aplikasi berdasarkan nama paket
    pid = find_pid(package_name)
    if pid:
        try:
            os.kill(pid, 15)  # Mengirim sinyal SIGTERM untuk menutup aplikasi
            print(f"Aplikasi dengan nama paket {package_name} telah dihentikan.")
        except OSError:
            print(f"Gagal menghentikan aplikasi dengan nama paket {package_name}.")
    else:
        print(f"Tidak dapat menemukan aplikasi dengan nama paket {package_name}.")

# Contoh penggunaan:
if __name__ == "__main__":
    app_package_name = "www.topbos.com"  # Ganti dengan nama paket aplikasi yang ingin Anda hentikan
    kill_application(app_package_name)
