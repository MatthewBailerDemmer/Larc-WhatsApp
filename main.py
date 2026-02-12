import ClientSocket
import time
from flask import Flask, render_template, request
import requests

HOST = "larc.furb.br"
PORT = 1012
logged_userId = 0
password = ""

#userId = 1943
#password = "dghol"

LAST_ACTION = ""


app = Flask(__name__, static_folder='static', static_url_path='/static')

client = ClientSocket.ClientSocket(HOST, PORT)


def getName(result, userId):
    name = ''
    for seila in result:
        if seila[0] == userId:
            name = seila[1]
            break
    return name


def players_front(players, result):
    players_retz = []

    i = 0

    while i < len(players) - 1:
        name = ''
        for seila in result:
            print(seila[0])
            print(players[i])
            if seila[0] == players[i]:
                name = seila[1]
                break

        tuplezinha  = (name, players[i + 1])
        players_retz.append(tuplezinha)
        i += 2

    return players_retz


def render_car(game_action, processed_card):
    if game_action == "ENTER" or game_action == "STOP" or game_action == "QUIT":
        client.send_message_game(game_action)
    elif game_action == "PEGAR":
        processed_card = process_card(client.get_card())
    return processed_card



def process_card(card):
    return card.replace(":","")


@app.route('/')
def login():
    user = request.args.get("logged_in_username")
    password = request.args.get("logged_in_passwrod")


    if user is not None and password is not None:
        logged_userId = user
        password = password
        client.log_in(logged_userId, password)
        time.sleep(6)
        return get_all_posts()

    

    return render_template("login.html")




@app.route('/whatsapp')
def get_all_posts():
    user = request.args.get("user")
    userId = request.args.get("userId")
    logged_in = client.get_score().split(':')
    last_card = request.args.get("card")
    game_action = request.args.get("action")
    result = []
    sent_message = request.args.get("sent_message")

    received_messagez = client.get_messages().split(":")

    i = 0
    while i < len(logged_in) - 1:
        tuplezinha  = (logged_in[i], logged_in[i + 1])
        result.append(tuplezinha)
        i += 3

    result.append((0, "Todos"))

    received_message = (getName( result,received_messagez[0]), received_messagez[1])

    players = client.get_players().split(":")

    players_ret = players_front(players, result)

    

    card = render_car(game_action, last_card)

    return render_template("index.html", logged_users=result, message_user=user, message_userId=userId, sent_message=sent_message, received_message=received_message, players=players_ret, card=card)


@app.route('/whatsapp')
def sendMessage():
    user = request.args.get("user")
    userId = request.args.get("userId")
    game_action = request.args.get("action")
    last_card = request.args.get("card")
    logged_in = client.get_score().split(':')
    result = []
    sent_message = request.args.get("sent_message")

    if sent_message is not None and sent_message != "":
        client.send_message(userId, sent_message)

    received_messagez = client.get_messages().split(":")
    received_message = (getName(received_messagez[0]), received_messagez[1])

    i = 0
    while i < len(logged_in) - 1:
        tuplezinha  = (logged_in[i], logged_in[i + 1])
        result.append(tuplezinha)
        i += 3

    result.append((0, "Todos"))

    players = client.get_players().split(":")

    players_ret = players_front(players, result)

    card = render_car(game_action, last_card)

    return render_template("index.html", logged_users=result, message_user=user, message_userId=userId, sent_message=sent_message, received_message=received_message, players=players_ret, card=card)
        


if __name__ == "__main__":
    app.run(debug=True, port=5001)