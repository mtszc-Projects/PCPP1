"""
2.1.1.4 Server checker once again
https://edube.org/learn/pcpp1-working-with-restful-apis/server-checker-once-again
"""
import sys
import requests
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
    try:
        reply = requests.head(f'http://{address}:{port}', allow_redirects=True, timeout=5)
        print(f'Status code: {reply.status_code}')
    except requests.exceptions.Timeout:
        print("Connection dropped because of inability to connect for seconds.")
    except requests.exceptions.ConnectionError:
        print("Can't connect to provided endpoint.")
    except requests.exceptions.InvalidURL:
        print('Unknown URL.')
except Exception as e:
    sys.stdout.write("Error unknown.\n")
    logging.exception(e)
    sys.exit(4)
