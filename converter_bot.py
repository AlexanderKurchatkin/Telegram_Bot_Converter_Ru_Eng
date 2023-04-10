import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from transliterate import translit


logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(massege: types.Message):
    user_name = massege.from_user.full_name 
    user_id = massege.from_user.id
    text = f"Здравствуйте {user_name}, введите ФИО через пробел!"
    logging.info(f"{user_name=} {user_id=} sent massege: {massege.text} ") 
    await massege.reply(text)
 
@dp.message_handler()
async def send_echo(massege: types.Message):
    user_name = massege.from_user.full_name 
    user_id = massege.from_user.id
    input_rus_text = massege.text
    text = translit(input_rus_text, language_code='ru', reversed=True).upper()
    logging.info(f"{user_name=} {user_id=} sent massege: {text} ") 
    await bot.send_message(user_id, text)



if __name__ == '__main__':
    executor.start_polling(dp)