import FreeSimpleGUI as sg


def who_wins(window):

    message_player1 = "Player 1 (X)"
    message_player2 = "Player 2 (O)"

    player1_map = []  # Mapa para el jugador 1 (X)
    player2_map = []  # Mapa para el jugador 2 (O)

    for i in range(1, 10):
        button = window.Element(f"-{i}-")
        if button.ButtonText == "X":
            player1_map.append("X")
            player2_map.append(" ")
        elif button.ButtonText == "O":
            player1_map.append(" ")
            player2_map.append("O")
        else:
            player1_map.append(" ")
            player2_map.append(" ")

    if winning_combinations(player1_map):
        return message_player1
    elif winning_combinations(player2_map):
        return message_player2
    else:
        return None


def winning_combinations(player_map):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for combination in winning_combinations:
        if player_map[combination[0]] == player_map[combination[1]] == player_map[combination[2]] != " ":
            return True
    return False


def main():

    BUTTON_SIZE = (7, 3)

    PLAYER_ONE = "X"
    PLAYER_TWO = "O"

    current_player = PLAYER_ONE
    win_player = None

    #Layout definition
    layout = [
        [
            #First row
            sg.Button("", key="-1-", size=BUTTON_SIZE),
            sg.Button("", key="-2-", size=BUTTON_SIZE),
            sg.Button("", key="-3-", size=BUTTON_SIZE)
        ],
        [
            #Second row
            sg.Button("", key="-4-", size=BUTTON_SIZE),
            sg.Button("", key="-5-", size=BUTTON_SIZE),
            sg.Button("", key="-6-", size=BUTTON_SIZE)
        ],
        [
            #Third row
            sg.Button("", key="-7-", size=BUTTON_SIZE),
            sg.Button("", key="-8-", size=BUTTON_SIZE),
            sg.Button("", key="-9-", size=BUTTON_SIZE)
        ],
        [
            sg.Text("", key="-WINNER-")
        ],
        [
            sg.Button("Cerrar", key="-Cerrar-")
        ]
    ]

    window = sg.Window("Tic-Tac-Toe", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "-Cerrar-":
            break

        if window.Element(event).ButtonText == "":
            window.Element(event).Update(text=current_player)
            if current_player == PLAYER_ONE:
                current_player = PLAYER_TWO
            else:
                current_player = PLAYER_ONE

        #Let's see who wins
        win_player = who_wins(window)
        if win_player:
            print(win_player)
            break

    window.Element("-WINNER-").update("{} won the game!".format(win_player))
    event, values = window.read()
    window.close()


if __name__ == "__main__":
    main()