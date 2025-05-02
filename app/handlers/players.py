from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

jogadores_furia = [
    "🖤 **yuurih** - AWPer da FURIA, destaque nas últimas competições, conhecido por seu incrível controle de mira e habilidades com a AWP.",
    "🖤 **art** - IGL (In-Game Leader), estrategista do time, responsável por coordenar as táticas e decisões durante as partidas.",
    "🖤 **KSCERATO** - Rifler, com grande impacto em todas as partidas, conhecido por sua consistência e precisão nas eliminações.",
    "🖤 **VINI** - Rifler e suporte, grande experiência em competições, sempre focado em dar apoio tático à equipe e cumprir funções cruciais.",
    "🖤 **drop** - Suporte tático, foco em ajudar a equipe, responsável por controlar áreas do mapa e garantir a visão estratégica do time.",
]

PLAYERS_PER_PAGE = 1


async def players_handler(update: Update, context: CallbackContext) -> None:
    page = int(context.args[0]) if context.args else 1
    start_index = (page - 1) * PLAYERS_PER_PAGE
    end_index = page * PLAYERS_PER_PAGE

    message = f"Aqui está o jogador {start_index + 1} de {len(jogadores_furia)}:\n\n"
    message += jogadores_furia[start_index:end_index][0]

    keyboard = []

    if end_index < len(jogadores_furia):
        keyboard.append(
            [InlineKeyboardButton("Próximo", callback_data=f"next_player_{page + 1}")]
        )
    if page > 1:
        keyboard.append(
            [InlineKeyboardButton("Anterior", callback_data=f"back_player_{page - 1}")]
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
