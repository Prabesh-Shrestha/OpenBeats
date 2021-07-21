fav_file_name = 'fav.txt'

def readfav():
    with open(fav_file_name, 'r') as file:
        lines = file.read().split('\n')
    return lines

def createfav(list_of_song):
    with open(fav_file_name, 'w') as file:
        file.write('\n'.join(list_of_song))


def updatefav(listofsong):
    oldsongs = readfav()
    newsongs = list(set(listofsong) - set(oldsongs))
    fulllist = oldsongs + newsongs
    createfav(fulllist)

if __name__ == '__main__':
    # print(readfav())      
    updatefav(["1","2","Cö shu Nie - Asphyxia.wav"])





