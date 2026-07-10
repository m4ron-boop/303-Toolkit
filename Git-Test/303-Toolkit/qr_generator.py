import qrcode

def start_qr():
    print("=" * 35)
    print("        QR GENERATOR")
    print("=" * 35)

    veri = input("\nQR içine yazılacak metin: ")
    dosya = input("Dosya adı (uzantı yazma): ")

    qr = qrcode.make(veri)
    qr.save(f"{dosya}.png")

    print(f"\n✅ {dosya}.png oluşturuldu!")