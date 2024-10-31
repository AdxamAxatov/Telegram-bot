from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇸 EN", callback_data="en"),
            InlineKeyboardButton(text="🇺🇿 UZ", callback_data="uzbek"),
        ]
    ]
)
