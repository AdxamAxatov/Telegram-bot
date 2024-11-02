import logging
from aiogram import types
from keyboards.inline.backinlineKeyboard import back_keyboard
from keyboards.inline.inlineKeyboards import menu_start, links_keyboard
from keyboards.inline.resumeKeyboard import resume_keyboard

from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id, )


@dp.callback_query_handler(text="bio")
async def send_bio(call: types.CallbackQuery):
    logging.info(call)
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.full_name=}")
    users = {call.from_user.id:call.from_user.username}
    photo_id = "AgACAgIAAxkBAAMzZwyO9a7dDB-cJwLh30yavfPsKK0AAnPxMRtTPGlIWd7gOZXrjocBAAMCAAN4AAM2BA"
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Otajon Bozorboyev.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    await call.message.delete()
    await call.message.answer_photo(photo_id, caption=msg, reply_markup=back_keyboard )
    await call.answer(cache_time=60)
    

@dp.callback_query_handler(text="resume")
async def send_resume(call: types.CallbackQuery):
    logging.info(call)
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.full_name=}")
    users = {call.from_user.id:call.from_user.username}
    ph_id = "AgACAgIAAxkBAAMzZwyO9a7dDB-cJwLh30yavfPsKK0AAnPxMRtTPGlIWd7gOZXrjocBAAMCAAN4AAM2BA"
    dscrpt = 'click the button below to download'
    await call.message.delete()
    await call.message.answer_photo(ph_id, caption=dscrpt, reply_markup=resume_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="to_menu")
async def send_menu(call: types.CallbackQuery):
    logging.info(call)
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.full_name=}")
    users = {call.from_user.id:call.from_user.username}
    ph_id = "AgACAgIAAxkBAAMzZwyO9a7dDB-cJwLh30yavfPsKK0AAnPxMRtTPGlIWd7gOZXrjocBAAMCAAN4AAM2BA"
    dsrpt = "Main page"
    await call.message.delete()
    await call.message.answer_photo(ph_id, caption=dsrpt, reply_markup=menu_start)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="link")
async def send_link(call: types.CallbackQuery):
    logging.info(call)
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.full_name=}")
    users = {call.from_user.id:call.from_user.username}
    ph_id = "AgACAgIAAxkBAAMzZwyO9a7dDB-cJwLh30yavfPsKK0AAnPxMRtTPGlIWd7gOZXrjocBAAMCAAN4AAM2BA"
    cap = "Click the buttons below to open"
    await call.message.delete()
    await call.message.answer_photo(ph_id, caption=cap, reply_markup=links_keyboard)
    await call.answer(cache_time=60)











































