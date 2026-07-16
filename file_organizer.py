# ==========================================
# 303 TOOLKIT
# Module : File Organizer
# Version: v1.4.3
# Author : Entity303
# ==========================================

import os
import shutil


def organize_folder(folder):

    if not os.path.exists(folder):
        print("\n❌ Böyle bir klasör bulunamadı!")
        input("\nDevam etmek için Enter'a bas...")
        return

    extensions = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".gif": "Images",

        ".mp4": "Videos",
        ".mkv": "Videos",
        ".avi": "Videos",

        ".mp3": "Music",
        ".wav": "Music",

        ".pdf": "PDF",
        ".docx": "Documents",
        ".txt": "Documents",

        ".zip": "Archives",
        ".rar": "Archives",
        ".7z": "Archives",

        ".py": "Python",
        ".exe": "Programs"
    }

    summary = {
        "Images": 0,
        "Videos": 0,
        "Music": 0,
        "PDF": 0,
        "Documents": 0,
        "Archives": 0,
        "Python": 0,
        "Programs": 0
    }

    print(f"\n📂 Seçilen klasör:\n{folder}")

    cevap = input(
        "\n⚠️ Bu işlem dosyaları taşıyacaktır.\nDevam etmek istiyor musun? (E/H): "
    ).lower()

    if cevap != "e":
        print("\n❌ İşlem iptal edildi.")
        input("\nDevam etmek için Enter'a bas...")
        return

    print("\nDosyalar düzenleniyor...\n")
     
    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1].lower()

            if ext in extensions:

                category = extensions[ext]

                target = os.path.join(folder, category)

                os.makedirs(target, exist_ok=True)

                try:

                    shutil.move(file_path, os.path.join(target, file))

                    summary[category] += 1

                    print(f"✅ {file} -> {category}")

                except Exception as e:

                    print(f"❌ {file} taşınamadı! ({e})")

    print("\n🎉 İşlem tamamlandı!")

    total = sum(summary.values())

    print("\n" + "=" * 35)
    print("            ÖZET")
    print("=" * 35)

    icons = {
        "Images": "🖼️",
        "Videos": "🎬",
        "Music": "🎵",
        "PDF": "📕",
        "Documents": "📄",
        "Archives": "📦",
        "Python": "🐍",
        "Programs": "⚙️"
    }

    for category, count in summary.items():

        if count > 0:

            print(f"{icons[category]} {category:<10}: {count}")

    print("-" * 35)
    print(f"📊 Toplam düzenlenen dosya: {total}")

    input("\nDevam etmek için Enter'a bas...")


def start_organizer():

    while True:

        print("=" * 35)
        print("      FILE ORGANIZER")
        print("=" * 35)
        print("1 - 📥 Downloads Düzenle")
        print("2 - 🖥️ Desktop Düzenle")
        print("3 - 📂 Kendi Klasörünü Seç")
        print("4 - 🔙 Geri")

        secim = input("\nSeçimin: ")

        if secim == "1":

            home = os.path.expanduser("~")

            downloads = os.path.join(home, "Downloads")

            organize_folder(downloads)

        elif secim == "2":

            home = os.path.expanduser("~")

            desktop = os.path.join(home, "OneDrive", "Desktop")

            if not os.path.exists(desktop):
                desktop = os.path.join(home, "Desktop")

            organize_folder(desktop)

        elif secim == "3":

            folder = input("\nKlasör yolu: ")

            organize_folder(folder)

        elif secim == "4":

            break

        else:

            print("\n❌ Geçersiz seçim!")
