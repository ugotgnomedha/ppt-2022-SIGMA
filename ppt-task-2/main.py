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
        sock.sendto(b'', addr)
        # sock.sendto(b'INIT_CIRC', (int(UDP_IP), int(UDP_PORT)))
        data = sock.recv(4096)
        trashResponseCheck(data)  # Check if response is unclear.
        if data == "OK":
            print("Установлено подключение к контуру безопасности")
            while stateChecker():  # Check server status.
                i = 0  # Do nothing if state is normal
            else:
                print("Внимание, нарушение контура безопасности!")
                stopper()  # Alarm
    except socket.timeout:
        print("Не удалось установить подключение / Превышено время ожидания")


def stateChecker():
    sock.sendto(b'CIRC_STATE', addr)
    data = sock.recv(4096)
    trashResponseCheck(data)  # Check if response is unclear.
    state = True
    if data == "SOLID":
        state = True
    elif data == "BREAK":
        state = False
    return state


def stopper():
    sock.sendto(b'ALARM', addr)
    data = sock.recv(4096)
    trashResponseCheck(data)  # Check if response is unclear.
    if data != "STOPPED":
        stopper()  # Send ALARM again if previous didn't stop the server.
    elif data == "STOPPED":
        stateDetails()  # Get detailed info about state.


def stateDetails():
    sock.sendto(b'CIRC_ALL_STATE', addr)
    data = sock.recv(4096)
    trashResponseCheck(data)  # Check if response is unclear.
    response = json.loads(data)
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
sock.settimeout(5)  # 5 second timeout on commands

UDP_IP = os.environ['host']
UDP_PORT = os.environ['port']

addr = (UDP_IP, UDP_PORT)

establishConn()  # Establish connection to server.

sock.close()
