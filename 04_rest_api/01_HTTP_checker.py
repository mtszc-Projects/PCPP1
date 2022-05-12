"""
2.1.1.1 HTTP server availability checker
https://edube.org/learn/pcpp1-working-with-restful-apis/http-server-availability-checker
"""
import sys
import socket
import logging

try:
    if len(sys.argv) not in [2, 3]:
        sys.stdout.write("Wrong arguments quantity! There should be one or two arguments.\n")
        sys.exit(1)
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
        if not 1 < int(sys.argv[2]) < 65535:
            sys.stdout.write("Second argument is wrong! It should be a number in range from 1 to 65535.\n")
            sys.exit(2)
    else:
        address = sys.argv[1]
        port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((address, port))
    sock.send(b"HEAD / HTTP/1.1\r\nHost: " + bytes(address, "utf8") + b"\r\nConnection: close\r\n\r\n")
    try:
        reply = sock.recv(1000)
    except Exception as e:
        sys.stdout.write("Timeout error.\n")
        logging.exception(e)
        sys.exit(3)
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    sys.stdout.write(str(reply).split('\\r')[0][2:] + '\n')
except Exception as e:
    sys.stdout.write("Error unknown.\n")
    logging.exception(e)
    sys.exit(4)
