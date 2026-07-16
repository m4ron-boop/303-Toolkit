# ==========================================
# 303 TOOLKIT
# Module : Network Tools
# Version: v1.6.3
# Author : Entity303
# ==========================================

import requests
import socket
import subprocess
import ip_lookup
import nmap_tools


def public_ip():

    print("=" * 35)
    print("         PUBLIC IP")
    print("=" * 35)

    try:

        ip = requests.get("https://api.ipify.org", timeout=5).text

        print(f"\n🌐 Public IP : {ip}")

    except:

        print("\n❌ Public IP alınamadı!")

    input("\nDevam etmek için Enter'a bas...")


def local_ip():

    print("=" * 35)
    print("         LOCAL IP")
    print("=" * 35)

    try:

        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        print(f"\n💻 Bilgisayar Adı : {hostname}")
        print(f"🏠 Local IP       : {ip}")

    except:

        print("\n❌ Local IP alınamadı!")

    input("\nDevam etmek için Enter'a bas...")


def dns_lookup():

    print("=" * 35)
    print("        DNS LOOKUP")
    print("=" * 35)

    domain = input("\n🌍 Domain: ")

    try:

        ip = socket.gethostbyname(domain)
        print(f"\n✅ IP Adresi : {ip}")

    except:

        print("\n❌ Domain bulunamadı!")

    input("\nDevam etmek için Enter'a bas...")

def ping():

    print("=" * 35)
    print("            PING")
    print("=" * 35)

    host = input("\n🌐 IP veya Domain: ")

    try:

        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )

        print("\n" + result.stdout)

    except Exception as e:

        print("\n❌ Hata oluştu!")
        print(e)

    input("\nDevam etmek için Enter'a bas...")

def port_check():

    print("=" * 35)
    print("        PORT CHECK")
    print("=" * 35)

    host = input("\n🌐 IP veya Domain: ")

    try:
        port = int(input("🚪 Port: "))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((host, port))

        print()

        if result == 0:
            print("✅ Port AÇIK")
        else:
            print("❌ Port KAPALI")

        sock.close()

    except ValueError:
        print("\n❌ Port sayı olmalıdır!")

    except Exception as e:
        print("\n❌ Hata oluştu!")
        print(e)

    input("\nDevam etmek için Enter'a bas...")


def start_network():

    while True:

        print("=" * 35)
        print("       NETWORK TOOLS")
        print("=" * 35)
        print("1 - 🌐 Public IP")
        print("2 - 🏠 Local IP")
        print("3 - 🔍 IP Lookup")
        print("4 - 🌍 DNS Lookup")
        print("5 - 📡 Ping")
        print("6 - 🚪 Port Check")
        print("7 - 🕵️ Nmap Tools")
        print("8 - 🔙 Geri")

        secim = input("\nSeçimin: ")

        if secim == "1":
            public_ip()

        elif secim == "2":
            local_ip()

        elif secim == "3":
            ip_lookup.start_lookup()

        elif secim == "4":
            dns_lookup()

        elif secim == "5":
            ping()

        elif secim == "6":
            port_check()

        elif secim == "7":
            nmap_tools.nmap_menu()

        elif secim == "8":
            break

        else:
            print("\n❌ Geçersiz seçim!")
            input("\nDevam etmek için Enter'a bas...")