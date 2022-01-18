from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot
from BotConfig import BotToken as bt
import cv2
import numpy as np

bot = Bot(token=bt)
dp = Dispatcher(bot)


@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    file_info = await bot.get_file(message.photo[-1].file_id)
    await message.photo[-1].download(file_info.file_path.split('photos/')[1])  # ++
    print(file_info)
    chat_id = message.chat.id
    text = "Фото сохранено на сервере"

    await bot.send_message(chat_id=chat_id, text=text)
    img = cv2.imread(message.photo)

    n_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    n_img = cv2.GaussianBlur(n_img, (5, 5), 3)
    n_img = cv2.cvtColor(n_img, cv2.COLOR_BGR2GRAY)

    n_img = cv2.Canny(n_img, 30, 30)

    kernel = np.ones((3, 3), np.uint8)
    n_img = cv2.dilate(n_img, kernel, iterations=1)
    await bot.send_photo(chat_id=chat_id, photo=n_img)

if __name__ == '__main__':
    executor.start_polling(dp)
