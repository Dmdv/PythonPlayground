import socket, sys, os

def start():
    print "Starting " + __file__

    host = "example.ru"
    open_ports = []
    common_ports = { 21, 22, 23, 25, 53, 69, 80, 88, 109, 110, 123, 137, 138, 139, 143, 156, 161, 389, 443, 445, 500, 546, 547, 587, 660, 995, 993, 2086,2087, 2082, 2083, 3306, 8443, 10000 }
    start_port = 1
    end_port = 10
    name = socket.gethostbyname(host)
    print ("Probing '{0}' with IP = '{1}'".format(host, name))
    
    for port in sorted(common_ports):
        sys.stdout.flush()
        print(port)
        response = probe_port(host, port)
        if response == 0:
            open_ports.append(port)
        if not port == end_port:
            sys.stdout.write('\b' * len(str(port)))
    
    if open_ports:
        print("Opened ports:")
        print(sorted(open_ports))
    else:
        print("No opened ports found")


def probe_port(host, port, result = 1):
    try:
        sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockObj.settimeout(0.5)
        r = sockObj.connect_ex((host, port))
        if r == 0:
            result = r
        sockObj.close()
    except Exception as e:
        print (e.message)
        pass
    return result

if __name__ == "__main__":
    start()