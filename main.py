import logging
import wikipediaapi
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

API_TOKEN = '7470262322:AAGHWfG927aQ9HJtlqCJomdX6tysmP_nD-I'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('uz')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men Wikipedia Botiman.\nMenga istalgan mavzuni yuboring va men siz uchun Wikipediadan ma'lumot topib beraman.")

@dp.message_handler(content_types=ContentType.TEXT)
async def fetch_wikipedia(message: types.Message):
    search_term = message.text
    await types.ChatActions.typing()  # Send "typing..." action
    page = wiki_wiki.page(search_term)
    
    if page.exists():
        response = f"Sarlavha: {page.title}\n\nQisqacha: {page.summary[0:1000]}...\n\nBatafsil o'qing: {page.fullurl}"
    else:
        response = "Kechirasiz, bu mavzu bo'yicha hech qanday ma'lumot topa olmadim."

    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
