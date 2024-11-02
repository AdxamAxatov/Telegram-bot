from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="to_menu"),
         
        ]
    ])


