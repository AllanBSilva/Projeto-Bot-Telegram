from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def start_handler(update: Update, context: CallbackContext) -> None:
    welcome_message = (
        "👋 *Bem-vindo ao FURIA Bot!*\n\n"
        "Aqui você encontra tudo sobre a FURIA Esports:\n\n"
        "Escolha uma opção abaixo 👇"
    )

    keyboard = [
        [
            InlineKeyboardButton("📅 Próximos Jogos", callback_data="go_schedule"),
            InlineKeyboardButton("📊 Resultados", callback_data="go_results"),
        ],
        [
            InlineKeyboardButton("🎯 Jogadores", callback_data="go_players"),
            InlineKeyboardButton("🗣️ Frases Marcantes", callback_data="go_quotes"),
        ],
        [
            InlineKeyboardButton("🔥 Ao Vivo", callback_data="go_live"),
            InlineKeyboardButton("❓ Quiz", callback_data="go_quiz"),
        ],
        [
            InlineKeyboardButton("⏰ Lembretes", callback_data="go_reminder"),
            InlineKeyboardButton("ℹ️ Ajuda", callback_data="go_help"),
        ],
        [
            InlineKeyboardButton("🛒 Loja Oficial", callback_data="go_store"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            welcome_message, reply_markup=reply_markup, parse_mode="Markdown"
        )
    elif update.callback_query and update.callback_query.message:
        await update.callback_query.message.reply_text(
            welcome_message, reply_markup=reply_markup, parse_mode="Markdown"
        )
