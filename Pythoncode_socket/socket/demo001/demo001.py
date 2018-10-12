import socket
from binascii import hexlify


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name:%s" % host_name)
    print("IP address: %s" % ip_address)


def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print('ip address: %s' % socket.gethostbyname(remote_host))
    except socket.error:
        print('%s: %s' % remote_host)



def convery_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print('IP address: %s => Packed: %s, Unpacked: %s'\
              %(ip_addr, hexlify(packed_ip_addr),unpacked_ip_addr))


def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 53]:
        print('port: %s => service name: %s' %(port, socket.getservbyport(port, protocolname)))



if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info()
    convery_ip4_address()
    find_service_name()
