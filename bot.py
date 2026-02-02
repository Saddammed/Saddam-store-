from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8179576448:AAGR15urYreu8zooAF4eXyguRNn7nqkkank"
CHANNEL_USERNAME = "@Online_store485353"

WELCOME_TEXT = """
🔥 مرحباً بك {name} في *Saddam Store*!

⚡ للاستفادة من خدماتنا، يرجى الاشتراك في قنواتنا:

👇 بعد الاشتراك اضغط *تم الاشتراك*:
"""

MAIN_MENU_TEXT = """
🎉 مرحباً {name} في *Saddam Store*!

اختر الخدمة التي تريدها 👇
"""

GAMES_TEXT = """
🔥 *شحن الألعاب*:

• PUBG Mobile  
• Free Fire  
• eFootball  
• TikTok Coins  

📲 واتساب:
https://wa.me/message/REDKIHRAVCUEB1

💬 تيليجرام:
https://t.me/Saddammed
"""

DIGITAL_TEXT = """
🛒 *المنتجات الرقمية*:

• Netflix  
• Google Play  
• Apple Store  
• اشتراكات تطبيقات أخرى  

📲 واتساب:
https://wa.me/message/REDKIHRAVCUEB1

💬 تيليجرام:
https://t.me/Saddammed
"""

WEB_TEXT = """
🌐 *تصميم المواقع*:

• مواقع شخصية  
• متاجر إلكترونية  
• صفحات هبوط  

تصميم عصري ومتوافق مع الجوال 📱

📲 واتساب:
https://wa.me/message/REDKIHRAVCUEB1

💬 تيليجرام:
https://t.me/Saddammed
"""

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔵 قناة تيليجرام", url="https://t.me/Online_store485353")],
        [InlineKeyboardButton("🟢 قناة واتساب", url="https://whatsapp.com/channel/0029Vb74xLN1yT2ArsVMwS2B")],
        [InlineKeyboardButton("🎵 TikTok", url="https://www.tiktok.com/@saddam33000")],
        [InlineKeyboardButton("📘 Facebook", url="https://www.facebook.com/share/17hWP9gCDd/")],
        [InlineKeyboardButton("✅ تم الاشتراك", callback_data="check")]
    ]

    await update.message.reply_text(
        WELCOME_TEXT.format(name=update.effective_user.first_name),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ===== تحقق الاشتراك =====
async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    member = await context.bot.get_chat_member(CHANNEL_USERNAME, query.from_user.id)

    if member.status in ["member", "administrator", "creator"]:
        menu = [
            [
                InlineKeyboardButton("🔥 شحن ألعاب", callback_data="games"),
                InlineKeyboardButton("🛒 منتجات رقمية", callback_data="digital")
            ],
            [
                InlineKeyboardButton("🌐 تصميم مواقع", callback_data="web")
            ],
            [
                InlineKeyboardButton("🌍 موقعنا الرسمي", url="https://digital-service-hub--sidimed485353.replit.app")
            ]
        ]

        await query.edit_message_text(
            MAIN_MENU_TEXT.format(name=query.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(menu),
            parse_mode="Markdown"
        )
    else:
        await query.answer("❌ اشترك في القناة أولاً", show_alert=True)

# ===== القوائم =====
async def menus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    back = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ رجوع", callback_data="check")]
    ])

    if query.data == "games":
        await query.edit_message_text(GAMES_TEXT, reply_markup=back, parse_mode="Markdown")

    elif query.data == "digital":
        await query.edit_message_text(DIGITAL_TEXT, reply_markup=back, parse_mode="Markdown")

    elif query.data == "web":
        await query.edit_message_text(WEB_TEXT, reply_markup=back, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_sub, pattern="^check$"))
    app.add_handler(CallbackQueryHandler(menus))
    app.run_polling()

if __name__ == "__main__":
    main()
