import requests

def disconnect_server(url):
    try:
        # Mengirimkan permintaan GET ke server
        response = requests.get(url, timeout=5)
        
        # Menampilkan respons dari server
        print("Response from server:")
        print(response.text)
        
        # Memutus koneksi dengan mengirimkan permintaan POST palsu (opsional)
        # Anda dapat menyesuaikan ini dengan kebutuhan Anda
        fake_post_data = {"fake": "data"}
        fake_response = requests.post(url, data=fake_post_data, timeout=5)
        print("Fake response sent:")
        print(fake_response.text)
        
        print("Disconnected successfully.")
    except requests.exceptions.RequestException as e:
        print("Failed to disconnect:")
        print(e)

# Contoh penggunaan:
if __name__ == "__main__":
    server_url = "http://example.com"  # Ganti dengan URL server yang ingin Anda coba putuskan aksesnya
    disconnect_server(server_url)
