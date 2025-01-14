import beachedcrypt, beachedsend, time, socket, sys, ast
from _thread import *

HOST = "localhost"
PORT = 1337

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen()
    print("Server Started")
    while True:
        try:
            conn, addr = s.accept()
            print("Connected to:", addr)
            start_new_thread(threaded_client, (conn,addr))
        except Exception as e:
            print("Error With Client Connection. Received Exception: \n")

def threaded_client(conn,addr):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                print(str(addr) + " Disconnected")
                conn.close()
                break
            else:
                print("Received Data: ", data)
                conn.sendall(handledata(data))
        except:
            print(sys.exc_info())
            print("Lost Connection To " + str(addr))
            break
    conn.close()

def handledata(data):
    arglist = [
        "heartbeat",
        "execcmd",
    ]
    decodeddata = beachedcrypt.decrypt(data.decode('utf-8'))
    aid = decodeddata[0]
    command = decodeddata[1]
    if command in arglist:
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(command)
        return method()
    else:
        return b"Unknown Action"

def heartbeat():
    return b'ACK'

main()