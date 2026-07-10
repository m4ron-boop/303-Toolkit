import os
import shutil


def start_organizer():
    print("=" * 35)
    print("      FILE ORGANIZER")
    print("=" * 35)

    folder = input("\nKlasör yolu: ")

    if not os.path.exists(folder):
        print("\n❌ Böyle bir klasör bulunamadı!")
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

    print("\nDosyalar düzenleniyor...\n")

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1].lower()

            if ext in extensions:

                target_folder = os.path.join(folder, extensions[ext])

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, file))

                print(f"✅ {file} -> {extensions[ext]}")

    print("\n🎉 İşlem tamamlandı!")