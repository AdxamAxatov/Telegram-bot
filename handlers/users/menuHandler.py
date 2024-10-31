import logging
from aiogram import types
from aiogram.types import Message, CallbackQuery, InputFile, ReplyKeyboardRemove
from keyboards.inline.staffKeyboard import staff_key, otajon_tech, xusan_tech, xurshid_tech, otabek_tech, miraziz_tech, rustam_tech
from keyboards.inline.menuKeyboard import menu_key, first_menu
from keyboards.inline.coursesKeyboard import course_key, course_back
from keyboards.inline.backKeyboard import back_key, about_back_key
from keyboards.default.requestdata import request_vacan_data, request_contact_data, course_contact_data

from loader import dp
# photo AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE
# video BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

@dp.callback_query_handler(text="en")
async def show_staff(call: CallbackQuery):
    # photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"
    await call.message.answer_photo(photo=photo_id, caption="Check our academy.", reply_markup=menu_key)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="menu")
async def show_staff(call: CallbackQuery):
    # photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"
    await call.message.answer_photo(photo=photo_id, caption="Check our academy.", reply_markup=menu_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="staf")
async def show_staff(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="Check our teachers.", reply_markup=staff_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="courses")
async def show_staff(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="Check our courses.", reply_markup=course_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="about")
async def show_staff(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=about_back_key)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="otajon")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=otajon_tech)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="rustam")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Rustam.\n\n"   
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=rustam_tech)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="xusan")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Xusan.\n\n"   
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=xusan_tech)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="otabek")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Otabek.\n\n"   
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=otabek_tech)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="xurshid")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Xurshid.\n\n"   
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=xurshid_tech)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="miraziz")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Miraziz.\n\n"   
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=miraziz_tech)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="front")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Our frontend development course is designed to equip you with the essential skills to build interactive and visually appealing websites.\n"
    msg += "You'll learn how to transform designs into functional web pages using HTML, CSS, and JavaScript."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=course_back)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="backend")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Our backend development course will teach you the essential skills to build the server-side logic and infrastructure of web applications. \n"
    msg += "You'll learn how to handle data, manage databases, and create robust APIs."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=course_back)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="cyber")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Our backend development course will teach you the essential skills to build the server-side logic and infrastructure of web applications. \n"
    msg += "You'll learn how to handle data, manage databases, and create robust APIs."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=course_back)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="designer")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Our backend development course will teach you the essential skills to build the server-side logic and infrastructure of web applications. \n"
    msg += "You'll learn how to handle data, manage databases, and create robust APIs."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=course_back)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="back")
async def back(call: CallbackQuery):
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    await call.message.answer_photo(photo=photo_id, caption="Check our academy.", reply_markup=menu_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="special_back")
async def back(call: CallbackQuery):
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    msg = f"Assalam Aleykum {call.message.from_user.full_name}\n"
    msg += "Welcome to our IT academy bot\n"
    msg += "Changing the language of the bot can be done by /language command.\n"
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=first_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="teacher_back")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="Check our teachers.", reply_markup=staff_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="course_back")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="Check our courses.", reply_markup=course_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="vacan")
async def back(call: CallbackQuery):
    await call.message.answer("We need some of your personal data,\nPlease click the button below for more.", reply_markup=request_vacan_data)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="contact")
async def back(call: CallbackQuery):
    await call.message.answer("We need some of your personal data,\nPlease click the button below for more.", reply_markup=request_contact_data)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="apply")
async def back(call: CallbackQuery):
    await call.message.answer("We need some of your personal data,\nPlease click the button below for more.", reply_markup=course_contact_data)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.message_handler(text="Cancel")
async def remove(message: Message):
    await message.answer("Operation cancelled", reply_markup=ReplyKeyboardRemove())
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    await message.answer_photo(photo=photo_id,  caption="Check our academy.", reply_markup=menu_key)


