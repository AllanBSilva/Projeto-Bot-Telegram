from telegram import Update
from telegram.ext import CallbackContext


async def menu_router(update: Update, context: CallbackContext) -> None:
    if "quiz_question" in context.user_data:
        return

    text = update.message.text

    if text == "📅 Próximos Jogos":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .schedule import schedule_handler

        await schedule_handler(update, context)

    elif text == "📊 Resultados":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .results import results_handler

        await results_handler(update, context)

    elif text == "🎯 Jogadores":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .players import players_handler

        await players_handler(update, context)

    elif text == "🗣️ Frases":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .quotes import quotes_handler

        await quotes_handler(update, context)

    elif text == "🛒 Loja":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .store import store_handler

        await store_handler(update, context)

    elif text == "ℹ️ Ajuda":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .help import help_handler

        await help_handler(update, context)

    elif text == "🔥 Ao Vivo":
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action="typing"
        )
        from .live import live_handler

        await live_handler(update, context)

    elif text == "❓ Quiz":
        await update.message.reply_text(
            "🧠 Iniciando quiz...\nUse o comando /quiz para começar!"
        )

    elif text == "🏠 Voltar ao Menu":
        from .start import start_handler

        await start_handler(update, context)
    else:
        await update.message.reply_text(
            "❌ Comando não reconhecido. Por favor, escolha uma opção do menu."
        )


async def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "go_quiz":
        from app.handlers.quiz import start_quiz

        await start_quiz(update, context)

    elif data.startswith("next_player_") or data.startswith("back_player_"):
        try:
            page = int(data.split("_")[-1])
            context.args = [str(page)]
            from .players import players_handler

            await players_handler(update, context)
        except ValueError:
            await query.answer("Página inválida.")

    elif data == "back_to_main":
        from .start import start_handler

        await start_handler(update, context)

    elif data.startswith("next_") or data.startswith("back_"):
        try:
            page = int(data.split("_")[-1])
            context.args = [str(page)]
            from .schedule import schedule_handler

            await schedule_handler(update, context)
        except ValueError:
            await query.answer("Página inválida.")

    elif data == "go_schedule":
        context.args = ["1"]
        from .schedule import schedule_handler

        await schedule_handler(update, context)

    elif data == "go_results":
        context.args = ["1"]
        from .results import results_handler

        await results_handler(update, context)

    elif data == "go_players":
        context.args = ["1"]
        from .players import players_handler

        await players_handler(update, context)

    elif data == "go_quotes":
        from .quotes import quotes_handler

        await quotes_handler(update, context)

    elif data == "go_store":
        from .store import store_handler

        await store_handler(update, context)

    elif data == "go_live":
        from .live import live_handler

        await live_handler(update, context)

    elif data == "go_help":
        from app.handlers.help import help_handler

        await help_handler(update, context)

    elif data.startswith("remind_"):
        if data == "remind_activate":
            from .schedule import schedule_handler

            await schedule_handler(update, context)

        elif data == "remind_deactivate":
            from .reminder import clear_reminder

            await clear_reminder(update, context)

        elif data == "remind_view":
            from .reminder import view_reminder

            await view_reminder(update, context)

        else:
            try:
                game_index = int(data.split("_")[1])
                from .reminder import schedule_specific_reminder

                await schedule_specific_reminder(update, context, game_index)
            except (ValueError, IndexError):
                await query.answer("ID do jogo inválido.")

    elif query.data.startswith("next_"):
        page = int(query.data.split("_")[1])
        context.args = [str(page)]
        await schedule_handler(update, context)

    elif query.data.startswith("back_"):
        page = int(query.data.split("_")[1])
        context.args = [str(page)]
        await schedule_handler(update, context)

    elif query.data == "back_to_main":
        await query.edit_message_text("🔙 Você voltou ao menu principal.")

    elif data == "go_reminder":
        from .reminder import show_reminders_menu

        await show_reminders_menu(update, context)
    else:
        await query.answer("Ação desconhecida.")
