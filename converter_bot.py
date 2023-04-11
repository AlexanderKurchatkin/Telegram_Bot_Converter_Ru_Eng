import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from transliterate import translit


logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

alph_RU_ENG = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'ie','ы':'y','ь':'','э':'e',
      'ю':'iu','я':'ia', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'KH',
      'Ц':'TS','Ч':'CH','Ш':'SH','Щ':'SHCH','Ъ':'','Ы':'Y','Ь':'','Э':'E',
      'Ю':'IU','Я':'IA',',':'','?':'',' ':' ','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}

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
    text = massege.text
    for key in alph_RU_ENG:
        text = text.replace(key, alph_RU_ENG[key]).upper()
    logging.info(f"{user_name=} {user_id=} sent massege: {text} ") 
    await bot.send_message(user_id, text)



if __name__ == '__main__':
    executor.start_polling(dp)
