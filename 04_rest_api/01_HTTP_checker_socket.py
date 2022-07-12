"""
2.1.1.1 HTTP server availability checker
https://edube.org/learn/pcpp1-working-with-restful-apis/http-server-availability-checker
We want you to write a simple CLI (Command Line Interface) tool which can be used in order to diagnose the current
status of a particular http server. The tool should accept one or two command line arguments:
    (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be
    extremely simple, we just want to know if the server is dead or alive)
    (optional) the server's port number (any absence of the argument means that the tool should use port 80)
    use the HEAD method instead of GET — it forces the server to send the full response header but without any content;
    it's enough to check if the server is working properly; the rest of the request remains the same as for GET.
We also assume that:
    the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error
    message and returns an exit code equal to 1;
    if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535,
    the tool prints an error message and returns an exit code equal to 2;
    if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
    if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
    if the connection succeeds, the very first line of the server’s response is printed.
Hints:
    to access command line arguments, use the argv variable from the sys module; its length is always one more than the
    actual number of arguments, as argv[0] stores your script's name; this means that the first argument is at argv[1]
    and the second at argv[2]; don't forget that the command line arguments are always strings!
    returning an exit code equal to n can be achieved by invoking the exit(n) function.
Assuming that the tool is placed in a source file name sitechecker.py, here are some real-use cases:
Command prompt -- sitechecker.py
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
