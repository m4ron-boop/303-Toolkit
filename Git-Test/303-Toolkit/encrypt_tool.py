from cryptography.fernet import Fernet

# Program açıldığında tek bir anahtar oluşturulur
key = Fernet.generate_key()
cipher = Fernet(key)


def start_encrypt():
    while True:
        print("=" * 35)
        print("      ENCRYPT TOOL")
        print("=" * 35)
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Anahtarı Göster")
        print("4 - Geri")

        secim = input("\nSeçimin: ")

        if secim == "1":
            text = input("\nŞifrelenecek metin: ")

            encrypted = cipher.encrypt(text.encode())

            print("\nŞifrelenmiş Metin:\n")
            print(encrypted.decode())

        elif secim == "2":
            text = input("\nŞifreli metin: ")

            try:
                decrypted = cipher.decrypt(text.encode()).decode()

                print("\nÇözülen Metin:\n")
                print(decrypted)

            except:
                print("\n❌ Anahtar yanlış veya metin bozuk!")

        elif secim == "3":
            print("\nAnahtar:")
            print(key.decode())

        elif secim == "4":
            break

        else:
            print("\nGeçersiz seçim!")

        input("\nDevam etmek için Enter...")