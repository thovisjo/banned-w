from pygame import *



mixer.init()
mixer.music.load('425255__eardeer__howtowintheloundnesswars.ogg')
mixer.music.play()





















while mixer.music.get_busy():
        time.Clock().tick(10)  
