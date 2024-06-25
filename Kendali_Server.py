import socket

def is_unwanted_ip(ip_address):
    # Definisikan logika untuk memeriksa IP yang tidak diinginkan
    unwanted_ips = ["8.8.8.8", "9.9.9.9"]
    return ip_address in unwanted_ips

def block_connection(ip_address):
    # Implementasi untuk menangani koneksi dari IP yang tidak diinginkan
    print(f"Blokir koneksi dari IP: {ip_address}")

def main():
    # Contoh menggunakan socket untuk mendengarkan koneksi
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    print("Menunggu koneksi...")

    while True:
        client_socket, addr = server_socket.accept()
        client_ip = addr[0]

        if is_unwanted_ip(client_ip):
            block_connection(client_ip)
            client_socket.close()
        else:
            # Lanjutkan dengan koneksi yang diizinkan
            print(f"Koneksi dari IP yang diizinkan: {client_ip}")
            client_socket.close()

if __name__ == "__main__":
    main()
