from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from app.handlers.schedule import games_data, get_next_game


async def set_reminder(update: Update, context: CallbackContext, game_index: int):
    game = games_data[game_index]
    context.user_data["reminder"] = game
    message = f"✅ Lembrete agendado para o jogo: {game['teams']} no dia {game['date']} às {game['time']}!"
    await update.callback_query.message.reply_text(message)


async def show_reminders_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Ativar Próximo Lembrete", callback_data="remind_activate"
            )
        ],
        [
            InlineKeyboardButton(
                "❌ Desativar Lembrete", callback_data="remind_deactivate"
            )
        ],
        [InlineKeyboardButton("👁️ Visualizar Lembrete", callback_data="remind_view")],
        [InlineKeyboardButton("🔙 Voltar", callback_data="back_to_main")],
    ]

    await query.edit_message_text(
        "⏰ O que você deseja fazer?", reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def show_next_game_reminder(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    index, next_game = get_next_game()
    if not next_game:
        await query.edit_message_text("❌ Nenhum jogo futuro encontrado.")
        return

    keyboard = [
        [InlineKeyboardButton("✅ Ativar Lembrete", callback_data=f"remind_{index}")],
        [InlineKeyboardButton("🔙 Voltar", callback_data="back_to_main")],
    ]

    msg = (
        f"🔔 Deseja ativar lembrete para o próximo jogo?\n\n"
        f"🕒 {next_game['date']} às {next_game['time']} - {next_game['teams']}"
    )

    await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))


async def clear_reminder(update: Update, context: CallbackContext):
    if "reminder" in context.user_data:
        del context.user_data["reminder"]
        await update.callback_query.message.reply_text(
            "🗑️ Lembrete removido com sucesso."
        )
    else:
        await update.callback_query.message.reply_text(
            "ℹ️ Nenhum lembrete estava ativado."
        )


async def view_reminder(update: Update, context: CallbackContext):
    reminder = context.user_data.get("reminder")
    if reminder:
        await update.callback_query.message.reply_text(
            f"🔔 Lembrete ativo para: {reminder['teams']} em {reminder['date']} às {reminder['time']}."
        )
    else:
        await update.callback_query.message.reply_text("ℹ️ Nenhum lembrete está ativo.")


async def schedule_specific_reminder(
    update: Update, context: CallbackContext, index: int
):
    await set_reminder(update, context, index)
