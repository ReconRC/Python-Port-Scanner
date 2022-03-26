import socket
import threading
from queue import Queue

target = '192.168.1.254'
queue = Queue()
openPorts = []


def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def getPorts(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.port(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports separated by blanks:")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)


def queueWorker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print('Port {} is open!'.format(port))
            openPorts.append(port)


def runScanner(threads, mode):
    getPorts(mode)
    threadList = []

    for t in range(threads):
        thread = threading.Thread(target=queueWorker)
        threadList.append(thread)

    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()

    print(f'Open ports are: {openPorts}')

mode = int(input(f'Enter the corresponding number for mode you wish to use\n(1)Scan ports 1-1024\n(2)Scan ports 1-49152\n(3)Scan ports 20, 21, 22, 23, 25, 53, 80, 110, and 443\n(4)Choose your own ports\nEnter Here:'))
runScanner(200,mode)

