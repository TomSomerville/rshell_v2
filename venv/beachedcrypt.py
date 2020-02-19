import socket, pickle, base64, ast, time, sys

def encrypt(data):
    pickled = pickle.dumps(data)
    b64ed = base64.b64encode(pickled)
    xored = xord_text(b64ed)
    return xored

def decrypt(data):
    unxored = xord_text(data)
    unb64ed = base64.b64decode(ast.literal_eval(unxored))
    unpickled = pickle.loads(unb64ed)
    return unpickled

def bytes_xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def xord_text(string):
    key = bytearray("k", "utf-8")
    xord_bytes = []
    xord_string = []
    for i in str(string):
        xord_bytes.append(bytes_xor(bytearray(i, 'utf-8'), key))

    for i in xord_bytes:
        xord_string.append(i.decode('utf-8'))

    return ''.join(xord_string)