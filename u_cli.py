import mpv
import time

for i in range(20):
    playerID = mpv.MPV(ytdl=True)
    newplayerID = mpv.MPV(ytdl=True)

    playerID.play("https://youtu.be/Is3icfcbmbs")
    time.sleep(0.5)
    newplayerID.play("https://youtu.be/_vBVGjFdwk4")
    
playerID.wait_for_playback()



