from sys import argv
import subprocess
import re
from rich.table import Table
from rich.live import Live
from rich import box

def get_range(ip):
    ip = ip.split("/")
    cidr = int(ip[1])
    ip = ip[0].split(".")
    bip = list(map(lambda element: bin(int(element)).removeprefix("0b").zfill(8), ip))
    bin_ip = "".join(bip)
    subnet = bin_ip[:cidr]
    bin_ip = subnet + "0" * (31 - cidr) + "1"
    bin_ip = [bin_ip[:8], bin_ip[8:16], bin_ip[16:24], bin_ip[24:]]
    first_ip = list(map(lambda element: int(element, 2), bin_ip))
    ip_range = (2 ** (32 - cidr)) - 2
    return first_ip, ip_range

def list_ips(ip, ip_range):
    ip_list = []
    for _ in range(ip_range):
        ip_list.append(format_ip(ip))
        ip[-1] += 1
        for i in range(-1, -5, -1):
            if ip[i] > 255:
                ip[i] = 0
                ip[i - 1] += 1
    return ip_list

def format_ip(ip):
    return ".".join(map(str, ip))

def ping_ip(ip):
    try:
        output = subprocess.run(["ping", "-c", "1", ip], timeout=5, capture_output=True)
        if output.stdout:
            output.stdout = output.stdout.decode()
            status = "UP"
            detail = re.search("time=.+ms", output.stdout).group().replace("time=", "")
        else:
            status = "DOWN"
            detail = "No response"
    except subprocess.TimeoutExpired:
        status = "ERROR"
        detail = "Connection timeout"
    return [ip, status, detail]

first_ip, ip_range = get_range(argv[1])

table = Table("IP", "Status", "Response", box=box.ASCII_DOUBLE_HEAD)

with Live(table, auto_refresh=False) as live:
    try:
        for ip in list_ips(first_ip, ip_range):
            response = ping_ip(ip)
            table.add_row(response[0], response[1], response[2])
            live.refresh()
    except KeyboardInterrupt:
        live.stop()