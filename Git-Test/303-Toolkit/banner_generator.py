import pyfiglet
import random
import pyperclip

fonts = [
    "standard",
    "slant",
    "doom",
    "big",
    "digital",
    "bubble",
    "isometric1"
]


def start_banner():
    while True:
        print("=" * 35)
        print("      ASCII BANNER")
        print("=" * 35)
        print("1 - Standard")
        print("2 - Slant")
        print("3 - Doom")
        print("4 - Big")
        print("5 - Digital")
        print("6 - Bubble")
        print("7 - Isometric")
        print("8 - Random Font")
        print("9 - Geri")

        secim = input("\nSeçimin: ")

        if secim == "9":
            break

        text = input("\nYazı: ")

        if secim == "1":
            font = "standard"

        elif secim == "2":
            font = "slant"

        elif secim == "3":
            font = "doom"

        elif secim == "4":
            font = "big"

        elif secim == "5":
            font = "digital"

        elif secim == "6":
            font = "bubble"

        elif secim == "7":
            font = "isometric1"

        elif secim == "8":
            font = random.choice(fonts)

        else:
            print("\n❌ Geçersiz seçim!")
            continue

        banner = pyfiglet.figlet_format(text, font=font)

        while True:
            print("=" * 35)
            print("1 - Ekranda Göster")
            print("2 - TXT Olarak Kaydet")
            print("3 - Panoya Kopyala")
            print("4 - Yeni Banner")
            print("5 - Geri")

            secim2 = input("\nSeçimin: ")

            if secim2 == "1":
                print("\n")
                print(banner)

            elif secim2 == "2":
                dosya = input("\nDosya adı: ")

                with open(dosya + ".txt", "w", encoding="utf-8") as f:
                    f.write(banner)

                print(f"\n✅ {dosya}.txt oluşturuldu!")

            elif secim2 == "3":
                pyperclip.copy(banner)
                print("\n✅ Banner panoya kopyalandı!")

            elif secim2 == "4":
                break

            elif secim2 == "5":
                return

            else:
                print("❌ Geçersiz seçim!")