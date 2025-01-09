import telebot
import random
import time
import threading
from telebot import types
from dotenv import load_dotenv
import os

# Carregar configurações sensíveis de um arquivo .env
load_dotenv()

# Configurações do bot (defina estas variáveis no arquivo .env)
API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
CAMINHO_IMAGEM = os.getenv('CAMINHO_IMAGEM', 'caminho_da_imagem.png')

# Links de plataformas autorizadas
links = {
    "Plataforma 1": os.getenv('PLATAFORMA_1_URL', 'https://exemplo1.com'),
    "Plataforma 2": os.getenv('PLATAFORMA_2_URL', 'https://exemplo2.com')
}

# Configurações de delay (em segundos)
DELAY_SINAL_EM_BREVE = int(os.getenv('DELAY_SINAL_EM_BREVE', 1))
DELAY_SINAL_CAPTURADO = int(os.getenv('DELAY_SINAL_CAPTURADO', 10))
DELAY_ENVIO_TABULEIRO = int(os.getenv('DELAY_ENVIO_TABULEIRO', 300))
DELAY_ENVIO_GREEN = int(os.getenv('DELAY_ENVIO_GREEN', 10))
DELAY_ENVIO_RANKING = int(os.getenv('DELAY_ENVIO_RANKING', 10))

# Configurações adicionais
MIN_BOMBAS = int(os.getenv('MIN_BOMBAS', 1))
MAX_BOMBAS = int(os.getenv('MAX_BOMBAS', 4))
MIN_ESTRELAS = int(os.getenv('MIN_ESTRELAS', 2))
MAX_ESTRELAS = int(os.getenv('MAX_ESTRELAS', 4))
MIN_VALOR = int(os.getenv('MIN_VALOR', 100))
MAX_VALOR = int(os.getenv('MAX_VALOR', 3000))
MIN_PORCENTAGEM = int(os.getenv('MIN_PORCENTAGEM', 65))
MAX_PORCENTAGEM = int(os.getenv('MAX_PORCENTAGEM', 90))

# Inicialização do bot
bot = telebot.TeleBot(API_TOKEN)

# Função para gerar nomes aleatórios
def gerar_nome():
    prefixos = ["Ana", "João", "Lucas", "Beatriz", "Maria", "Pedro", "Isabela", "Rafael", "Carla", "Victor"]
    sufixos = ["Silva", "Souza", "Oliveira", "Pereira", "Costa", "Alves", "Gomes", "Martins", "Barros", "Ferreira"]
    return random.choice(prefixos) + " " + random.choice(sufixos)

# Função para gerar valores aleatórios
def gerar_valor():
    return random.randint(MIN_VALOR, MAX_VALOR)

# Função para gerar uma porcentagem aleatória
def gerar_porcentagem():
    return random.randint(MIN_PORCENTAGEM, MAX_PORCENTAGEM)

# Função para criar o tabuleiro
def criar_tabuleiro(tamanho=5, num_casas_sorteadas=None):
    if num_casas_sorteadas is None:
        num_casas_sorteadas = random.randint(MIN_ESTRELAS, MAX_ESTRELAS)

    tabuleiro = [["🟦" for _ in range(tamanho)] for _ in range(tamanho)]
    coordenadas_sorteadas = random.sample(
        [(x, y) for x in range(tamanho) for y in range(tamanho)],
        num_casas_sorteadas
    )
    for x, y in coordenadas_sorteadas:
        tabuleiro[x][y] = "⭐"
    return tabuleiro, num_casas_sorteadas

def formatar_tabuleiro(tabuleiro):
    return "\n".join("".join(linha) for linha in tabuleiro)

# Função para atualizar o cronômetro na mensagem
def atualizar_cronometro(chat_id, message_id, tabuleiro_formatado, tempo_restante, markup):
    mensagem_anterior = None
    while tempo_restante > 0:
        minutos, segundos = divmod(tempo_restante, 60)
        novo_conteudo = (
            f"🟦 *NOME_DO_SEU_BOT* 🟦\n"
            f"-------------------------------------\n"
            f"⚡ - *Tentativas Restantes*: 5\n"
            f"💣 - *Minas Ativadas*: 2\n"
            f"⏰ - *Validade*: 5:00 minutos\n\n"
            f"{tabuleiro_formatado}\n\n"
            f"-------------------------------------\n"
            f"🔵 *OS SINAIS FUNCIONAM APENAS NA PLATAFORMA ABAIXO!*\n"
        )

        cronometro_formatado = f"```\n🕒 {minutos:02d}:{segundos:02d} restantes\n```"
        novo_conteudo_com_timestamp = f"{novo_conteudo}\n\n{cronometro_formatado}"

        if mensagem_anterior != novo_conteudo_com_timestamp:
            try:
                bot.edit_message_caption(
                    chat_id=chat_id,
                    message_id=message_id,
                    caption=novo_conteudo_com_timestamp,
                    reply_markup=markup,
                    parse_mode="Markdown"
                )
                mensagem_anterior = novo_conteudo_com_timestamp
                time.sleep(15)
                tempo_restante -= 15
            except Exception as e:
                print(f"Erro ao atualizar cronômetro: {e}")
                break

    bot.edit_message_caption(
        chat_id=chat_id,
        message_id=message_id,
        caption="⏳ *TEMPO ESGOTADO - ESPERE O PRÓXIMO SINAL!*",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# Função principal de envio de sinais
def enviar_sinal():
    bot.send_message(
        CHAT_ID, 
        "🔵 - `SINAL EM PREPARAÇÃO!`\n\n"
        "```🔺Aguarde... Um novo sinal está sendo capturado.```\n", 
        parse_mode="Markdown"
    )
    time.sleep(DELAY_SINAL_EM_BREVE)

    tabuleiro, num_casas_sorteadas = criar_tabuleiro()
    tabuleiro_formatado = formatar_tabuleiro(tabuleiro)
    ranking = gerar_ranking()
    porcentagem_vitoria = gerar_porcentagem()

    if num_casas_sorteadas == 2:
        tentativas = random.randint(8, 10)
        minas = random.randint(MIN_BOMBAS, MIN_BOMBAS + 1)
    elif num_casas_sorteadas == 3:
        tentativas = random.randint(5, 7)
        minas = random.randint(MIN_BOMBAS + 1, MIN_BOMBAS + 2)
    else:
        tentativas = random.randint(3, 5)
        minas = random.randint(MIN_BOMBAS + 2, MAX_BOMBAS)

    bot.send_message(
        CHAT_ID, 
        "📡 - `SINAL CAPTURADO!`\n\n"
        "```🔹Confira! O tabuleiro será gerado abaixo.```\n", 
        parse_mode="Markdown"
    )
    time.sleep(DELAY_SINAL_CAPTURADO)

    markup_tabuleiro = types.InlineKeyboardMarkup()
    markup_tabuleiro.add(types.InlineKeyboardButton("🌐 Acessar Plataforma", url=links["Plataforma 1"]))

    with open(CAMINHO_IMAGEM, 'rb') as img:
        mensagem = bot.send_photo(
            CHAT_ID,
            img,
            caption=( 
                f"🔒 *NOME_DO_SEU_BOT* 🔒\n"
                f"-------------------------------------\n"
                f"⚡ - *Tentativas*: {tentativas}\n"
                f"💣 - *Minas Ativadas*: {minas}\n"
                f"⏰ - *Validade*: 5:00 minutos\n\n"
                f"{tabuleiro_formatado}\n\n"
                f"-------------------------------------\n"
                f"🔵 *LUCRE SOMENTE NAS PLATAFORMAS AUTORIZADAS!*\n"
            ),
            parse_mode="Markdown",
            reply_markup=markup_tabuleiro
        )

    threading.Thread(
        target=atualizar_cronometro,
        args=(CHAT_ID, mensagem.message_id, tabuleiro_formatado, 300, markup_tabuleiro),
        daemon=True
    ).start()

    time.sleep(DELAY_ENVIO_TABULEIRO)

    bot.send_message(
        CHAT_ID,
        "🟢 *GREEN DETECTADO!* 🟢\n"
        "-------------------------------------\n"
        "🎉 *Parabéns! A aposta foi um sucesso.*\n"
        "Continue acompanhando nossos sinais exclusivos e maximize seus lucros! 💰\n"
        "-------------------------------------\n",
        parse_mode="Markdown"
    )
    time.sleep(DELAY_ENVIO_GREEN)

    markup_ranking = types.InlineKeyboardMarkup()
    markup_ranking.add(types.InlineKeyboardButton("🌐 Lucre Agora!", url=links["Plataforma 2"]))

    bot.send_message(
        CHAT_ID,
        f"🏆 *RANKING DE VITÓRIAS!* 🏆\n"
        f"-------------------------------------\n"
        f"📊 *{porcentagem_vitoria}% dos apostadores tiveram sucesso!*\n\n"
        f"{ranking}\n"
        f"-------------------------------------\n",
        parse_mode="Markdown",
        reply_markup=markup_ranking
    )
    time.sleep(DELAY_ENVIO_RANKING)

# Função para gerar ranking aleatório
def gerar_ranking():
    ranking = [(gerar_nome(), gerar_valor()) for _ in range(7)]
    ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)
    return "\n".join([f"*{i+1}º:* {nome} - `R$ {valor}`" for i, (nome, valor) in enumerate(ranking_ordenado)])

# Loop para envio automático
def ciclo_sinais():
    while True:
        try:
            enviar_sinal()
        except Exception as e:
            print(f"Erro no envio de sinais: {e}")
            time.sleep(10)

# Iniciar o bot
if __name__ == "__main__":
    thread = threading.Thread(target=ciclo_sinais, daemon=True)
    thread.start()
    bot.polling()
