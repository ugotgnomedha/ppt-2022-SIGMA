import socket
import os


def mover():
    try:
        sock.sendall(b'GLUE_PUMP_OFF')

        sock.sendall(b'YOUNG_DRAW: 1.25:-50.79: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:0: -41.8:')
        sock.sendall(b'GLUE_PUMP_ON')

        sock.sendall(b'YOUNG_DRAW: -1.28:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1.41:0.59: 0:')
        sock.sendall(b'YOUNG_DRAW: -1.6:1.6: 0:')
        sock.sendall(b'YOUNG_DRAW: -1.34:1.23: 0:')
        sock.sendall(b'YOUNG_DRAW: -2.36:1.71: 0:')
        sock.sendall(b'YOUNG_DRAW: -2.57:1.37: 0:')
        sock.sendall(b'YOUNG_DRAW: -2.74:1: 0:')
        sock.sendall(b'YOUNG_DRAW: -2.851:0.6: 0:')
        sock.sendall(b'YOUNG_DRAW: -2.9:0.2: 0:')
        sock.sendall(b'YOUNG_DRAW: -15.85:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:8.04: 0:')

        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: -10.05:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:4: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 10:0: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:12: 0:')

        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: -10.05:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:4: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 10:0: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:12: 0:')

        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: -10.05:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:4: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 10:0: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:12: 0:')

        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: -10.05:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:4: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 10:0: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:12: 0:')

        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: -10:0: 0:')
        sock.sendall(b'YOUNG_DRAW: -1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:4: 0:')
        sock.sendall(b'YOUNG_DRAW: 1:1: 0:')
        sock.sendall(b'YOUNG_DRAW: 18.17:0: 0:')

        sock.sendall(b'YOUNG_DRAW: 3.22:-0.3: 0:')
        sock.sendall(b'YOUNG_DRAW: 3.11:-0.89: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.89:-1.45: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.58:1.96: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.17:-2.4: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.68:-2.77: 0:')
        sock.sendall(b'YOUNG_DRAW: 0.92:-2.28: 0:')

        sock.sendall(b'YOUNG_DRAW: 1.25:-3.04: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.7:-2.81: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.12:-2.52: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.48:-2.16: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.78:-1.75: 0:')
        sock.sendall(b'YOUNG_DRAW: 3.02:-1.3: 0:')
        sock.sendall(b'YOUNG_DRAW: 3.18:-0.82: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.82:-0.31: 0:')

        sock.sendall(b'YOUNG_DRAW: 2.68:-0.32: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.6:-0.73: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.45:-1.13: 0:')
        sock.sendall(b'YOUNG_DRAW: 2.25:-1.49: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.99:-1.82: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.69:-2.11: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.34:-2.34: 0:')
        sock.sendall(b'YOUNG_DRAW: 0.96:-2.52: 0:')
        sock.sendall(b'YOUNG_DRAW: 0.56:-2.64: 0:')
        sock.sendall(b'YOUNG_DRAW: 0.15:-2.35: 0:')

        sock.sendall(b'YOUNG_DRAW: 0:-8.81: 0:')

        sock.sendall(b'YOUNG_DRAW: 0.18:-2.73: 0:')
        sock.sendall(b'YOUNG_DRAW: 0.53:-2.68: 0:')
        sock.sendall(b'YOUNG_DRAW: 0.88:-2.59: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.21:-2.45: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.52:-2.27: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.8:-2.05: 0:')
        sock.sendall(b'YOUNG_DRAW: 1.46:-1.33: 0:')

        sock.sendall(b'YOUNG_DRAW: 0.73:-1.54: 0:')
        sock.sendall(b'YOUNG_DRAW: 0:-1.43: 0:')
        sock.sendall(b'YOUNG_DRAW: -0.59:-1.41: 0:')
        sock.sendall(b'YOUNG_DRAW: -30.18:-30.18: 0:')
        sock.sendall(b'YOUNG_DRAW: -1.41:-0.59: 0:')

        sock.sendall(b'GLUE_PUMP_OFF')
        sock.sendall(b'YOUNG_DRAW: 0:0: 41.8:')
        sock.sendall(b'YOUNG_DRAW: -1.25:50.79: 0:')
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(0)


def establishConnRobot():
    try:
        sock.sendall(b'YOUNG_INIT')
        data = sock.recv(4096)
        if data.decode() == "YOUNG_START":
            print("Установлено подключение к контуру безопасности")
            mover()
    except:
        print("Не удалось установить подключение / Превышено время ожидания")
        exit(0)


sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

UDP_IP = os.environ['host']
UDP_PORT = os.environ['port']

# UDP_IP = "localhost"
# UDP_PORT = 5005

addr = (UDP_IP, int(UDP_PORT))

sock.connect(addr)

establishConnRobot()  # Establish connection to server.
