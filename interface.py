import playlist
import downloader
import discordint
import os
from tkinter import *
from pygame import mixer
from config import *

root = Tk()
mixer.init()
root.title("OpenBeats!")
# root.geometry("600x100")
root.config(bg = CONTROLBOARDCOLOR)
musicplaying = False
playlistSelected = False
index_of_song = 0
index_of_fav_song = 0

# creates the song lists
list_of_songs_fullname = os.listdir(MUSICFOLDER + '/')
list_of_fav_songs_fullname = playlist.readfav("fav.txt")
list_of_songs = [i[:numberoflettersinmusic] for i in list_of_songs_fullname]
list_of_fav_songs = [i[:numberoflettersinmusic] for i in list_of_fav_songs_fullname]



print(list_of_songs_fullname)
print(list_of_songs_fullname[index_of_song])


mixer.music.load(MUSICFOLDER + "/"+ list_of_songs_fullname[index_of_song])
mixer.music.play(loops=0)
mixer.music.pause()

# board list
searchbarboard = Frame(root, bg = SEARCHBOARDCOLOR, borderwidth=2)
searchbarboard.grid(row = 0, column =0)

musicnameboard = Frame(root, bg = BACKGROUNDCOLOR, borderwidth=6)
musicnameboard.grid(row = 1, column =0)

playlistboard= Frame(root, bg = LISTBOARDCOLOR, borderwidth=2)
playlistboard.grid(row = 0, column =1, rowspan=10)

listboard= Frame(root, bg = LISTBOARDCOLOR, borderwidth=2)
listboard.grid(row = 0, column =2, rowspan=10)


controlboard = Frame(root, bg = CONTROLBOARDCOLOR, borderwidth=2)
controlboard.grid(row = 2, column =0)



songname = Label(musicnameboard,text = str(list_of_songs[index_of_song])[0:45], bg = BACKGROUNDCOLOR)










# sb = Scrollbar(root)
# sb.grid(row = 0, column = 1)
  
# songlist = Listbox(listboard, yscrollcommand = sb.set).grid(row = 0, column = 0)  
# sb.config(command = songlist.yview)  

sb = Scrollbar(listboard)  
sb.pack(side = RIGHT, fill = Y)  
songlist = Listbox(listboard, yscrollcommand = sb.set )  
songlist.pack( side = LEFT )  
sb.config( command = songlist.yview )








def changesongname(name):
    songname.config(text = name[0:45])

def addfav():
    playlist.updatefav([list_of_songs_fullname[index_of_song]])
    # print(list_of_songs_fullname[index_of_song])
def playmusic():
    global index_of_song
    global list_of_fav_songs_fullname
    global list_of_fav_songs
    if playlistSelected:
        nameofsong = list_of_songs[index_of_song]
        changesongname(nameofsong)
        mixer.music.load(MUSICFOLDER + "/"+ list_of_fav_songs_fullname[index_of_fav_song])
        mixer.music.play(loops=0)
        discordint.discordpresenceupdate(list_of_fav_songs_fullname[index_of_fav_song])
    else:
        nameofsong = list_of_songs_fullname[index_of_song]
        changesongname(nameofsong)
        mixer.music.load(MUSICFOLDER + "/"+ list_of_songs_fullname[index_of_song])
        mixer.music.play(loops=0)
        discordint.discordpresenceupdate(list_of_songs_fullname[index_of_song])

def volumecontrol(temp):
    try:
        mixer.music.set_volume(volumeslider.get()/100)
    except:
        pass

def refreshmusiclist():

    global listlabel
    global list_of_fav_songs
    global list_of_songs
    global list_of_songs_fullname

    list_of_fav_songs_fullname = os.listdir(MUSICFOLDER + '/')
    list_of_fav_songs = [i[:numberoflettersinmusic] for i in list_of_fav_songs_fullname]
    
    list_of_songs_fullname = os.listdir(MUSICFOLDER + '/')
    list_of_songs = [i[:numberoflettersinmusic] for i in list_of_songs_fullname]
    if playlistSelected:
        songlist.delete(0, END)
        for i in list_of_fav_songs:
            songlist.insert(END,i)
        # songlist.insert(END,"\n".join(list_of_fav_songs))

    else:
        songlist.delete(0, END)
        for i in list_of_songs:
            songlist.insert(END,i)

        # listlabel = Label(listboard, text = "\n".join(list_of_songs), bg = LISTBOARDCOLOR).grid(row = 0, column = 0)
    print("List refreshed")
    

def leftbuttonpressed():
    global index_of_song
    if playlistSelected:
        try:
            index_of_song -=1
            print(index_of_song)
            playmusic()
        except:
            index_of_song =0
            print(index_of_song)
            playmusic()
        pass
    else:
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
        



def showallinlist():
    global listlabel
    try:
        songlist.delete(0, END)
        for i in list_of_songs:
            songlist.insert(END,i)
        print("favlist distroyed")
    except:
        pass
def showfavinlist():
    global favlistlabel
    try:
        songlist.delete(0, END)
        for i in list_of_fav_songs:
            songlist.insert(END,i)
    except:
        pass

search_entry = Entry(searchbarboard,width = 31)

def searchforsong():
    url = search_entry.get()
    search_entry.delete(0, 'end')
    downloader.download(url)


search_entry.grid(row = searchbar_row, column =0, columnspan = 4)
search_button = Button(searchbarboard,text = "🔍", command = searchforsong).grid(row = searchbar_row, column = 5)

songname.grid(row = musicname_row, column = 0, columnspan = 10)


Button(playlistboard, text = "All", padx = 30, pady = 5, command = showallinlist).grid(row =0, column = 0)
Button(playlistboard, text = "Favourite", command = showfavinlist).grid(row =1, column = 0)

Button(controlboard,text = "🗘", command=refreshmusiclist).grid(row = musicbar_row, column =0)
Button(controlboard,text = "<", command=leftbuttonpressed).grid(row = musicbar_row, column =1)
Button(controlboard,text = "||", command=pausemusic).grid(row = musicbar_row, column =2)
Button(controlboard,text = ">", command=rightbuttonpressed).grid(row = musicbar_row, column =3)
Button(controlboard,text = "+", command=addfav).grid(row = musicbar_row, column =4)

volumeslider = Scale(controlboard, from_=0, to=100, borderwidth=0, bg = CONTROLBOARDCOLOR, orient=HORIZONTAL, command=volumecontrol)
volumeslider.grid(row = musicbar_row, column =5)
volumeslider.set(50)

discordint.discordpresenceupdate(list_of_songs_fullname[index_of_song])

root.mainloop()
