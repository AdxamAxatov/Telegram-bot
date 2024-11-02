from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="back"),
        ]
    ]
)


about_back_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Channel", url="https://t.me/tramplin_uz"),
            InlineKeyboardButton(text="🔙 Back", callback_data="back"),

        ]
    ]
)

# -----------------------------------------------------------------------------------


ortga_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga"),
        ]
    ]
)


haqida_ortga_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Channel", url="https://t.me/tramplin_uz"),
            InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga"),

        ]
    ]
)