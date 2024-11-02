from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

resume_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="download", callback_data="to_menu", url="https://drive.google.com/file/d/1c0MRpccz4AUH2v-kY9s2dCn5SvQMpGid/view?usp=sharing"),
            InlineKeyboardButton(text="🔙 Back", callback_data="to_menu"),
         
        ]
    ])

