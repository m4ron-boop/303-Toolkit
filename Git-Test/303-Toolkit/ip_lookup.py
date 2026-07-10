import requests


def start_ip_lookup():
    print("=" * 35)
    print("        IP LOOKUP")
    print("=" * 35)

    ip = input("IP Adresi: ").strip()

    print("\nSorgulanıyor...\n")

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            print(f"IP         : {data['query']}")
            print(f"Ülke       : {data['country']}")
            print(f"Bölge      : {data['regionName']}")
            print(f"Şehir      : {data['city']}")
            print(f"ISP        : {data['isp']}")
            print(f"Organizasyon: {data['org']}")
            print(f"Saat Dilimi: {data['timezone']}")
            print(f"Koordinat  : {data['lat']}, {data['lon']}")

        else:
            print("❌ IP bulunamadı!")

    except Exception:
        print("❌ İnternet bağlantısı veya API hatası!")