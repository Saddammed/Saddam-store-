from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8179576448:AAGR15urYreu8zooAF4eXyguRNn7nqkkank"
CHANNEL_USERNAME = "@Online_store485353"  # قناة التليجرام (إجباري)

# ===== رسالة قبل الاشتراك =====
WELCOME_TEXT = """
🔥 مرحباً بك {name} في *Saddam Store*!

⚡ للاستفادة من خدماتنا، يرجى الاشتراك في قنواتنا:

1️⃣ قناة تليجرام (إجباري)
2️⃣ قناة واتساب (إجباري)
3️⃣ تيك توك (إجباري)
4️⃣ فيسبوك (إجباري)

👇 بعد الاشتراك اضغط *تم الاشتراك*:
"""

# ===== رسالة بعد التحقق =====
AFTER_TEXT = """
🎉 مرحباً {name} في *Saddam Store*!

🔥 متجر رقمي متكامل
🎮 PUBG | Free Fire | eFootball
💎 TikTok Coins
💻 منتجات رقمية حصرية
⚡ تسليم فوري

👇 اختر من القائمة:
"""

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔵 قناة التليجرام", url="https://t.me/Online_store485353")],
        [InlineKeyboardButton("🟢 قناة واتساب", url="https://whatsapp.com/channel/0029Vb74xLN1yT2ArsVMwS2B")],
        [InlineKeyboardButton("🎵 تيك توك", url="https://www.tiktok.com/@saddam33000")],
        [InlineKeyboardButton("📘 فيسبوك", url="https://www.facebook.com/share/17hWP9gCDd/")],
        [InlineKeyboardButton("✅ تم الاشتراك", callback_data="check")]
    ]

    await update.message.reply_text(
        WELCOME_TEXT.format(name=update.effective_user.first_name),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ===== التحقق من الاشتراك =====
async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if member.status in ["member", "administrator", "creator"]:
        menu_keyboard = [
            [InlineKeyboardButton("🎮 شحن الألعاب", callback_data="games")],
            [InlineKeyboardButton("💎 TikTok Coins", callback_data="tiktok")],
            [InlineKeyboardButton("💻 خدمات رقمية", callback_data="digital")],
            [InlineKeyboardButton("📞 تواصل معنا", url="https://t.me/Saddammed")]
        ]

        await query.edit_message_text(
            AFTER_TEXT.format(name=query.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(menu_keyboard),
            parse_mode="Markdown"
        )
    else:
        await query.answer("❌ اشترك في قناة التليجرام أولاً", show_alert=True)

# ===== تشغيل البوت =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_sub))

    app.run_polling()

if name == "__main__":
    main()
