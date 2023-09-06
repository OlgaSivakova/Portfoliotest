import telebot as p
import wikipedia
import pickle
import os
import webbrowser
from moviepy.editor import*
from pathlib import Path
from telebot import types
import sqlite3


whattodo = ''
def inputvideotocreate(nameoffile):
     vidsec = f'{nameoffile}.mp4'
     path1=Path(vidsec)
     return(path1)
dictoptions = ['0. Выход из программы 1.Склеить два видео 2.Извлечь музыку из видео 3.Обрезать видео 4.Преобразовать видео в gif']

                  
wikipedia.set_lang('ru')

bot = p.TeleBot('6014014781:AAHxcPLpkigJJ6CQc8L--VRB2iXdo9_Gk8I')
d ={'12.04': ['12:00','13:00','16:00'], '13.04': ['12:00','13:00','16:00'] }
nonemptyfile = 'my_dict.pkl'


#функция на дату и время
def book(dic, n ,m):

    if os.path.getsize(nonemptyfile)==0:

        if m in dic[n]:
                ind = dic[n].index(m)
                dic[n].pop(ind)
                dirs = {n : dic[n]}
                dic.update( dirs)

                
        elif m not in dic[n]:
            txt = f'Запись на это время невозможна. Пожалуйста, проверьте список доступного времени и повторите попытку'
            
            return  f'{txt}{dic[n]}'
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
        
        elif m not in ld[n]:
            txt = f'Запись на это время невозможна. Пожалуйста, проверьте список доступного времени и повторите попытку'
           
            return f'{txt} {ld[n]}'
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





#начало бота   
@bot.message_handler(content_types=['photo', 'video'])
def get_video(message):
    
    bot.reply_to(message, 'Данные получены')
  
name = ''    
@bot.message_handler(commands=['start'])#команда с которой нужно начинать
def sql(message):
    conn = sqlite3.connect('table.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), date varchar(15))')
    
    conn.commit()
    cur.close()
    conn.close()
    
    bot.send_message(message.chat.id, f'Укажите имя')
    bot.register_next_step_handler(message, user_name) #регистрация следующей функции позволяет непрерывно их выполнять
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, f'Укажите дату')
    bot.register_next_step_handler(message, date)
    
def date(message):
    date = message.text.strip()
    
    conn = sqlite3.connect('table.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, date) VALUES ("%s", "%s")' % (name, date))
    
    conn.commit()
    cur.close()
    conn.close()
    
    bot.send_message(message.chat.id, f'Данные получены')

"""@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data =='users':
        conn = sqlite3.connect('table.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall() #возвращение всех данных в перемнную
        info = ''
        for el in users:
            info += f'Имя: {el[1]}, Дата записи: {el[2]}\n'
    
        cur.close()
        conn.close()
        
        bot.send_message(call.message.chat.id, info)
    elif call.data =='conc':
         bot.send_message(call.message.chat.id, 'Введите название видео, из которого хотите извлечь музыку')"""
        


   
    
    
@bot.message_handler(commands=['menu'])#команда с которой нужно начинать    
def welcom(message):
    bt = types.InlineKeyboardMarkup()
    bt.add(types.InlineKeyboardButton('Больше на сайте', url='https://www.kufar.by/account/my_ads/published'))
    bt.add(types.InlineKeyboardButton('Соеденить видео', callback_data='conc'))
    bot.send_message(message.chat.id, f'Привет <u>{message.from_user.first_name}!</u> <b>Выберите действие из списка </b>',parse_mode='html', reply_markup= bt)

    
@bot.callback_query_handler(func=lambda callback: True) #функция для кнопки выше
def callback_message(callback):
    if callback.data =='conc':
         bot.send_message(callback.message.chat.id, 'Введите название видео, из которого хотите извлечь музыку')
         
@bot.message_handler(commands=['site'])#команда с которой нужно начинать
def site(message):
   webbrowser.open('https://www.kufar.by/account/my_ads/published')

    
@bot.message_handler(content_types=['text'])#значение которое будем принимать
def talk(message):
    if message.text=='1':
        bot.send_message(message.chat.id, '<b><em>Введите название двух видео</em></b>', parse_mode='html')
    elif message.text == 'данные':
        conn = sqlite3.connect('table.sql')
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall() #возвращение всех данных в перемнную
        info = ''
        for el in users:
            info += f'Имя: {el[1]}, Дата записи: {el[2]}\n'
    
        cur.close()
        conn.close()
        
        bot.send_message(message.chat.id, info)
        
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
    elif message.text=='2':
        bot.send_message(message.chat.id, 'Введите название видео, из которого хотите извлечь музыку')
    elif 'В музыку:' in message.text:
            firstv = message.text.split(':')[1]
            path_video = inputvideotocreate(firstv)
            video = VideoFileClip(f'{path_video}')
            audio = video.audio
            audio.write_audiofile(f'{path_video.stem}.mp3')
            bot.send_message(message.chat.id, f'{path_video.stem}.mp3')
    elif message.text=='3':
        bot.send_message(message.chat.id, 'Введите название видео, и секунды начала и конца отрезка в формате НАЗВАНИЕ[1,5]')
    elif '[' in message.text:
           
            firstvidsec= message.text.split('[')[1]#
            firstvidsecc= message.text.split('[')[0]#имя
            firstvidse= message.text.split('[')[1]
            firstvids = (str(firstvidsec)).split(',')
            firstvid = int((str(firstvids[1])).split(']')[0]) #последняя
            firstvi = int((str(firstvids[0])))
           
            pathfrondef= inputvideotocreate(firstvidsecc)
            
            video = VideoFileClip(f'{pathfrondef}')
            cutvideo = video.subclip(firstvi, firstvid)
            cutvideo.write_videofile('Finalcut.mp4')
            bot.send_message(message.chat.id, 'Готово!')
    elif message.text == '4':
        bot.send_message(message.chat.id, 'Введите название видео после слова Преобразовать:')
    elif 'Преобразовать:' in message.text:
            newtxt = message.text.replace(':', ',').replace('(', ',').replace(',', ',').replace(')', '').replace(' ', '')
            name = newtxt.split(',')[1]
            fsec = int(newtxt.split(',')[2])
            ssec = int(newtxt.split(',')[3])
            
                        

            pathfrondef2= inputvideotocreate(name)
            
            
            video = VideoFileClip(f'{pathfrondef2}').subclip(fsec,ssec)
            video.write_gif('Finalgif.gif')
            
            
            bot.send_message(message.chat.id, 'Готово!')
            
    elif message.text=='Получить информацию':
        bot.send_message(message.chat.id, 'Введите название запроса')
    elif message.text=='Запись':
        bot.send_message(message.chat.id, 'Введите время и дату в формате ДД/ЧЧ')
    elif '.' in message.text and '/' in message.text and ':' in message.text and len(message.text)==11:
        a = message.text.split('/')[0]
        b = message.text.split('/')[1]
        user = str(book(d, a, b))

        bot.send_message(message.chat.id, user)
        
      
    else:
        mes = message.text
        mew = mes.replace(' ', '_')
        page = wikipedia.page(mes)
        bot.send_message(message.chat.id, page.summary)
    
bot.polling(none_stop=True)


'''bot.send_message(message.chat.id, message.text) #отправляем то, что присылаем'''