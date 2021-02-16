from pygame import mixer # pip install pygame

mixer.init() # Запустить mixer и в случае ошибки,
# запустить через терминал или сминить conf


mixer.music.load('song.mp3') # вписываете трек который хотите послушать, если выдаст ошибку при чтении,
# следует сменить формат файла

mixer.music.set_volume(0.7) # Тут настраивается громкость
mixer.music.play() # Плей

while True:
    print("Нажмите на 'p' для паузы")
    print("Нажмите на 'r' чтобы продолжить прослушывание")
    print("Нажмите на 'q' для выхода из программы")
    query = input(">>>")

    if query == 'p':
        mixer.music.pause() 
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'q':
        mixer.music.stop()
        break