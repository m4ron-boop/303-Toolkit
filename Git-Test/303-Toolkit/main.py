import time

import matrix
import password
import calculator
import qr_generator
import hash_generator
import base64_tool
import encrypt_tool
import file_hash
import ip_lookup
import banner_generator
import file_organizer
import system_info
import network_tools


print("=" * 42)
print("🚀 303 TOOLKIT v1.6 🚀")
print("Developed by Entity303")
print("=" * 42)

print("\nLoading...\n")
time.sleep(1)


while True:

    print("=" * 35)
    print("        303 TOOLKIT")
    print("=" * 35)
    print("1 - Matrix")
    print("2 - Password Generator")
    print("3 - Calculator")
    print("4 - QR Generator")
    print("5 - Hash Generator")
    print("6 - Base64 Tool")
    print("7 - Encrypt Tool")
    print("8 - File Hash")
    print("9 - IP Lookup")
    print("10 - ASCII Banner")
    print("11 - File Organizer")
    print("12 - System Info")
    print("13 - Network Tools")
    print("14 - Exit")

    secim = input("\nSeçimin: ")

    if secim == "1":
        matrix.start_matrix()

    elif secim == "2":
        try:
            length = int(input("Şifre uzunluğu: "))
            print("\nOluşturulan Şifre:")
            print(password.generate_password(length))
        except ValueError:
            print("❌ Lütfen geçerli bir sayı gir!")

    elif secim == "3":
        calculator.start_calculator()

    elif secim == "4":
        qr_generator.start_qr()

    elif secim == "5":
        hash_generator.start_hash()

    elif secim == "6":
        base64_tool.start_base64()

    elif secim == "7":
        encrypt_tool.start_encrypt()

    elif secim == "8":
        file_hash.start_file_hash()

    elif secim == "9":
        ip_lookup.start_lookup()

    elif secim == "10":
        banner_generator.start_banner()

    elif secim == "11":
        file_organizer.start_organizer()

    elif secim == "12":
        system_info.start_system_info()

    elif secim == "13":
        network_tools.start_network()

    elif secim == "14":
        print("Görüşürüz 😎")
        break

    else:
        print("❌ Geçersiz seçim!")

    input("\nDevam etmek için Enter'a bas...")
    print("\n" * 3)