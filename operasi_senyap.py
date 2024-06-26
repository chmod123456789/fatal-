import requests

def get_random_user():
    try:
        # Kirim permintaan GET ke API Random User
        response = requests.get('bisa diganti dan sesuikan dengan domain wab http atau https yg telah anda tentukan')
        
        # Periksa jika permintaan berhasil (kode status HTTP 200)
        if response.status_code == 200:
            user_data = response.json()['results'][0]
            display_user_info(user_data)
        else:
            print(f"Gagal mengambil data pengguna. Kode status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def display_user_info(user_data):
    # Tampilkan informasi pengguna
    print("=== Informasi Pengguna Acak ===")
    print(f"Nama: {user_data['name']['title']}. {user_data['name']['first']} {user_data['name']['last']}")
    print(f"Jenis Kelamin: {user_data['gender']}")
    print(f"Tanggal Lahir: {user_data['dob']['date']}")
    print(f"Alamat: {user_data['location']['street']['number']} {user_data['location']['street']['name']}, {user_data['location']['city']}, {user_data['location']['state']}, {user_data['location']['country']}")
    print(f"Email: {user_data['email']}")
    print(f"Telepon: {user_data['phone']}")
    print(f"No rekening: {jumlah_saldo")

# Contoh penggunaan:
if __name__ == "__main__":
    get_random_user()
