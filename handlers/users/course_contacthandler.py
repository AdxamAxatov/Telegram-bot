from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.coursesKeyboard import course_back
from loader import dp
from states.personalData3 import PersonalData3


@dp.message_handler(text="Share Info")
async def enter_test(message: types.Message):
    await message.answer("Enter your full name", reply_markup=ReplyKeyboardRemove())
    await PersonalData3.fullname.set()

@dp.message_handler(state=PersonalData3.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name = fullname)
    await state.update_data(
        {'name': fullname}
        )

    await message.answer("Enter your phone number")
    await PersonalData3.next()
    # await PersonalData.email.set()

@dp.message_handler(state=PersonalData3.phoneNumber)
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
    await message.answer(msg, reply_markup=course_back)

    await state.finish()
    await state.reset_state(with_data = False)