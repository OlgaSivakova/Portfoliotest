from aiogram import Bot, Dispatcher, types
from aiogram import executor


bot = Bot('6666279021:AAHu-fWCGmE-L1_vNicn6uGliSMCe_ILhxs')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    #await bot.send_message(message.chat_id, 'Hello')
    
    mp = types.InlineKeyboardMarkup()
    mp.add(types.InlineKeyboardButton('Say welcome', callback_data= 'hello'))
    await message.answer('Hello', reply_markup=mp)
@dp.callback_query_handler()
async def callback(call):
    await call.message.answer('Welcome')
    

#bot.polling(none_stop=True) in pytelegram

executor.start_polling(dp)