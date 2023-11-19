
import nmap

import re



def NmapScanner(ip_add,prange):
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

    port_min = 0
    port_max = 65535




    open_ports = []

    while True:
        ip_add_entered = ip_add
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is a valid ip address")
            break
        else: return(f"{ip_add_entered} not a valid ip address")

    mmm =""
    while True:
        
        #print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = prange#input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    nm = nmap.PortScanner()

    for port in range(port_min, port_max + 1):
        try:
            
            result = nm.scan(ip_add_entered, str(port))
            
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
            mmm = mmm + f"Port {port} is {port_status}\n"
        except:
            
            print(f"Cannot scan port {port}.")
            mmm = mmm + f"Cannot scan port {port}.\n"
    return mmm
            

