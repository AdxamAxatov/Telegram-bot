from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.backKeyboard import back_key
from loader import dp
from states.personalData2 import PersonalData2


@dp.message_handler(text="Share info")
async def enter_test(message: types.Message):
    await message.answer("Enter your full name", reply_markup=ReplyKeyboardRemove())
    await PersonalData2.fullname.set()

@dp.message_handler(state=PersonalData2.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name = fullname)
    await state.update_data(
        {'name': fullname}
        )

    await message.answer("Enter your phone number")
    await PersonalData2.next()
    # await PersonalData.email.set()

@dp.message_handler(state=PersonalData2.phoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
        )
    
    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')

    msg = "The following data has been recieved:\n"
    msg += f"Name - {name}\n"
    msg += f"Phone - {phone}\n"   
    msg += f"Admin will be in touch shortly."   
    await message.answer(msg, reply_markup=back_key)

    await state.finish()
    await state.reset_state(with_data = False)