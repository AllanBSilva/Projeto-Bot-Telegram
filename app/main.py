from .config import TOKEN
from datetime import datetime
from telegram import Update
from telegram.ext import MessageHandler, filters
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from .handlers.start import start_handler
from .handlers.schedule import schedule_handler
from .handlers.results import results_handler
from .handlers.players import players_handler
from .handlers.quotes import quotes_handler
from .handlers.store import store_handler
from .handlers.help import help_handler
from .handlers.menu_router import menu_router, button_callback
from .handlers.live import live_handler
from .handlers.quiz import start_quiz, answer_quiz
from .handlers.reminder import (
    clear_reminder,
    schedule_specific_reminder,
    set_reminder,
    show_next_game_reminder,
    show_reminders_menu,
    view_reminder,
)


async def start(update: Update, context):
    await update.message.reply("Olá! Eu sou o seu bot.")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Ocorreu um erro: {context.error}")

    if update and update.effective_message:
        await update.effective_message.reply_text(
            "⚠️ Ocorreu um erro inesperado. Tente novamente mais tarde."
        )


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ Desculpe, não reconheço esse comando. Use /help para ver as opções disponíveis."
    )


async def schedule_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):  # noqa: F811
    await update.message.reply_text(
        "✅ Jogo marcado para 17:00. Notificação programada."
    )
    game_time = datetime.strptime("17:00", "%H:%M").replace(
        year=datetime.now().year, month=datetime.now().month, day=datetime.now().day
    )
    set_reminder(context, update.effective_chat.id, game_time)


def run_bot():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(
        MessageHandler(
            filters.Regex("(?i)^(oi|Oi|olá|Olá|ola|Ola|menu|Menu|Start|start)$"),
            start_handler,
        )
    )
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("quiz", start_quiz))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, answer_quiz)
    )
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu_router)
    )
    application.add_handler(MessageHandler(filters.TEXT, start_handler))
    application.add_handler(CommandHandler("schedule", schedule_handler))
    application.add_handler(CommandHandler("results", results_handler))
    application.add_handler(CommandHandler("players", players_handler))
    application.add_handler(CommandHandler("quotes", quotes_handler))
    application.add_handler(CommandHandler("store", store_handler))
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(
        CallbackQueryHandler(button_callback)
    )  # Manipulador de callback
    application.add_error_handler(error_handler)
    application.add_handler(MessageHandler(filters.COMMAND, unknown_handler))
    application.add_handler(CommandHandler("live", live_handler))
    application.add_handler(
        CallbackQueryHandler(show_reminders_menu, pattern="^reminders_menu$")
    )
    application.add_handler(
        CallbackQueryHandler(show_next_game_reminder, pattern="^remind_next$")
    )
    application.add_handler(
        CallbackQueryHandler(clear_reminder, pattern="^remind_deactivate$")
    )
    application.add_handler(
        CallbackQueryHandler(view_reminder, pattern="^remind_view$")
    )
    application.add_handler(
        CallbackQueryHandler(
            lambda u, c: schedule_specific_reminder(
                u, c, int(u.callback_query.data.split("_")[1])
            ),
            pattern="^remind_\\d+$",
        )
    )

    print("Iniciando polling...")
    application.run_polling()
    print("Polling finalizado.")


if __name__ == "__main__":
    run_bot()
