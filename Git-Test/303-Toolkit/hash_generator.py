import hashlib

def start_hash():
    while True:
        print("=" * 35)
        print("        HASH GENERATOR")
        print("=" * 35)
        print("1 - MD5")
        print("2 - SHA1")
        print("3 - SHA256")
        print("4 - Geri")

        secim = input("\nSeçimin: ")

        if secim == "4":
            break

        metin = input("\nHashlenecek metin: ")

        if secim == "1":
            sonuc = hashlib.md5(metin.encode()).hexdigest()
            print("\nMD5:")
            print(sonuc)

        elif secim == "2":
            sonuc = hashlib.sha1(metin.encode()).hexdigest()
            print("\nSHA1:")
            print(sonuc)

        elif secim == "3":
            sonuc = hashlib.sha256(metin.encode()).hexdigest()
            print("\nSHA256:")
            print(sonuc)

        else:
            print("Geçersiz seçim!")

        input("\nDevam etmek için Enter...")