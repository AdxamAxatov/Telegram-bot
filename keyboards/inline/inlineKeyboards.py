from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 BIO", callback_data="bio"),
            InlineKeyboardButton(text="🌟 Resume", callback_data="resume"),
          
        ],
        [
            InlineKeyboardButton(text="🔗 Link", callback_data="link"),
            InlineKeyboardButton(text="📱 Contact", callback_data="contact", url="https://t.me/obozorboyev_bot"),
        ]
    ]
)

links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🐙 GitHub", url="https://github.com/otajonbozorboyev/"),
            InlineKeyboardButton(text="⚡ Telegram", url="https://t.me/iotajonbozorboev"),
           
        ],
        [
             InlineKeyboardButton(text="👔 Linkedin", url="https://www.linkedin.com/in/otajonbozorboyev/?trk=opento_nprofile_details"),
            InlineKeyboardButton(text="💻 Leetcode", url="https://leetcode.com/u/otajonbozorboyev571/"),
        ],
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="to_menu"),
        ]
    ]
)
