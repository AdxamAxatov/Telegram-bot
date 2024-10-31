from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.backKeyboard import ortga_key
from loader import dp
from states.malumot1 import malumot1

@dp.message_handler(text="Ulashish")
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
    await malumot1.fullname.set()


@dp.message_handler(state=malumot1.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name = fullname)
    await state.update_data(
        {'name': fullname}
        )

    await message.answer("Email manzilingizni kirinting")
    await malumot1.next()
    # await PersonalData.email.set()


@dp.message_handler(state=malumot1.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    # await state.update_data(email = email)
    await state.update_data(
        {'email': email}
        )

    await message.answer('Telefon raqamingizni kiriting')

    await malumot1.next()


@dp.message_handler(state=malumot1.phoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
        )
    
    await message.answer('Rezumeyingizni jo\'nating')

    await malumot1.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=malumot1.doc)
async def answer_resume(message: types.Message, state: FSMContext):
    document = message.document

    await state.update_data(
        {'doc': document}
        )

    # Ma'lumotlarni qayta o'qiymiz:
    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    document = data.get('doc')


    msg = "Quyidagi malumotlar qabul qilindi:\n"
    msg += f"Ism - {name}\n"
    msg += f"Email manzilingiz - {email}\n"
    msg += f"Telefon raqam - {phone}\n"   
    # msg += f"Resume {doc}\n"
    msg += f"Tez orada admin aloqaga chiqadi."   
    await message.answer(msg, reply_markup=ortga_key)

    await state.finish()
    await state.reset_state(with_data = False)

