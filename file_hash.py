import hashlib
import os


def calculate_hash(file_path, algorithm):
    hash_obj = hashlib.new(algorithm)

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


def start_file_hash():
    print("=" * 35)
    print("        FILE HASH")
    print("=" * 35)

    file_path = input("Dosya yolu: ").strip()

    if not os.path.exists(file_path):
        print("\n❌ Dosya bulunamadı!")
        return

    print("\nHesaplanıyor...\n")

    print("MD5:")
    print(calculate_hash(file_path, "md5"))

    print("\nSHA1:")
    print(calculate_hash(file_path, "sha1"))

    print("\nSHA256:")
    print(calculate_hash(file_path, "sha256"))