from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def help_handler(update: Update, context: CallbackContext) -> None:
    help_text = (
        "ℹ️ *Ajuda do FURIA Bot*\n\n"
        "Aqui está um guia sobre o que cada botão do menu faz:\n\n"
        "📅 *Próximos Jogos*: Veja os próximos confrontos da FURIA, com horários e adversários.\n\n"
        "📊 *Últimos Resultados*: Acompanhe os placares das partidas mais recentes.\n\n"
        "🎯 *Jogadores*: Descubra mais sobre os jogadores do time: funções, destaques e curiosidades.\n\n"
        "🗣️ *Frases da Equipe*: Receba frases motivacionais ditas pelos próprios jogadores da FURIA.\n\n"
        "🛒 *Loja Oficial*: Acesse o link da loja oficial e confira os produtos exclusivos.\n\n"
        "Caso tenha dúvidas ou encontre algum problema, entre em contato com o suporte do bot.\n"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "🏠 Voltar ao Menu Principal", callback_data="back_to_main"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            help_text, reply_markup=reply_markup, parse_mode="Markdown"
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            help_text, reply_markup=reply_markup, parse_mode="Markdown"
        )
