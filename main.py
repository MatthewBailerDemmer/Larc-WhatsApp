import ClientSocket
import time

HOST = "larc.furb.br"
PORT = 1012
userId = 1943
password = "dghol"


client = ClientSocket.ClientSocket(HOST, PORT, userId, password) 

client.log_in()
time.sleep(15)

while True:
    client.send_message(0, "fala aew")
    time.sleep(3)
    client.get_messages()