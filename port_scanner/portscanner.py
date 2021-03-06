# author: axi0m
# purpose: rudimentary port scanner (TCP CONNECT port scan)
# usage: portscanner.py --host --port
# example: portscanner.py --host 10.1.1.1 --port 21,22,23
# changelog: 12/11/18 - initial creation
# 12/12/2018 - added threading, fixed functions up a bit, fixed byte
# format for socket data

"""

TODO: Add the following scan types
TODO: TCP SYN, TCP XMAS, TCP FIN, TCP NULL, TCP SYN
TODO: https://nmap.org/book/man-port-scanning-techniques.html

TODO: Add Unit Tests
TODO: Add Logging
TODO: Add Colorized Output via colorama
TODO: Add pprint type functionality
TODO: Add output via JSON

Weird bug in recv from port 22, results are returned and are bytes but for w/e
reason the CLI hangs and never completes. Blocking mode issue?

"""

import argparse
import socket
import threading
from colorama import Fore, init

# init colorama
init()

SCREEN_LOCK = threading.Semaphore(value=1)


def conn_scan(host, port):
    """ TCP scan and banner receiver"""
    try:
        socket.setdefaulttimeout(1)
        conn_socket = socket.socket()
        conn_socket.connect((host, port))
        conn_socket.send("SampleData\r\n".encode("utf-8"))
        results = conn_socket.recv(100)
        SCREEN_LOCK.acquire()
        print(Fore.GREEN + f"[+] {port}/tcp open")
        print(Fore.GREEN + f"[+] {results.decode('utf-8')}")

    except TimeoutError as timeout_error:
        SCREEN_LOCK.acquire()
        print(
            Fore.LIGHTYELLOW_EX
            + f"[!] Connection timeout on port {port}: {timeout_error}"
        )

    except KeyboardInterrupt as keybd_err:
        SCREEN_LOCK.acquire()
        print(Fore.LIGHTYELLOW_EX + f"[!] Keyboard interrupt: {keybd_err}")

    except Exception as generic_err:
        SCREEN_LOCK.acquire()
        print(
            Fore.LIGHTYELLOW_EX
            + f"[-] Generic exception port most likely closed or network timeout: {generic_err}"
        )
        print(Fore.LIGHTYELLOW_EX + f"[-] {port}/tcp closed")

    finally:
        SCREEN_LOCK.release()
        conn_socket.close()


def port_scan(host, port):
    """ Perform scan for given hostname and TCP port number(s)"""
    try:
        targetipv4 = socket.gethostbyname(host)
        print(
            Fore.LIGHTYELLOW_EX
            + f"[-] DEBUG Host IP address resolved via DNS: {targetipv4}"
        )

    except KeyboardInterrupt as keybd_err:
        print(Fore.RED + f"[!] ERROR Keyboard interrupt handled: {keybd_err}")
        return None

    except Exception as generic_err:
        print(Fore.RED + f"[!] ERROR cannot resolve host {host}: {generic_err}")
        return None

    if targetipv4 is not None:
        try:
            targetname = socket.gethostbyaddr(host)
            print(f"DNS results for: {targetname[0]}")
        except Exception as generic_err:
            print(
                f"[!] ERROR Exception encountered during address resolution: {generic_err}"
            )
            print(f"DNS results for: {targetipv4}")

        socket.setdefaulttimeout(1)

        for tcp_port in port:
            thread_object = threading.Thread(
                target=conn_scan, args=(host, int(tcp_port))
            )
            thread_object.start()


def main():
    """ Main function call to parse arguments and run port scan"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", nargs="?", action="store", dest="host", help="Host to scan."
    )
    parser.add_argument(
        "--port",
        nargs="+",
        action="store",
        dest="port",
        help="Port(s) to scan, csv and space delimited",
    )

    args = parser.parse_args()

    host = args.host
    port = args.port

    if host is None:
        parser.print_help()
        exit(0)

    if port is None:
        parser.print_help()
        exit(0)

    port_scan(host, port)


if __name__ == "__main__":
    main()
