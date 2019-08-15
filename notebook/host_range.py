import subprocess
import ipaddress
import tabulate

ip_addresses_gen = [ipaddress.ip_address(f'192.162.0.{x}') for x in range(5)]
reachable =[]
unreachable = []
def host_ping_range(ip_addresses_gen):
    for ip in ip_addresses_gen:
        code = subprocess.call(["ping", str(ip)],shell=False,  stdout=subprocess.PIPE)
        if code == 0:
            reachable.append(ip)
            print(f"{ip} Узел доступен!")
        else:
            unreachable.append(ip)
            print(f"{ip} Узел недоступен!")



host_ping_range(ip_addresses_gen)

def host_range_ping_tab():

    host_dict ={'reachable':reachable, 'unreachable':unreachable}

    print(tabulate.tabulate(host_dict, headers = 'keys', tablefmt='grid'))
host_range_ping_tab()