from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




birinchi_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bosh bo'lim", callback_data="menyu")
        ]
    ]
)



bosh_bolim_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍🏫 O'qituvchilar", callback_data="oqituvchi"),
            InlineKeyboardButton(text="🎓 Kurslar", callback_data="kurslar"),
        ],
        [
            InlineKeyboardButton(text="🙋‍♂️ Haqida", callback_data="haqida"),
            InlineKeyboardButton(text="🈳 Vakansiyalar", callback_data="vakansiya"),
        ],
        [
            InlineKeyboardButton(text="📞 Bog'lanish", callback_data="boglansh"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="ozgacha_ortga"),
        ]
    ]
)
