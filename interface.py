import playlist
import downloader
import discordint
import os
from tkinter import *
from pygame import mixer

# constants
CONTROLBOARDCOLOR = "#50CB93"
BACKGROUNDCOLOR = "#71EFA3"
SEARCHBOARDCOLOR = "#ACFFAD"
LISTBOARDCOLOR= "#A2DBFA"

root = Tk()
mixer.init()
root.title("OpenBeats!")
# root.geometry("600x100")
root.config(bg = CONTROLBOARDCOLOR)
musicplaying = False




list_of_songs = os.listdir('songs/')
index_of_song = 0



print(list_of_songs)
print(list_of_songs[index_of_song])


mixer.music.load("songs/"+ list_of_songs[index_of_song])
mixer.music.play(loops=0)
mixer.music.pause()

# board list
searchbarboard = Frame(root, bg = SEARCHBOARDCOLOR, borderwidth=2)
searchbarboard.grid(row = 0, column =0)

musicnameboard = Frame(root, bg = BACKGROUNDCOLOR, borderwidth=6)
musicnameboard.grid(row = 1, column =0)

listboard= Frame(root, bg = LISTBOARDCOLOR, borderwidth=2)
listboard.grid(row = 0, column =1, rowspan=10)

favlistboard= Frame(root, bg = LISTBOARDCOLOR, borderwidth=2)
favlistboard.grid(row = 0, column =2, rowspan=10)


controlboard = Frame(root, bg = CONTROLBOARDCOLOR, borderwidth=2)
controlboard.grid(row = 2, column =0)



songname = Label(musicnameboard,text = str(list_of_songs[index_of_song])[0:45], bg = BACKGROUNDCOLOR)


def changesongname(name):
    songname.config(text = name[0:45])

def addfav():
    pass

def playmusic():
    global index_of_song
    nameofsong = list_of_songs[index_of_song]
    changesongname(nameofsong)
    mixer.music.load("songs/"+ list_of_songs[index_of_song])
    mixer.music.play(loops=0)
    discordint.discordpresenceupdate(list_of_songs[index_of_song])

def volumecontrol(temp):
    try:
        mixer.music.set_volume(volumeslider.get()/100)
    except:
        pass

def refreshmusiclist():
    global listlabel
    global list_of_songs
    list_of_songs = os.listdir('songs/')
    listlabel = Label(listboard, text = "\n".join(list_of_songs), bg = LISTBOARDCOLOR).grid(row = 0, column = 0)
    print("List refreshed")
    

def leftbuttonpressed():
    global index_of_song
    try:
        index_of_song -=1
        print(index_of_song)
        playmusic()
    except:
        index_of_song =0
        print(index_of_song)
        playmusic()
        

def pausemusic():
    global musicplaying
    if not(musicplaying):
        print("playing music")
        musicplaying = True
        mixer.music.unpause()
    else:
        mixer.music.pause()
        musicplaying = False
        print("Music paused")

def rightbuttonpressed():
    global index_of_song
    try:
        index_of_song +=1
        print(index_of_song)
        playmusic()
    except:
        index_of_song =0
        print(index_of_song)
        playmusic()
        

searchbar_row = 0
musicname_row = 1
musicbar_row = 2

# frames


search_entry = Entry(searchbarboard,width = 31)

def searchforsong():
    url = search_entry.get()
    search_entry.delete(0, 'end')
    downloader.download(url)


search_entry.grid(row = searchbar_row, column =0, columnspan = 4)
search_button = Button(searchbarboard,text = "🔍", command = searchforsong).grid(row = searchbar_row, column = 5)

songname.grid(row = musicname_row, column = 0, columnspan = 10)
addfavbutton = Button()

listlabel = Label(listboard, text = "\n".join(list_of_songs), bg = LISTBOARDCOLOR).grid(row = 0, column = 0)
favlistlabel = Label(favlistboard, text = "\n".join(playlist.readfav()), bg = LISTBOARDCOLOR).grid(row = 0, column = 0)

Button(controlboard,text = "🗘", command=refreshmusiclist).grid(row = musicbar_row, column =0)
Button(controlboard,text = "<", command=leftbuttonpressed).grid(row = musicbar_row, column =1)
Button(controlboard,text = "||", command=pausemusic).grid(row = musicbar_row, column =2)
Button(controlboard,text = ">", command=rightbuttonpressed).grid(row = musicbar_row, column =3)

volumeslider = Scale(controlboard, from_=0, to=100, borderwidth=0, bg = CONTROLBOARDCOLOR, orient=HORIZONTAL, command=volumecontrol)
volumeslider.grid(row = musicbar_row, column =4)
volumeslider.set(50)

discordint.discordpresenceupdate(list_of_songs[index_of_song])

root.mainloop()
