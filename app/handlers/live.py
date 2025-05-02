from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

LIVE_MATCH = {
    "opponent": "Team Liquid",
    "score": "10 x 8",
    "status": "2º mapa - Ao Vivo",
    "start_time": "17:00",
}


async def live_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        f"🔥 *Jogo ao Vivo!*\n\n"
        f"🆚 FURIA vs {LIVE_MATCH['opponent']}\n"
        f"⏰ Início: {LIVE_MATCH['start_time']}\n"
        f"🎯 Placar: {LIVE_MATCH['score']}\n"
        f"📺 Status: {LIVE_MATCH['status']}\n"
    )

    keyboard = [
        [InlineKeyboardButton("Voltar ao Menu Principal", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.message.reply_text(
        message, parse_mode="Markdown", reply_markup=reply_markup
    )
