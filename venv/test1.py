import beachedcrypt, beachedsend, time

aid = "1A"

def heartbeat():
    hearbeat_data = aid, "heartbeat"
    return beachedsend.send_data('localhost',1337,beachedcrypt.encrypt(hearbeat_data))


while True:
    print(heartbeat())
    time.sleep(5)
