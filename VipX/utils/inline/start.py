from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 𝐎ᴜʀ 𝐆ʀᴏᴜᴩ 🥰",
url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="🥹 𝐇ᴇʟᴩ 🥹",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="😂 𝐒ᴇᴛᴛɪɴɢ𝐬 😂", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❣️ 𝐁ᴀᴅ𝗌ʜᴀʜ ❣️", url=f"https://t.me/Shivans_Raj_BrockenHart"),
            InlineKeyboardButton(
                text="❤️ 𝐁ᴇɢᴀᴍ ❤️", url=f"https://t.me/Ziddi_Rani"
             ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐎ᴡɴᴇʀ 💖", user_id=OWNER),
            InlineKeyboardButton(
                text="💝 𝐂ᴏ 𝐎ᴡɴᴇʀ 💝", url=f"https://t.me/Sonu2860"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 𝐎ᴜʀ 𝐆ʀᴏᴜᴩ 🥰",
url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥹 𝐇ᴇʟᴩ 🥹", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❣️ 𝐁ᴀᴅ𝗌ʜᴀʜ ❣️", url=f"https://t.me/Shivans_Raj_BrockenHart"),
            InlineKeyboardButton(
                text="❤️ 𝐁ᴇɢᴀᴍ ❤️", url=f"https://t.me/Ziddi_Rani"
            ),
        ],
        [
            InlineKeyboardButton(text="💖 𝐎ᴡɴᴇʀ 💖", user_id=OWNER),
            InlineKeyboardButton(
                text="💝 𝐂ᴏ 𝐎ᴡɴᴇʀ 💝", url=f"https://t.me/Sonu2860"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🌹 𝐒ᴛᴜᴅʏ 𝐆ʀᴏᴜᴘ  🌹", url=f"https://t.me/Study_House_Family"
            ),
           ],
     ]
    return buttons
