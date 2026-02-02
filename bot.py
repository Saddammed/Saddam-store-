from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8179576448:AAGR15urYreu8zooAF4eXyguRNn7nqkkank"
CHANNEL_USERNAME = "@Online_store485353"  # غيّرها إذا لزم

WELCOME_TEXT = """
🔥 مرحباً بك {name} في Saddam Hub!

⚡ للاستفادة من خدماتنا:
يرجى الاشتراك في القناة 👇
"""

AFTER_TEXT = """
🎉 تم التحقق بنجاح!

🛒 مرحباً بك في متجر صدام
اختر الخدمة التي تريدها وسيتم الرد عليك 🤝
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("تم الاشتراك ✅", callback_data="check")]]
    await update.message.reply_text(
        WELCOME_TEXT.format(name=update.effective_user.first_name),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if member.status in ["member", "administrator", "creator"]:
        await query.edit_message_text(AFTER_TEXT)
    else:
        await query.edit_message_text("❌ اشترك في القناة أولاً ثم اضغط الزر مرة أخرى")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_sub))

    app.run_polling()

if __name__ == "__main__":
    main()
