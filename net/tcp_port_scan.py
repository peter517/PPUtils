import socket
import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "param len is not 4"
        exit(0)

    server_ip = sys.argv[1]

    print "server_ip=" + server_ip

    for i in range(1024, 65535):
        address = (server_ip, i)
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(address)
        except Exception, e:
            pass
        else:
            print "tcp port " + str(i) + " is available to connect"
        finally:
            client_socket.close()
