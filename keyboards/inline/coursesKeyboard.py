from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

course_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖥️ Frontend", callback_data="front"),
            InlineKeyboardButton(text="⚙️ Backend", callback_data="backend"),
        ],
        [
            InlineKeyboardButton(text="🛡️ Cyber Security", callback_data="cyber"),
            InlineKeyboardButton(text="🎨 Graphic Designer", callback_data="designer"),
        ],
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="back"),
        ]
    ]
)

course_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Apply", callback_data="apply"),
            InlineKeyboardButton(text="🔙 Back", callback_data="course_back"),

        ]
    ]
)

# -----------------------------------------------------------------------------------

# uzb
kurs_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖥️ Frontend", callback_data="frontend"),
            InlineKeyboardButton(text="⚙️ Backend", callback_data="bekend"),
        ],
        [
            InlineKeyboardButton(text="🛡️ Kiber xavfsizlik", callback_data="kiber"),
            InlineKeyboardButton(text="🎨 Grafik Dizayner", callback_data="dizayner"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga"),
        ]
    ]
)

kurs_ortga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Kursga yozilish", callback_data="yozilish"),
            InlineKeyboardButton(text="🔙 Ortga", callback_data="kurs_ortga"),

        ]
    ]
)