import platform
import psutil
import socket
import time


def get_system_info():
    print("\nSystem Information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")


def get_network_info():
    print("\nNetwork Information:")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    net_info = psutil.net_if_addrs()
    for interface, addresses in net_info.items():
        print(f"\nInterface: {interface}")
        for address in addresses:
            print(f"  Address Family: {address.family.name}")
            print(f"  Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast: {address.broadcast}")


def get_disk_info():
    print("\nDisk Information:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Total Size: {usage.total / (1024 ** 3):.2f} GB")
            print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
            print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
            print(f"  Usage: {usage.percent}%")
        except PermissionError:
            continue


def wait_for_device():
    print("\nWaiting for a new device to connect...")
    known_devices = {p.device for p in psutil.disk_partitions(all=True)}
    while True:
        current_devices = {p.device for p in psutil.disk_partitions(all=True)}
        new_devices = current_devices - known_devices
        if new_devices:
            print(f"New device detected: {', '.join(new_devices)}")
            break
        time.sleep(1)


if __name__ == "__main__":
    wait_for_device()
    get_system_info()
    get_network_info()
    get_disk_info()

