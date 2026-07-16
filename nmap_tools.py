import os
import shutil 


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def check_nmap():
    """
    Check if nmap is installed on the system.
    """
    return shutil.which("nmap") is not None
   

def nmap_menu():
    while True:
        clear()

        print("=" * 40)
        print("      NMAP TOOLS")
        print("=" * 40)

        if check_nmap():
           print("✅ Nmap is installed.")
        else:
            print("❌ Nmap is not installed. Please install it to use Nmap tools.")

        print("=" * 40)

        print("1 - Ping Scan")
        print("2 - Port Scan")
        print("3 - Service Version Detection")
        print("4 - OS Detection")
        print("5 - Scan a Network")
        print("6 - Back")

        print("=" * 40)

        choice = input("Select: ")

        if choice == "6":
            break

        print("\n🚧 This feature is under development.")
        input("\nPress Enter to continue...")