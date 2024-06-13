import subprocess

def check_host(host):
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Host {host} is reachable")
    else:
        print(f"Host {host} is unreachable")

if __name__ == "__main__":
    host_to_check = 'blackrock.com'  # Ganti dengan host yang ingin Anda periksa
    check_host(host_to_check)
