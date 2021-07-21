from pypresence import Presence
import time

client_id = "865184394544152586"
rpc = Presence(client_id)
rpc.connect()

def discordpresenceupdate(songname):
    rpc.update(state = "playing : " + songname,large_image = "pfp",start = time.time())