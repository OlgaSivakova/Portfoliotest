import telebot as p
import wikipedia
wikipedia.set_lang('ru')

bot = p.TeleBot('6014014781:AAHxcPLpkigJJ6CQc8L--VRB2iXdo9_Gk8I')

@bot.message_handler(commands=['start'])#команда с которой нужно начинать
def welcom(message):
    bot.send_message(message.chat.id, 'Давай пообщаемся!')
    
@bot.message_handler(content_types=['text'])#значение которое будем принимать
def talk(message):
    if message.text=='Привет':
        bot.send_message(message.chat.id, 'И тебе привет')
    elif message.text=='Получить информацию':
        bot.send_message(message.chat.id, 'Введите название запроса')
    else:
        mes = message.text
        mew = mes.replace(' ', '_')
        page = wikipedia.page(mes)
        bot.send_message(message.chat.id, page.summary)
    
bot.polling(none_stop=True)


'''bot.send_message(message.chat.id, message.text) #отправляем то, что присылаем'''