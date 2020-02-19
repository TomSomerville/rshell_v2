import sys, traceback, socket, pickle
from _thread import *
import ast

HOST = "localhost"
PORT = 1337

arglist = ['def1', 'def2']

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
                break
            else:
                print("Received Data: ", data)
                stringed = data.decode('utf-8')
                decoded = xord_text(stringed)
                print("decoded Data:", decoded)
                depickpled = pickle.loads(ast.literal_eval(decoded))
                print("De-pickled: ", depickpled)
                if depickpled[0] in arglist:
                    reply = execdef(depickpled[0], depickpled[1])
                else:
                    reply = "Unknown Action"
                conn.sendall(str(reply).encode("utf-8"))
        except:
            print(sys.exc_info())
            print("Lost Connection To " + str(addr))
            break
    conn.close()

def execdef(defname, input):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(defname)
    return method(input)

def def1(input):
    reply = 'ran def1'
    return reply

def def2(input):
    reply = 'ran def2'
    return reply

def bytes_xor(a, b) :
    return bytes(x ^ y for x, y in zip(a, b))

def xord_text(string):
    key = bytearray("k", "utf-8")
    xord_bytes = []
    xord_string = []
    for i in string:
        xord_bytes.append(bytes_xor(bytearray(i,'utf-8'), key))

    for i in xord_bytes:
        xord_string.append(i.decode('utf-8'))

    return ''.join(xord_string)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unable to start server. Received exception: \n", e)



