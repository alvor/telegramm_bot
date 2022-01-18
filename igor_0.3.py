from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot
from BotConfig import BotToken as bt
import cv2

bot = Bot(token=bt)
dp = Dispatcher(bot)

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    file_info = await bot.get_file(message.photo[-1].file_id)
    await message.photo[-1].download()

