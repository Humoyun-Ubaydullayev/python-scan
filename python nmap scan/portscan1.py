import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("ip manzilingizni kiriting: ")
port = int(input("xoxlagan portingizni kiriting: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("bu port yopiq")
    else:
        print("bu port ochiq")

portScanner(port)