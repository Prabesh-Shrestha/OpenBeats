import os


def playlists():
    play = os.listdir("openbeats/playlist/")
    return play


def readfav(fav_file_name):
    fav_file_name = "openbeats/playlist/" + fav_file_name
    with open(fav_file_name, "r") as file:
        lines = file.read().split("\n")
    return lines


def createfav(fav_file_name, list_of_song):
    fav_file_name = "openbeats/playlist/" + fav_file_name
    with open(fav_file_name, "w") as file:
        file.write("\n".join(list_of_song))


def updatefav(listofsong):
    with open("openbeats/playlist/fav.txt", "a") as file:
        file.write("\n".join(listofsong))
        file.write("\n")


if __name__ == "__main__":
    # print(readfav())
    updatefav(["1", "2", "Cö shu Nie - Asphyxia.wav"])