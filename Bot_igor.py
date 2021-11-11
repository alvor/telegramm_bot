from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="1905808928:AAFx1uBKo20mvO_ji052zD418ovSTxxWy30")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "сам ты "+message.text
    send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(send_message.to_python())

executor.start_polling(dp)
