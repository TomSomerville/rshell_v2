import socket, pickle, base64, ast, time

class encrypt_data():
    def __init__(self):
        pass

    def prepdata(data):
        pickled = pickle.dumps(data)
        b64ed = base64.b64encode(pickled)
        xored = xord_text(b64ed)
        return xored

    def unprepdata(data):
        unxored = xord_text(data)
        unb64ed = base64.b64decode(ast.literal_eval(unxored))
        unpickled = pickle.loads(unb64ed)
        return unpickled

    def bytes_xor(a, b) :
        return bytes(x ^ y for x, y in zip(a, b))

    def xord_text(string):
        key = bytearray("k", "utf-8")
        xord_bytes = []
        xord_string = []
        for i in str(string):
            xord_bytes.append(bytes_xor(bytearray(i,'utf-8'), key))

        for i in xord_bytes:
            xord_string.append(i.decode('utf-8'))

        return ''.join(xord_string)


def send_data(data):
    HOST = "localhost"
    PORT = 1337
    postprepdata = prepdata(data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(postprepdata)
    response = s.recv(1024)
    return response

#print(send_data(b'test'))

testvar = "This is my custom crypto!"

print("Encrpyting the string: ", testvar, "\n--------------")
results = prepdata(testvar)
time.sleep(1)
print("Encrypted String is: ", results, "\n------------------------")
time.sleep(1)
print("Decrypting the encrypted string: ", results, "\n-------------" )
decrypted = unprepdata(results)
time.sleep(1)
print("Decrypted string is: ", decrypted, "\n--------------")
time.sleep(1)
print("Complete")

