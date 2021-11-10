from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust me, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!

By @DEOOUS
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("♰ بدا استخراج", callback_data="generate")],
        [InlineKeyboardButton(text="♰ رجوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("♰ بدا استخراج", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("♰ بدا استخراج", callback_data="generate")],
        [InlineKeyboardButton("♰ قناتنا", url="https://telegram.dog/deoous")],
        [
            InlineKeyboardButton("♰ مساعده", callback_data="help"),
            InlineKeyboardButton("♰ وصف البوت", callback_data="about")
        ],
        [InlineKeyboardButton("♰ مطورين", url="https://telegram.dog/rekhso")],
    ]

    # Help Message
    HELP = """
» انقر على الزر أدناه أو استخدم/إنشاء الأمر لبدء إنشاء جلسة!

» انقر على الزر المطلوب؛ [Pyrogram/Telethon]

» أدخل المتغيرات المطلوبة عندما يطلب منك ذلك.

راجع للشغل، إذا كنت لا تثق بي، يمكنك استضافة [واحد] مثلي باستخدام شفرة المصدر الخاصة بي المتوفرة في صفحتي عن؛ [/حول]
"""

    # About Message
    ABOUT = """
وصف البوت ♰
[مطور](https://t.me/rekhso)
[المطور الي كتب البوت](https://t.me/ckcck)
[قناتنا](https://t.me/deoous)
♰ وشكرا
    """
