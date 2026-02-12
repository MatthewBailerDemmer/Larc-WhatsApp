import socket
import threading
import time   



class ClientSocket:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        



    def KeepAlive(self, stop_event):
        while not stop_event.is_set():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                #s.connect((self.HOST, self.PORT))
                #msg = f"GET USERS {self.userId}:{self.password}\r\n"
                #s.sendall(msg.encode("ascii"))
                #data = s.recv(1024)
                #print(f"Logged In: {data.decode("utf-8")!r}")
                time.sleep(6)
                
    def get_score(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                #s.connect((self.HOST, self.PORT))
                #msg = f"GET USERS {self.userId}:{self.password}\r\n"
                #s.sendall(msg.encode("ascii"))
                #data = s.recv(1024)
                #print(f"Logged In: {data.decode("utf-8")!r}")
                #return data.decode("utf-8")
                return "222:Kid Bengala:0:1943:Matheus Bailer:2:69:tadalafelas:0"


    def log_in(self, username, password):
        self.userId = username
        self.password = password
        self.stop_event = threading.Event()
        self.threadKeepAlive = threading.Thread(target=self.KeepAlive, args=(self.stop_event,))
        self.threadKeepAlive.start()
    def log_out(self):
        self.stop_event.set()
        self.threadKeepAlive.join()

    def get_messages(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #s.connect((self.HOST, self.PORT))
            #msg = f"GET MESSAGE {self.userId}:{self.password}\r\n"
            #s.sendall(msg.encode("ascii"))
            #data = s.recv(1024)
            #print(f"Messages received: {data.decode("utf-8")!r}")
            return "1943:Hallow"

    def send_message(self, user2Id, sending):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            #s.settimeout(5)
            #msg = f"SEND MESSAGE {self.userId}:{self.password}:{user2Id}:{sending}\r\n".encode("ascii")
            #s.sendto(msg ,(self.HOST, 1011))
            try:
                #data, addr = s.recvfrom(1024)
                #print(f"Sent message: {data.decode("utf-8")!r}")
                print(f"{user2Id}: {sending}")
            except socket.timeout:
                print("No message received from server")

    def get_players(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #s.connect((self.HOST, self.PORT))
            #msg = f"GET PLAYERS {self.userId}:{self.password}\r\n"
            #s.sendall(msg.encode("ascii"))
            #data = s.recv(1024)
            #print(f"Players: {data.decode("utf-8")!r}")
            return "222:PLAYING:1943:IDLE:69:GETTING"

    def get_card(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #s.connect((self.HOST, self.PORT))
            #msg = f"GET CARD {self.userId}:{self.password}\r\n"
            #s.sendall(msg.encode("ascii"))
            #data = s.recv(1024)
            #print(f"CARD: {data.decode("utf-8")!r}")
            return "J:DIAMOND"

    def send_message_game(self, msg):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            #s.settimeout(5)
            #msg = f"SEND GAME {self.userId}:{self.password}:{msg}\r\n".encode("ascii")
            #s.sendto(msg ,(self.HOST, 1011))
            #try:
            #    data, addr = s.recvfrom(1024)
            #    print(f"Sent message: {data.decode("utf-8")!r}")
            #except socket.timeout:
            #    print("No message received from server")
            print(msg)