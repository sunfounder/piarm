from robot_hat import Music,TTS
from time import sleep

m = Music()
t = TTS()

def sound():
    song = '../../Sound/Emergency_Alarm.wav'
    m.music_set_volume(40)
    print('Music duration',m.sound_length(song))
    m.sound_play(song)

def background_music():
    music = '../../Music/peace.mp3'	
    m.music_set_volume(50)
    m.background_music(music)	

def tts():
    t.say("timing begins")
    sleep(1)
    t.say("three")
    sleep(1)
    t.say("two")
    sleep(1)
    t.say("one")
    sleep(1)
    t.say("Stop music")
    sleep(1)
	
if __name__ == "__main__":
    background_music()
    sleep(10)	
    #sound()
    #tts()
    while True:
        #background_music()
        sound()
        tts()		
