from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
import asyncio


# Константы
me = 1089665132


# Бот
TOKEN = ''
bot = Bot(token=Token)
bot_dp = Dispatcher(bot=bot)


# Клавиатура админа
button_yes_ad = KeyboardButton('Да')
button_no_ad = KeyboardButton('Нет')
admin_kb = ReplyKeyboardMarkup()
admin_kb.add(button_yes_ad).add(button_no_ad)


# Клавиатура пользователя
button_yes = KeyboardButton('Да')
button_no = KeyboardButton('Нет')
user_kb = ReplyKeyboardMarkup()
user_kb.add(button_yes).add(button_no)


@bot_dp.message_handler(commands=['start'])
async def start_message(message):
    pass


@bot_dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    pass


@bot_dp.message_handler(content_types=["photo"])
async def photo(message):
    idphoto = message.photo[0].file_id
    await bot.send_photo(me, idphoto, f'ID пользователя: {message.from_user.id}')


if __name__ == '__main__':
    executor.start_polling(bot_dp)