from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

quiz_data = {
    "Quem é o capitão da FURIA?": "arT",
    "Qual país a FURIA representa?": "Brasil",
    "Qual é o principal jogo da FURIA Esports?": "CS2",
    "Quem é o coach (técnico) da equipe de CS da FURIA?": "Guerri",
    "Qual é o nome do jogador da FURIA conhecido por usar a AWP?": "saffee",
    "Em que ano a FURIA foi fundada?": "2017",
}


async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    user_data["questions"] = list(quiz_data.items())
    user_data["current_index"] = 0
    user_data["acertos"] = 0
    user_data["erros"] = 0
    user_data["quiz_mode"] = True

    question = user_data["questions"][0][0]
    await send_question(update, context, question)


async def answer_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data

    if update.message.text == "🏠 Voltar ao Menu":
        user_data["quiz_mode"] = False
        from app.handlers.menu_router import menu_router

        await menu_router(update, context)
        return

    if not user_data.get("quiz_mode"):
        await update.message.reply_text(
            "❌ Comando não reconhecido. Por favor, escolha uma opção do menu."
        )
        return

    user_answer = update.message.text.strip().lower()
    idx = user_data["current_index"]
    question, correct_answer = user_data["questions"][idx]

    if user_answer == correct_answer.lower():
        user_data["acertos"] += 1
        await update.message.reply_text("✅ Acertou!")
    else:
        user_data["erros"] += 1
        await update.message.reply_text(
            f"❌ Errou! A resposta certa era: *{correct_answer}*", parse_mode="Markdown"
        )

    idx += 1
    if idx < len(user_data["questions"]):
        user_data["current_index"] = idx
        await send_question(update, context, user_data["questions"][idx][0])
    else:
        acertos = user_data["acertos"]
        erros = user_data["erros"]
        resumo = (
            f"🎉 Fim do quiz!\n\n"
            f"✅ Acertos: {acertos}\n"
            f"❌ Erros: {erros}\n\n"
            "Clique abaixo 👇 para voltar ao menu!"
        )
        keyboard = [["🏠 Voltar ao Menu"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(resumo, reply_markup=reply_markup)
        user_data["quiz_mode"] = False


async def send_question(
    update: Update, context: ContextTypes.DEFAULT_TYPE, question: str
):
    if update.message:
        await update.message.reply_text(
            f"🧠 {question}\n\nResponda com a sua resposta!"
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            f"🧠 {question}\n\nResponda com a sua resposta!"
        )
