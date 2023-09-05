import telebot as p
import wikipedia
import pickle
import os
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




@bot.message_handler(commands=['start'])#команда с которой нужно начинать
def welcom(message):
    bot.send_message(message.chat.id, 'Давай пообщаемся!')
    
@bot.message_handler(content_types=['text'])#значение которое будем принимать
def talk(message):
    if message.text=='Привет':
        bot.send_message(message.chat.id, 'И тебе привет')
    elif message.text=='Получить информацию':
        bot.send_message(message.chat.id, 'Введите название запроса')
    elif message.text=='Запись':
        bot.send_message(message.chat.id, a)
    elif message.text=='13.04/16:00':
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