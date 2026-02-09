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
    option = int(input(f"1 para entrar no jogo\nn2 para parar\n3 para sair do jogo"))
    if option == 1:
        client.send_message_game("ENTER")
    elif option == 2:
        client.send_message_game("STOP")
    elif option == 3:
        client.send_message_game("QUIT")