import ipaddress
import subprocess
import socket
import threading


def banner():

    print("=" * 35)
    print("      NETWORK SCANNER")
    print("=" * 35)


def get_local_ip():

    hostname = socket.gethostname()

    return socket.gethostbyname(hostname)


def get_network():

    ip = get_local_ip()

    network = ipaddress.ip_network(ip + "/24", strict=False)

    return network


def get_hosts():

    network = get_network()

    return list(network.hosts())


def ping(ip):

    result = subprocess.run(
        ["ping", "-n", "1", "-w", "300", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


# Aktif cihazlar burada tutulacak
active_hosts = []


def scan(ip):

    if ping(ip):

        print(f"🟢 {ip}")

        active_hosts.append(str(ip))


if __name__ == "__main__":

    banner()

    print(f"\n💻 Bilgisayar Adı : {socket.gethostname()}")
    print(f"🏠 Local IP       : {get_local_ip()}")
    print(f"🌐 Network        : {get_network()}")

    hosts = get_hosts()

    print(f"💻 Toplam Host    : {len(hosts)}")

    print("\n🌐 Ağ taranıyor...\n")

    threads = []

    for host in hosts:

        t = threading.Thread(target=scan, args=(host,))

        threads.append(t)

        t.start()

    for t in threads:

        t.join()

    print("\n===================================")
    print("Aktif Cihazlar")
    print("===================================")

    for host in active_hosts:

        print(f"✅ {host}")