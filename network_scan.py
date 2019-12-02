import socket
import sys

def get_ipaddress():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8",80))
  r = s.getsockname()[0]
  s.close()
  return r

def scan_internal(ip_addr):
    sct = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    subnet_ = ip_addr[0:4]
    host_name = "None"
    print("Scanning Network...")
    print("My ip_addr: " + ip_addr)
    print("*"*93)
    print("Status                    Hostname                    IP_addr                    MAC_addr")
    print("*"*93)
    try:
        if subnet_ == "192.":
            for a in range(1, 255):
                scan_ip = (ip_addr[0:10] + str(a))
                try:
                    host_name = socket.gethostbyaddr(scan_ip)[0]
                    sct.connect((scan_ip, 8080))
                    sct.settimeout(5)
                    print("found                     " + host_name + "        " + scan_ip + "")
                except Exception as err:
                    print("not found                 " + "None" + "                        " + scan_ip)


        elif subnet_ == "172.":
            for a in range(1, 255):
                scan_ip = (ip_addr[0:9] + "" + str(a))
                try:
                    host_name = socket.gethostbyaddr(scan_ip)[0]
                    sct.connect((scan_ip, 8080))
                    sct.settimeout(5)
                    print("found                     " + host_name + "        " + scan_ip + "")
                except Exception as err:
                    print("not found                 " + "None" + "                        " + scan_ip)
        else:
            print("wrong ip")

    except KeyboardInterrupt:
        print("bye~ bye~")
        sys.exit(0)

if __name__ == '__main__':
    my_ip = get_ipaddress()
    scan_internal(my_ip)
