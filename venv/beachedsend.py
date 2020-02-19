import socket
def send_data(host,port,string):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    send_data = string.encode("utf-8")
    s.sendall(send_data)
    response = s.recv(1024)
    return response