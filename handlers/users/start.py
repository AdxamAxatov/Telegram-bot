from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.menuKeyboard import first_menu
from aiogram.types import InputFile
from keyboards.inline.choose_lang import lang_key

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    msg = f"Assalam Aleykum {message.from_user.full_name}\n"
    msg += "Welcome to our IT academy bot\n"
    msg += "Changing the language of the bot can be done by /language command.\n"
    await message.answer_photo(photo=photo_id, caption=msg, reply_markup=first_menu)
  


@dp.message_handler(Command('language'))
async def bot_start(message: types.Message):
    await message.answer("Chosen language", reply_markup=lang_key)
 
    
