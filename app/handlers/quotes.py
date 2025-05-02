from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import random


async def quotes_handler(update: Update, context: CallbackContext) -> None:
    frases_furia = [
        "🖤 'Cada round é uma chance de mostrar quem somos.' - yuurih",
        "🖤 'A estratégia vence a força bruta.' - art",
        "🖤 'Confiança, treino e sangue nos olhos.' - KSCERATO",
        "🖤 'Vitória se constrói com trabalho em equipe.' - VINI",
        "🖤 'Não jogamos só com o mouse, jogamos com o coração.' - drop",
        "🖤 'Errar faz parte, desistir nunca.' - yuurih",
        "🖤 'Respeitamos todos, tememos ninguém.' - art",
        "🖤 'O impossível é só mais um obstáculo.' - KSCERATO",
        "🖤 'A cada jogo, uma nova história.' - VINI",
        "🖤 'A FURIA é mais que um time, é uma família.' - drop",
    ]

    introducao = "⚡ *Inspiração da FURIA para hoje:*"
    frase = random.choice(frases_furia)

    mensagem = f"{introducao}\n\n{frase}"

    keyboard = [
        [InlineKeyboardButton("Voltar ao Menu Principal", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.message.reply_text(
            mensagem, parse_mode="Markdown", reply_markup=reply_markup
        )
    elif update.message:
        await update.message.reply_text(
            mensagem, parse_mode="Markdown", reply_markup=reply_markup
        )
