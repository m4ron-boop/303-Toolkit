import base64

def start_base64():
    while True:
        print("=" * 35)
        print("        BASE64 TOOL")
        print("=" * 35)
        print("1 - Encode")
        print("2 - Decode")
        print("3 - Geri")

        secim = input("\nSeçimin: ")

        if secim == "1":
            metin = input("\nMetin: ")

            encoded = base64.b64encode(metin.encode()).decode()

            print("\nEncoded:")
            print(encoded)

        elif secim == "2":
            metin = input("\nBase64 Metni: ")

            try:
                decoded = base64.b64decode(metin).decode()

                print("\nDecoded:")
                print(decoded)

            except:
                print("\n❌ Geçersiz Base64!")

        elif secim == "3":
            break

        else:
            print("\n❌ Geçersiz seçim!")

        input("\nDevam etmek için Enter...")