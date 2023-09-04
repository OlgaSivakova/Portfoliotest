from moviepy.editor import*
from pathlib import Path
whattodo = ''
def inputvideotocreate(nameoffile):
     vidsec = f'{nameoffile}.mp4'
     path1=Path(vidsec)
     return(path1)
dictoptions = {0: 'Выход из программы', 1: 'Склеить два видео',2: 'Извлечь музыку из видео', 3 : 'Обрезать видео', 4 : 'Преобразовать видео в gif'}
whattododict = int(input(f'Выберите действие из списка {dictoptions.keys()}'))
whattodo = dictoptions[whattododict]
while whattodo!='Выход из программы':
    

    if whattodo =='Склеить два видео':
            firstvideo = input('Введите название первого видео!')
            secondvideo = input('Введите название второго видео!')
            
            path1=inputvideotocreate(firstvideo)
            path2=inputvideotocreate(secondvideo)
            video = VideoFileClip(f'{path1}')
            
            video2 = VideoFileClip(f'{path2}')
            got = concatenate_videoclips([video, video2])
            got.write_videofile('Final.mp4')
    elif whattodo=='Извлечь музыку из видео':
            k=input('Введите название первого видео для извлечения музыки!')
            path_video = inputvideotocreate(k)
            video = VideoFileClip(f'{path_video}')
            audio = video.audio
            audio.write_audiofile(f'{path_video.stem}.mp3')
    elif whattodo=='Обрезать видео':
            firstvidsec= input('Введите название видео, которое хотите обрезать!')
            pathfrondef= inputvideotocreate(firstvidsec)
            firstsec= int(input('С какой секунды должна начинаться видеозапись?'))
            secondsec = int(input('Какой секундой должна заканчивтаься видеозапись?'))
            
            video = VideoFileClip(f'{pathfrondef}')
            cutvideo = video.subclip(firstsec, secondsec)

            cutvideo.write_videofile('Finalcut.mp4')
    elif whattodo=='Преобразовать видео в gif':
            firstvidgif= input('Введите название видео, которое хотите обрезать!')
            pathfrondef2= inputvideotocreate(firstvidgif)
            firstsectogif= int(input('С какой секунды должна начинаться видеозапись?'))
            secondsectogif = int(input('Какой секундой должна заканчивтаься видеозапись?'))
            
            video = (VideoFileClip(f'{pathfrondef2}').subclip(firstsectogif,secondsectogif))
            video.write_gif('Finalgif.gif')
                    
    elif whattodo=='Выход из программы':
            break
        