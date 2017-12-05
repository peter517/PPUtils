#!/usr/bin/env python
# coding=utf8

import socket
import sys
import thread
import time

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "param len is not 3"
        exit(0)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    print "server_ip=" + server_ip + ",server_port=" + str(server_port)
    wait_time_s = 10000;
    connected_num = 0
    address = (server_ip, server_port)

    def connect_target(threadName, delay):
        global connected_num
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(address)
        except Exception, e:
            pass
        else:
            connected_num = connected_num + 1
            print "tcp connected " + str(connected_num) + "\n"
            time.sleep(wait_time_s)

    try:
        for i in range(1, 10):
            thread.start_new_thread(connect_target, ("Thread-" + str(i), ''))
    except:
        print "Error: unable to start thread"

    time.sleep(wait_time_s)
