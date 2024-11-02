from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.backKeyboard import back_key
from loader import dp
from states.personalData import PersonalData

@dp.message_handler(text="Share")
async def enter_test(message: types.Message):
    await message.answer("Enter your full name", reply_markup=ReplyKeyboardRemove())
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name = fullname)
    await state.update_data(
        {'name': fullname}
        )

    await message.answer("Enter your email address")
    await PersonalData.next()
    # await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    # await state.update_data(email = email)
    await state.update_data(
        {'email': email}
        )

    await message.answer('Enter your phone number')

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNumber)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
        )
    
    await message.answer('Enter your resume')

    await PersonalData.next()

# @dp.message_handler(state=PersonalData.document)
# async def answer_phone(message: types.Message, state: FSMContext):
#     doc = message.text
@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PersonalData.document)
async def answer_resume(message: types.Message, state: FSMContext):
    doc = message.document

    await state.update_data(
        {'doc': doc}
        )

    # Ma'lumotlarni qayta o'qiymiz:
    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    doc = data.get('doc')


    msg = "The following data has been recieved:\n"
    msg += f"Name - {name}\n"
    msg += f"Email address - {email}\n"
    msg += f"Phone - {phone}\n"   
    # msg += f"Resume {doc}\n"
    msg += f"Admin will be in touch shortly."   
    await message.answer(msg, reply_markup=back_key)

    await state.finish()
    await state.reset_state(with_data = False)

