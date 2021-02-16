from gtts import gTTS # pip install gtts
from playsound import playsound # pip install playsound

audio = 'track.mp3'
language = 'ru'
sp = gTTS(text="Сюда вписывайте текст который будет конвертироваться", lang=language, slow=False)
sp.save(audio)
playsound(audio)