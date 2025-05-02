# 🤖 Projeto FURIA Bot  
## 🦁 Telegram Chatbot para Fãs da FURIA Esports

Um bot do Telegram criado especialmente para os fãs da equipe **FURIA Esports**, oferecendo uma experiência interativa, informativa e divertida diretamente no app de mensagens. Com comandos simples e botões intuitivos, você pode acompanhar jogos, conhecer os jogadores, receber lembretes, frases motivacionais, fazer quizzes e muito mais.

---

## 🎯 Propósito do Projeto

- Aproximar os fãs da FURIA do time em tempo real.
- Oferecer uma interface prática e envolvente via Telegram.
- Integrar funcionalidades relevantes do universo FURIA.
- Utilizar boas práticas com estrutura modular em Python e `python-telegram-bot`.
- Servir como referência para desenvolvedores de bots com múltiplos módulos.

---

## 🧰 Funcionalidades do Bot

| Funcionalidade         | Descrição |
|------------------------|-----------|
| 📅 **Próximos Jogos**   | Veja a agenda dos próximos confrontos da FURIA. |
| 📊 **Últimos Resultados** | Confira os placares e o desempenho recente da equipe. |
| 🎯 **Jogadores**         | Informações sobre o elenco atual da FURIA. |
| 🗣️ **Frases da Equipe**  | Frases motivacionais ditas por jogadores da FURIA. |
| 🔔 **Lembretes**         | Ative lembretes automáticos para os jogos. |
| 🔴 **Jogo ao Vivo**      | Veja o status de partidas em tempo real. |
| ❓ **Quiz Interativo**   | Responda perguntas sobre a FURIA. |
| 🛒 **Loja Oficial**      | Acesse a loja oficial da FURIA. |
| ℹ️ **Ajuda**             | Consulte instruções detalhadas sobre o uso do bot. |

---

## 📲 Exemplos de Uso

Inicie com `/start` e use os botões disponíveis, como:

- `📅 Próximos Jogos`
- `📊 Resultados`
- `🎯 Jogadores`
- `🗣️ Frases Marcantes`
- `🔥 Ao Vivo`
- `❓ Quiz`
- `⏰ Lembretes`
- `ℹ️ Ajuda`
- `🛒 Loja Oficial`

> Após o `/start`, a navegação acontece via botões inline para facilitar o uso.

---

## 📺 Descrição de Telas

### 📅 Tela de Próximos Jogos
Exibe os próximos confrontos da equipe com:
- Data e horário
- Nome do adversário
- Botão para ativar lembrete (opcional)

---

### 📊 Tela de Últimos Resultados
Mostra:
- Resultado das partidas recentes
- Placar, data e adversário
- Emojis indicando vitória ou derrota

---

### 🎯 Tela de Jogadores
Traz informações como:
- Nickname
- Função na equipe
- Curiosidades
- Habilidades

---

### 🗣️ Tela de Frases da Equipe
Frases motivacionais aleatórias ditas por membros da FURIA, com:
- Nome do autor
- Frase inspiradora

---

### 🛒 Tela da Loja Oficial
Oferece botões que direcionam para partes especificas do site.
- Bonés
- Camisas
- Moletons
- Link para Loja Completa

> 🛒 Acesse a loja oficial: [https://loja.furia.gg](https://loja.furia.gg)

---

### 🔔 Tela de Lembretes
Permite configurar lembretes automáticos com botões:
- Ativar lembrete
- Cancelar lembrete
- Visualizar lembrete

---

### 🔴 Tela de Jogo ao Vivo
Caso esteja ocorrendo um jogo, exibe:
- Nome das equipes
- Início da partida
- Placar ao vivo
- Status e tempo de jogo

---

### ❓ Tela de Quiz
Quiz interativo com:
- Perguntas
- Resposta imediata de acerto ou erro
- Resultado no final do quiz

---

### ℹ️ Tela de Ajuda
Ajuda textual com:
- Descrição de cada botão/tela
- Botão "Voltar ao Menu Principal"

---

## 📁 Estrutura do Projeto

```
furia_bot/
│
├── app/                      # Módulo principal do bot
│   ├── __init__.py
│   ├── main.py               # Ponto de entrada do bot
│   ├── config.py             # Configurações gerais
│   ├── handlers/             # Módulos com comandos
│   │   ├── start.py          # Comando de boas-vindas
│   │   ├── schedule.py       # Agenda de jogos
│   │   ├── results.py        # Últimos resultados
│   │   ├── players.py        # Informações dos jogadores
│   │   ├── quotes.py         # Frases famosas
│   │   ├── store.py          # Link da loja
│   │   ├── help.py           # Tela de ajuda
│   │   ├── menu_router.py    # Roteamento do menu
│   │   ├── live.py           # Jogo ao vivo
│   │   ├── reminder.py       # Lembretes
│   │   └── quiz.py           # Quiz interativo
├── .env                      # Variáveis de ambiente (NÃO subir ao GitHub)
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
└── run.py                    # Executa o bot localmente
```

---

## 🧭 Comandos Disponíveis

| Comando   | Descrição                                                                  |
|-----------|----------------------------------------------------------------------------|
| `/start`  | Inicia o bot e apresenta o menu principal com os botões interativos.       |
| `/help`   | Exibe a tela de ajuda com explicações sobre cada funcionalidade.           |

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- [python-telegram-bot (versão assíncrona)](https://github.com/python-telegram-bot/python-telegram-bot)
- asyncio
- Deploy: Railway, Heroku, VPS ou Docker
- Dependências extras em `requirements.txt`

---

## ⚙️ Como Rodar Localmente

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/furia-bot.git
cd furia-bot
```

2. **Crie e ative o ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate         # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure seu `.env`**

Crie um arquivo `.env` com o token do seu bot:

```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
```

5. **Execute o bot**

```bash
python run.py
```

---

## 🚀 Possibilidades Futuras

- Integração com API de eSports para resultados em tempo real.
- Ranking de usuários no quiz.
- Notificações push para novas coleções na loja.
- Suporte multilíngue.
- Painel web administrativo para gerenciar frases e perguntas.

---

## 🙌 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou novas funcionalidades.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).