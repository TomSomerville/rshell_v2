import socket, pickle

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

def send_data(data):
    HOST = "localhost"
    PORT = 1337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pickled_data = pickle.dumps(data)
    s.connect((HOST, PORT))
    s.sendall(xord_text(str(pickled_data)).encode('utf-8'))
    response = s.recv(1024)
    return response

def def1(input):
    data = "def1", input
    result = send_data(data)
    print(result)

def def2(input):
    data = "def2", input
    result = send_data(data)
    print(result)


print(def2('def2 this is longer'))

# test