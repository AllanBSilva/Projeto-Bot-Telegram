from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from datetime import datetime

games_data = [
    {"date": "2025-05-03", "time": "16:00", "teams": "FURIA vs G2 Esports"},
    {"date": "2025-05-06", "time": "18:30", "teams": "FURIA vs NAVI"},
    {"date": "2025-05-10", "time": "20:00", "teams": "FURIA vs FaZe Clan"},
    {"date": "2025-05-13", "time": "15:00", "teams": "FURIA vs Liquid"},
    {"date": "2025-05-17", "time": "19:00", "teams": "FURIA vs Vitality"},
    {"date": "2025-05-21", "time": "17:00", "teams": "FURIA vs Astralis"},
    {"date": "2025-05-25", "time": "16:30", "teams": "FURIA vs Heroic"},
    {"date": "2025-05-29", "time": "21:00", "teams": "FURIA vs Cloud9"},
]

GAMES_PER_PAGE = 10


async def schedule_handler(update: Update, context: CallbackContext) -> None:
    page = int(context.args[0]) if context.args else 1
    start_index = (page - 1) * GAMES_PER_PAGE
    end_index = page * GAMES_PER_PAGE

    message = "📅 **Próximos Jogos:**\n\n"
    keyboard = []

    for i, game in enumerate(games_data[start_index:end_index]):
        game_index = start_index + i
        message += f"🕒 {game['date']} às {game['time']} - {game['teams']}\n"

    if end_index < len(games_data):
        keyboard.append(
            [InlineKeyboardButton("Próximos Jogos", callback_data=f"next_{page + 1}")]
        )
    if page > 1:
        keyboard.append(
            [InlineKeyboardButton("Voltar", callback_data=f"back_{page - 1}")]
        )

    keyboard.append(
        [
            InlineKeyboardButton(
                "⏰ Ativar Lembrete", callback_data=f"remind_{game_index}"
            )
        ]
    )
    keyboard.append(
        [InlineKeyboardButton("Voltar ao Menu Principal", callback_data="back_to_main")]
    )

    reply_markup = InlineKeyboardMarkup(keyboard)

    if not update.callback_query: 
        await update.message.reply_text(
            message, reply_markup=reply_markup, parse_mode="Markdown"
        )
    else:
        await update.callback_query.edit_message_text(
            message, reply_markup=reply_markup, parse_mode="Markdown"
        )


def get_next_game():
    now = datetime.now()

    for i, game in enumerate(games_data):
        game_datetime = datetime.strptime(
            f"{game['date']} {game['time']}", "%Y-%m-%d %H:%M"
        )
        if game_datetime > now:
            return i, game

    return None, None
