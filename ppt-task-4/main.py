import socket
import os


def trashResponseCheck(response):
    if response == "EXIT 1":
        exit(1)
    elif response == "EXIT 2":
        exit(2)


def mainMover():
    ########### START MOVING HERE
    try:
        sock.sendall(b'RS_HOME:')  # Move home
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.

        # MOVE
        # MOVE
        # MOVE
        # MOVE
        # MOVE

        sock.sendall(b'RS_DISCONNECT:')  # Disconnect from robot
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
        if data.decode() == "CLIENT_OFF":
            print("Разрыв соединения с роботом.")
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(555)


def lMove(CS, X, Y, Z, O, A, T):
    try:
        sock.sendall(b'RS_LMOVE:' + str.encode(CS) + b':' + bytes(X) + b':' + bytes(Y) + b':' + bytes(Z) + b':' + bytes(
            O) + b':' + bytes(A) + b':' + bytes(T) + b':')
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(555)


def jMove(CS, X, Y, Z, O, A, T):
    try:
        sock.sendall(b'RS_JMOVE:' + str.encode(CS) + b':' + bytes(X) + b':' + bytes(Y) + b':' + bytes(Z) + b':' + bytes(
            O) + b':' + bytes(A) + b':' + bytes(T) + b':')
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(555)


def moveDraw(X, Y, Z, O, A, T):
    try:
        sock.sendall(b'RS_DRAW:' + bytes(X) + b':' + bytes(Y) + b':' + bytes(Z) + b':' + bytes(O) + b':' + bytes(
            A) + b':' + bytes(T) + b':')
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(555)


def moveDrive(axis, degrees):
    try:
        sock.sendall(b'RS_DRIVE:' + bytes(axis) + b':' + bytes(degrees) + b':')
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(555)


def establishConn():
    try:
        sock.sendall(b'RS_CONNECT')
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
        if data.decode() == "RS_CONNECTED":
            print("Установлено подключение к роботу")
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(555)



sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

UDP_IP = os.environ['host']
UDP_PORT = os.environ['port']

# UDP_IP = "127.0.0.1"
# UDP_PORT = 5005

addr = (UDP_IP, int(UDP_PORT))

sock.connect(addr)

sock.settimeout(5)  # timeout for 5 seconds

establishConn()  # Establish connection to server.

mainMover()

sock.close()
