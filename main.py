import ClientSocket
import time
from flask import Flask, render_template, request
import requests

HOST = "larc.furb.br"
PORT = 1012
userId = 1943
password = "dghol"



app = Flask(__name__)

client = ClientSocket.ClientSocket(HOST, PORT, userId, password) 

client.log_in()
time.sleep(15)

#while True:
#    option = int(input(f"1 para entrar no jogo\n2 para parar\n3 para sair do jogo\n4 para pegar carta\n5 para ver os players\n6 para ver logados\n"))
#    if option == 1:
#        client.send_message_game("ENTER")
#    elif option == 2:
#        client.send_message_game("STOP")
#    elif option == 3:
#        client.send_message_game("QUIT")
#    elif option == 4:
#        client.get_card()
#    elif option == 5:
#        client.get_players()
#    elif option == 6:
#        client.get_score()


@app.route('/')
def get_all_posts():
    user = request.args.get("user")
    logged_in = client.get_score().split(':')
    result = []

    i = 0
    while i < len(logged_in) - 1:
        tuplezinha  = f"{logged_in[i]}. {logged_in[i + 1]}"
        result.append(tuplezinha)
        i += 3

    return render_template("index.html", logged_users=result, message_user=user)
        

if __name__ == "__main__":
    app.run(debug=True, port=5001)