# ==========================================
# 303 TOOLKIT
# Module : System Info
# Version: v1.5.3
# Author : Entity303
# ==========================================

import platform
import sys
import psutil
import time


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


def ram_info():

    ram = psutil.virtual_memory()

    total = ram.total / (1024 ** 3)
    used = ram.used / (1024 ** 3)
    free = ram.available / (1024 ** 3)

    print("=" * 35)
    print("         RAM BİLGİSİ")
    print("=" * 35)

    print(f"\n🧠 Toplam RAM : {total:.2f} GB")
    print(f"📈 Kullanılan : {used:.2f} GB")
    print(f"📉 Boş RAM    : {free:.2f} GB")
    print(f"📊 Kullanım   : %{ram.percent}")

    input("\nDevam etmek için Enter'a bas...")


def disk_info():

    disk = psutil.disk_usage("/")

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)

    print("=" * 35)
    print("        DİSK BİLGİSİ")
    print("=" * 35)

    print(f"\n💾 Toplam Disk : {total:.2f} GB")
    print(f"📦 Kullanılan  : {used:.2f} GB")
    print(f"🆓 Boş Alan    : {free:.2f} GB")
    print(f"📊 Kullanım    : %{disk.percent}")

    input("\nDevam etmek için Enter'a bas...")


def python_info():

    print("=" * 35)
    print("        PYTHON")
    print("=" * 35)

    print(f"\n🐍 Python Sürümü : {platform.python_version()}")

    print("\n📂 Python Konumu:")
    print(sys.executable)

    input("\nDevam etmek için Enter'a bas...")


def uptime_info():

    boot = psutil.boot_time()
    now = time.time()

    uptime = int(now - boot)

    days = uptime // 86400
    uptime %= 86400

    hours = uptime // 3600
    uptime %= 3600

    minutes = uptime // 60
    seconds = uptime % 60

    print("=" * 35)
    print("       SİSTEM DURUMU")
    print("=" * 35)

    print("\n🟢 Durum      : Aktif")
    print(
        f"🕒 Açık Kalma : {days} Gün {hours} Saat {minutes} Dakika {seconds} Saniye"
    )

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
        print("5 - Sistem Açık Kalma Süresi")
        print("6 - Geri")

        secim = input("\nSeçimin: ")

        if secim == "1":
            computer_info()

        elif secim == "2":
            ram_info()

        elif secim == "3":
            disk_info()

        elif secim == "4":
            python_info()

        elif secim == "5":
            uptime_info()

        elif secim == "6":
            break

        else:
            print("\n❌ Geçersiz seçim!")
            input("\nDevam etmek için Enter'a bas...")