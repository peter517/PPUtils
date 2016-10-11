import socket
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print "param len is not 4"
        exit(0)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    msg_to_send = sys.argv[3]

    print "server_ip=" + server_ip + ",server_port=" + str(server_port) + ",msg_to_send=" + msg_to_send

    address = (server_ip, server_port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)

    client_socket.send(msg_to_send)

    client_socket.close()
