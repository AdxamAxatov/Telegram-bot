from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# request = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             # KeyboardButton(text="Share", request_contact=True),
#             # KeyboardButton(text="Cancel"),
#             # KeyboardButton(text='Location', request_location=True),
#         ],
#     ], resize_keyboard=True
# )

request_vacan_data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Share"),
            KeyboardButton(text="Cancel"),
        ]
    ], resize_keyboard=True
)


request_contact_data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Share info"),
            KeyboardButton(text="Cancel"),
        ]
    ], resize_keyboard=True
)

course_contact_data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Share Info"),
            KeyboardButton(text="Cancel"),
        ]
    ], resize_keyboard=True
)

# -----------------------------------------------------------------------------------


sorov_vacan_data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ulashish"),
            KeyboardButton(text="Bekor qilish"),
        ]
    ], resize_keyboard=True
)


sorov_contact_data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Malumot ulashish"),
            KeyboardButton(text="Bekor qilish"),
        ]
    ], resize_keyboard=True
)

kurs_contact_data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Malumot Ulashish"),
            KeyboardButton(text="Bekor qilish"),
        ]
    ], resize_keyboard=True
)