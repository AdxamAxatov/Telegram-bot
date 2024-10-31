from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


first_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Menu", callback_data="menu")
        ]
    ]
)



menu_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍🏫 Staff", callback_data="staf"),
            InlineKeyboardButton(text="🎓 Courses", callback_data="courses"),
        ],
        [
            InlineKeyboardButton(text="🙋‍♂️ About", callback_data="about"),
            InlineKeyboardButton(text="🈳 Vacancy", callback_data="vacan"),
        ],
        [
            InlineKeyboardButton(text="📞 Contact", callback_data="contact"),
        ],
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="special_back"),
        ]
    ]
)

# -----------------------------------------------------------------------------------
# UZB
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
