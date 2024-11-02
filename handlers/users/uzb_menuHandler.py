import logging
from aiogram import types
from aiogram.types import Message, CallbackQuery, InputFile, ReplyKeyboardRemove
from keyboards.inline.staffKeyboard import oqituvchi_key, otajon_tech, xusan_tech, xurshid_tech, otabek_tech, miraziz_tech, rustam_tech
from keyboards.inline.menuKeyboard import bosh_bolim_key, birinchi_menu
from keyboards.inline.coursesKeyboard import kurs_key, kurs_ortga
from keyboards.inline.backKeyboard import ortga_key, haqida_ortga_key
from keyboards.default.requestdata import sorov_vacan_data, sorov_contact_data, kurs_contact_data

from loader import dp
# photo AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE
# video BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE

@dp.callback_query_handler(text="uzbek")
async def show_staff(call: CallbackQuery):
    # photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"
    msg = f"Assalam Aleykum hurmatli {call.message.from_user.full_name}\n"
    msg += "IT akademiya botimizga xush kelibsiz\n"
    msg += "Bot tilini ozgartirishni istasangiz /language kamandasini yuboring\n"
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=birinchi_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="menyu")
async def show_staff(call: CallbackQuery):
    # photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"
    await call.message.answer_photo(photo=photo_id, caption="Akademiyamizni ko'rishingiz mumkin.", reply_markup=bosh_bolim_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="oqituvchi")
async def show_staff(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="O'qituvchilarimizni ko'rishingiz mumkin.", reply_markup=oqituvchi_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kurslar")
async def show_staff(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="Kurslarimizni ko'rishingiz mumkin.", reply_markup=kurs_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="haqida")
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
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=haqida_ortga_key)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="otajon_bozorboyev")
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

@dp.callback_query_handler(text="rustam_h")
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

@dp.callback_query_handler(text="xusan_dev")
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

@dp.callback_query_handler(text="otabek_front")
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

@dp.callback_query_handler(text="xurshid_backend")
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

@dp.callback_query_handler(text="miraziz_front")
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

@dp.callback_query_handler(text="frontend")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Backend dasturlash kursi sizga veb-saytlar va mobil ilovalarning orqa tomonini rivojlantirish bo'yicha zarur bo'lgan ko'nikmalarni beradi.\n"
    msg += " Ushbu kursda siz ma'lumotlar bazalari, serverlar, APIlar va boshqa texnologiyalar bilan ishlashni o'rganasiz."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=kurs_ortga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="bekend")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Backend dasturlash kursi sizga veb-saytlar va mobil ilovalarning orqa tomonini rivojlantirish bo'yicha zarur bo'lgan ko'nikmalarni beradi.\n"
    msg += " Ushbu kursda siz ma'lumotlar bazalari, serverlar, APIlar va boshqa texnologiyalar bilan ishlashni o'rganasiz."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=kurs_ortga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kiber")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Backend dasturlash kursi sizga veb-saytlar va mobil ilovalarning orqa tomonini rivojlantirish bo'yicha zarur bo'lgan ko'nikmalarni beradi.\n"
    msg += " Ushbu kursda siz ma'lumotlar bazalari, serverlar, APIlar va boshqa texnologiyalar bilan ishlashni o'rganasiz."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=kurs_ortga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="dizayner")
async def show_staff(call: CallbackQuery):
    # video_id = InputFile(path_or_bytesio="videos\cybersecurity.mp4")
    video_id = "BAACAgIAAxkBAAIB-2cXXRHwrvPZg5q29LRXv5CFCsyUAAJTUgACiqjASAABrOUkkeS49jYE"
    msg = "Backend dasturlash kursi sizga veb-saytlar va mobil ilovalarning orqa tomonini rivojlantirish bo'yicha zarur bo'lgan ko'nikmalarni beradi.\n"
    msg += " Ushbu kursda siz ma'lumotlar bazalari, serverlar, APIlar va boshqa texnologiyalar bilan ishlashni o'rganasiz."
    await call.message.answer_video(video=video_id, caption=msg, reply_markup=kurs_ortga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ortga")
async def back(call: CallbackQuery):
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    await call.message.answer_photo(photo=photo_id, caption="Akademiyamizni ko'rishingiz mumkin.", reply_markup=bosh_bolim_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ozgacha_ortga")
async def back(call: CallbackQuery):
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    msg = f"Assalam Aleykum hurmatli {call.message.from_user.full_name}\n"
    msg += "IT akademiya botimizga xush kelibsiz\n"
    msg += "Bot tilini ozgartirishni istasangiz /language kamandasini yuboring\n"
    await call.message.answer_photo(photo=photo_id, caption=msg, reply_markup=birinchi_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="qituvchi_back")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="O'qituvchilarimizni ko'rishingiz mumkin.", reply_markup=oqituvchi_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kurs_ortga")
async def back(call: CallbackQuery):
    photo_id = InputFile(path_or_bytesio="photos\photo_2024-10-20_11-36-22.jpg")
    await call.message.answer_photo(photo=photo_id, caption="Kurslarimizni ko'rishingiz mumkin.", reply_markup=kurs_key)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="vakansiya")
async def back(call: CallbackQuery):
    await call.message.answer("Bizga bir qancha malumotlaringiz kerak,\nIltimos pastgi tugmani bosing.", reply_markup=sorov_vacan_data)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="boglansh")
async def back(call: CallbackQuery):
    await call.message.answer("Bizga bir qancha malumotlaringiz kerak,\nIltimos pastgi tugmani bosing.", reply_markup=sorov_contact_data)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yozilish")
async def back(call: CallbackQuery):
    await call.message.answer("Bizga bir qancha malumotlaringiz kerak,\nIltimos pastgi tugmani bosing.", reply_markup=kurs_contact_data)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.message_handler(text="Bekor qilish")
async def remove(message: Message):
    await message.answer("Bekor qilindi", reply_markup=ReplyKeyboardRemove())
    photo_id = "AgACAgIAAxkBAAIB-WcXXQE0VVQmZXv8EEwAAZJ3H2cjUAACHeYxG4qowEhPkWB7Hmmb4wEAAwIAA3kAAzYE"      
    await message.answer_photo(photo=photo_id,  caption="Akademiyamizni ko'rishingiz mumkin.", reply_markup=bosh_bolim_key)


