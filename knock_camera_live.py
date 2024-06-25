import socket

def check_live(host, port):
    try:
        socket.setdefaulttimeout(1)  # Timeout set to 1 second
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except socket.error:
        return False

def main():
    host = input("Masukkan alamat IP atau hostname: ")
    port = int(input("Masukkan port (biasanya 80 untuk web): "))
    
    if check_live(host, port):
        print(f"{host}:{port} is live")
    else:
        print(f"{host}:{port} is not live")

if __name__ == "__main__":
    main()
