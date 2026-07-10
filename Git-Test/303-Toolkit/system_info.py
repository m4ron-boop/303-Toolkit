# ==========================================
# 303 TOOLKIT
# Module : System Info
# Version: v1.5
# Author : Entity303
# ==========================================

import os
import platform
import shutil
import sys


def computer_info():

    print("=" * 35)
    print("     BİLGİSAYAR BİLGİSİ")
    print("=" * 35)

    print(f"\n💻 Bilgisayar Adı : {platform.node()}")
    print(f"🪟 İşletim Sistemi : {platform.system()}")
    print(f"📦 Sürüm : {platform.release()}")
    print(f"⚙️ İşlemci : {platform.processor()}")
    print(f"🏗️ Mimari : {platform.machine()}")

    input("\nDevam etmek için Enter'a bas...")


def start_system_info():

    while True:

        print("=" * 35)
        print("        SYSTEM INFO")
        print("=" * 35)
        print("1 - Bilgisayar Bilgisi")
        print("2 - RAM Bilgisi")
        print("3 - Disk Bilgisi")
        print("4 - Python Sürümü")
        print("5 - Geri")

        secim = input("\nSeçimin: ")

        if secim == "1":
            computer_info()

        elif secim == "2":
            print("\n🚧 Yakında eklenecek...")
            input("\nDevam etmek için Enter'a bas...")

        elif secim == "3":
            print("\n🚧 Yakında eklenecek...")
            input("\nDevam etmek için Enter'a bas...")

        elif secim == "4":

            print("\n" + "=" * 35)
            print("        PYTHON")
            print("=" * 35)

            print(f"\n🐍 Python Sürümü : {platform.python_version()}")
            print(f"📂 Çalıştırılabilir Dosya :")
            print(sys.executable)

            input("\nDevam etmek için Enter'a bas...")

        elif secim == "5":
            break

        else:
            print("\n❌ Geçersiz seçim!")
            input("\nDevam etmek için Enter'a bas...")