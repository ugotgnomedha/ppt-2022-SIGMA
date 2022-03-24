import socket
import json
import os


def trashResponseCheck(response):
    if response == "EXIT 1":
        exit(1)
    elif response == "EXIT 2":
        exit(2)


def establishConn():
    try:
        sock.sendall(b'INIT_CIRC')
        data = sock.recv(4096)
        trashResponseCheck(data.decode())  # Check if response is unclear.
        if data.decode() == "OK":
            print("Установлено подключение к контуру безопасности")
            while stateChecker():  # Check server status.
                i = 0  # Do nothing if state is normal
            else:
                print("Внимание, нарушение контура безопасности!")
                stopper()  # Alarm
    except socket.timeout:
        print("Не удалось установить подключение / Превышено время ожидания")


def stateChecker():
    sock.sendall(b'CIRC_STATE')
    data = sock.recv(4096)
    trashResponseCheck(data.decode())  # Check if response is unclear.
    state = True
    if data.decode() == "SOLID":
        state = True
    elif data.decode() == "BREAK":
        state = False
    return state


def stopper():
    sock.sendall(b'ALARM')
    data = sock.recv(4096)
    trashResponseCheck(data.decode())  # Check if response is unclear.
    if data.decode() != "STOPPED":
        stopper()  # Send ALARM again if previous didn't stop the server.
    elif data.decode() == "STOPPED":
        stateDetails()  # Get detailed info about state.


def stateDetails():
    sock.sendall(b'CIRC_ALL_STATE')
    data = sock.recv(4096)
    trashResponseCheck(data.decode())  # Check if response is unclear.
    response = json.loads(data.decode())
    responseParser(response)


def responseParser(response):
    if response["state"] != "true":
        print("разрыв контура безопасности")
    if response["ebutton"] == "true":
        print("кнопка нажата (оператор остановил работу)")
    if response["end_cap"] == "true":
        print("концевик зажат (достигнута предельная деформация демпфера)")
    print("Расстояние измеренное с дальномеров контура безопасности: " + response["dist"])


sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

UDP_IP = os.environ['host']
UDP_PORT = os.environ['port']

# UDP_IP = "localhost"
# UDP_PORT = 5005

addr = (UDP_IP, int(UDP_PORT))

sock.connect(addr)

establishConn()  # Establish connection to server.

sock.close()
