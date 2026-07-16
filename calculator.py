def start_calculator():

    while True:
        print("=" * 34)
        print("         CALCULATOR")
        print("=" * 34)
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")
        print("5 - Geri Dön")

        secim = input("\nSeçimin: ")

        if secim == "5":
            break

        try:
            sayi1 = float(input("İlk sayı: "))
            sayi2 = float(input("İkinci sayı: "))

            if secim == "1":
                print(f"\nSonuç: {sayi1 + sayi2}")

            elif secim == "2":
                print(f"\nSonuç: {sayi1 - sayi2}")

            elif secim == "3":
                print(f"\nSonuç: {sayi1 * sayi2}")

            elif secim == "4":
                if sayi2 == 0:
                    print("\n0'a bölünemez!")
                else:
                    print(f"\nSonuç: {sayi1 / sayi2}")

            else:
                print("\nGeçersiz seçim!")

        except ValueError:
            print("\nLütfen sayı gir!")

        input("\nDevam etmek için Enter...")
        print("\n" * 3)