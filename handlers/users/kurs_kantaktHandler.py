from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.backKeyboard import ortga_key
from loader import dp
from states.malumot3 import malumot3


@dp.message_handler(text="Malumot Ulashish")
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
    await malumot3.fullname.set()

@dp.message_handler(state=malumot3.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name = fullname)
    await state.update_data(
        {'name': fullname}
        )

    await message.answer("Telefon raqamingizni kiriting")
    await malumot3.next()
    # await PersonalData.email.set()

@dp.message_handler(state=malumot3.phoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
        )
    
    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')

    msg = "Quyidagi malumotlar qabul qilindi:\n"
    msg += f"Ism - {name}\n"
    msg += f"Telefon raqam - {phone}\n"   
    msg += f"Tez orada admin aloqaga chiqadi."   
    await message.answer(msg, reply_markup=ortga_key)

    await state.finish()
    await state.reset_state(with_data = False)

