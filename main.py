from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import random
import asyncio


# Константы
me = 1089665132
admins = [me]


# Бот
TOKEN = '5621100860:AAEpqQg6QnN07YQ_MjPlD7vyDxB3q1vS4WU'
bot = Bot(token=TOKEN)
bot_dp = Dispatcher(bot=bot)


# Клавиатура админа
button_yes_ad = KeyboardButton('Да')
button_no_ad = KeyboardButton('Нет')
admin_kb = ReplyKeyboardMarkup()
admin_kb.add(button_yes_ad).add(button_no_ad)


# Клавиатура пользователя
# button_yes = KeyboardButton('Да')
button_spam = KeyboardButton('💣SPAM💣')
user_kb = ReplyKeyboardMarkup()
user_kb.add(button_spam)


# keyboards.py
inline_kb1 = InlineKeyboardMarkup()
inline_btn_1 = InlineKeyboardButton('💣SPAM💣', callback_data='spam')
inline_kb1.add(inline_btn_1)


@bot_dp.callback_query_handler(text='spam')
async def process_callback_button1(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    await bot.send_message(callback.from_user.id, 'DDOS of your ass')


@bot_dp.message_handler(commands=['start'])
async def start_message(message):
    if message.from_user.id in admins:
        await bot.send_message(me, 'Вы супер-пользователь', reply_markup=admin_kb)
    else:
        await bot.send_message(message.from_user.id, 'You are user', reply_markup=inline_kb1)


@bot_dp.message_handler(content_types=['text'])
async def get_text_messages(message):

    # ADMINS

    if message.from_user.id in admins:
        await bot.send_message(me, f'{message.from_user.id}', reply_markup=inline_kb1)
        ''' ^ Здесь в будущем нужно поменять на админскую клавиатуру сейчас это чисто тест ^ '''

    # USERS

    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.id}', reply_markup=inline_kb1)


@bot_dp.message_handler(content_types=["photo"])
async def photo(message):
    idphoto = message.photo[0].file_id
    await bot.send_photo(me, idphoto, f'ID пользователя: {message.from_user.id}')


if __name__ == '__main__':
    executor.start_polling(bot_dp)