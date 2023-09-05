import telebot as p
import wikipedia
import pickle
import os
from moviepy.editor import*
from pathlib import Path
whattodo = ''
def inputvideotocreate(nameoffile):
     vidsec = f'{nameoffile}.mp4'
     path1=Path(vidsec)
     return(path1)
dictoptions = {0: 'Выход из программы', 1: 'Склеить два видео',2: 'Извлечь музыку из видео', 3 : 'Обрезать видео', 4 : 'Преобразовать видео в gif'}

    
        
wikipedia.set_lang('ru')

bot = p.TeleBot('6014014781:AAHxcPLpkigJJ6CQc8L--VRB2iXdo9_Gk8I')
d ={'12.04': ['12:00','13:00','16:00'], '13.04': ['12:00','13:00','16:00'] }
nonemptyfile = 'my_dict.pkl'

def book(dic, n ,m):

    if os.path.getsize(nonemptyfile)==0:

        if m in dic[n]:
                ind = dic[n].index(m)
                dic[n].pop(ind)
                dirs = {n : dic[n]}
                dic.update( dirs)

        with open('my_dict.pkl', 'wb') as f:
            pickle.dump(dic, f)
        return dic
    elif os.path.getsize(nonemptyfile)!=0:
        with open('my_dict.pkl', 'rb') as f:
            ld = pickle.load(f)
       

        if m in ld[n]:
                ind = ld[n].index(m)
                ld[n].pop(ind)
                dirs = {n : ld[n]}
                ld.update( dirs)
        with open('my_dict.pkl', 'wb') as f:
            pickle.dump(ld, f)
        return ld  
#if os.path.getsize(nonemptyfile)==0:#
#            a = str(input(f'Выберите дату из свежего списка{d.keys()}'))
#            b = str(input(f'Выберите время из свежего списка{d[a]}'))
 #           d = d
#if os.path.getsize(nonemptyfile)!=0:
#            with open('my_dict.pkl', 'rb') as f:
#                    ld = pickle.load(f)
#            a = str(input(f'Выберите дату из использованного списка{ld.keys()}'))
#            b = str(input(f'Выберите время из использованного списка{ld[a]}'))
#            user = str(book(d, a, b))



@bot.message_handler(commands=['start'])#команда с которой нужно начинать
def welcom(message):
    bot.send_message(message.chat.id, f'Выберите действие из списка {dictoptions.keys()}')
    
@bot.message_handler(content_types=['text'])#значение которое будем принимать
def talk(message):
    if message.text=='1':
        bot.send_message(message.chat.id, 'Введите название двух видео')
    elif '|' in message.text:
        firstvideo = message.text.split('|')[0]
        secondvideo = message.text.split('|')[1]
        path1=inputvideotocreate(firstvideo)
        path2=inputvideotocreate(secondvideo)
        video = VideoFileClip(f'{path1}')
            
        video2 = VideoFileClip(f'{path2}')
        got = concatenate_videoclips([video, video2])
        got.write_videofile('Final.mp4')
        bot.send_message(message.chat.id, 'Final.mp4')
    elif message.text=='Получить информацию':
        bot.send_message(message.chat.id, 'Введите название запроса')
    elif message.text=='Запись':
        bot.send_message(message.chat.id, a)
    elif '.' in message.text and '/' in message.text and ':' in message.text and len(message.text)==11:
        a = message.text.split('/')[0]
        b = message.text.split('/')[1]
        user = str(book(d, a, b))

        bot.send_message(message.chat.id,  user )
        
      
    else:
        mes = message.text
        mew = mes.replace(' ', '_')
        page = wikipedia.page(mes)
        bot.send_message(message.chat.id, page.summary)
    
bot.polling(none_stop=True)


'''bot.send_message(message.chat.id, message.text) #отправляем то, что присылаем'''