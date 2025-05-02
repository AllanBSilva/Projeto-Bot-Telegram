import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def results_handler(update: Update, context: CallbackContext) -> None:
    resultados_furia = [
        "FURIA 2 - 0 MIBR - Torneio X - 30/04",
        "FURIA 1 - 2 Astralis - Torneio Y - 28/04",
        "FURIA 3 - 1 Liquid - Torneio Z - 25/04",
        "FURIA 2 - 2 FaZe Clan - Torneio W - 22/04",
        "FURIA 0 - 3 Vitality - Torneio X - 20/04",
        "FURIA 2 - 1 NaVi - Torneio Y - 18/04",
        "FURIA 1 - 2 G2 Esports - Torneio Z - 15/04",
        "FURIA 3 - 0 Heroic - Torneio W - 12/04",
    ]

    def formatar_resultados(resultados):
        resultados_formatados = []
        padrao = r"FURIA (\d+) - (\d+) (.+?) - (.+?) - (\d{2}/\d{2})"

        for resultado in resultados:
            match = re.search(padrao, resultado)
            if match:
                furia_score = int(match.group(1))
                opponent_score = int(match.group(2))
                opponent = match.group(3)
                torneio = match.group(4)
                data = match.group(5)

                if furia_score > opponent_score:
                    emoji = "🟢"
                elif furia_score < opponent_score:
                    emoji = "🔴"
                else:
                    emoji = "🟡"

                texto_formatado = f"{emoji} FURIA {furia_score} - {opponent_score} {opponent} · {torneio} · {data}"
                resultados_formatados.append(texto_formatado)
            else:
                resultados_formatados.append(f"❓ <code>{resultado}</code>")
        return resultados_formatados

    resultados_formatados = formatar_resultados(resultados_furia)
    message = "<b>📊 Últimos resultados da FURIA:</b>\n\n" + "\n\n".join(
        resultados_formatados
    )

    keyboard = [
        [InlineKeyboardButton("Voltar ao Menu Principal", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if not update.callback_query:
        await update.message.reply_text(
            message, reply_markup=reply_markup, parse_mode="HTML"
        )
    else:
        await update.callback_query.edit_message_text(
            message, reply_markup=reply_markup, parse_mode="HTML"
        )
