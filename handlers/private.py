
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ \n๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ \n๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐ค \nโญ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ [abhinas](https://t.me/abhinasroy)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "โฐsupport๐โฑ", url="https://t.me/ABOUT_ABHINAS"
                    ),
                    InlineKeyboardButton(
                        "โฐGroup๐ฉโฑ", url="https://t.me/DOSTI_GROUP_1234"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โฐcommand๐ฅโฑ", url="http://telegra.ph/Command-11-27"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ROY music bot online\n๐ ๐๐๐ฉ๐จ๐ซ๐ญ_๐๐ฉ ๐ฅ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Supportโค๏ธ", url="ABOUT_ABHINAS")
                ]
            ]
        )
   )
