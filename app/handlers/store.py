from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def store_handler(update: Update, context: CallbackContext) -> None:
    message = (
        "🔥 *Bem-vindo à Loja Oficial da FURIA!*\n\n"
        "Mostre que você é um verdadeiro FURIOSO com os produtos exclusivos da nossa equipe!\n"
        "Confira camisetas, moletons, bonés, e muito mais com estilo e atitude. 💪🦊\n\n"
        "👇 Escolha uma categoria para acessar diretamente:"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🧢 Bonés", url="https://www.furia.gg/produtos/acessorios/bones"
            )
        ],
        [
            InlineKeyboardButton(
                "👕 Camisetas", url="https://www.furia.gg/produtos/vestuario/camisetas"
            )
        ],
        [
            InlineKeyboardButton(
                "🧥 Moletons", url="https://www.furia.gg/produtos/vestuario/moletons"
            )
        ],
        [
            InlineKeyboardButton(
                "🛒 Ver Loja Completa", url="https://www.furia.gg/produtos"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 Voltar ao Menu Principal", callback_data="back_to_main"
            )
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if not update.callback_query:
        await update.message.reply_text(
            message, reply_markup=reply_markup, parse_mode="Markdown"
        )
    else:
        await update.callback_query.edit_message_text(
            message, reply_markup=reply_markup, parse_mode="Markdown"
        )
