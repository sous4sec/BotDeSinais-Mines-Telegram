# Bot de Sinais Mines para Telegram

Bem-vindo ao **Bot de Sinais Mines para Telegram**! Este é um projeto divertido e desafiador criado por um estudante de programação. O bot envia sinais automáticos para um grupo do Telegram com um tabuleiro interativo, rankings de apostadores e mensagens personalizadas. Perfeito para aprender sobre bots e automação!

## 🚀 Recursos Principais

- **Envio Automático de Sinais**: O bot cria e envia sinais com um tabuleiro estilo "mines".
- **Cronômetro Interativo**: Atualizações em tempo real do cronômetro na mensagem do Telegram.
- **Mensagens Personalizadas**: Inclui rankings e resultados das apostas.
- **Configurações Flexíveis**: Ajuste delays, configurações do tabuleiro e mais no arquivo `.env`.

---

## 🛠️ Pré-requisitos

Antes de começar, você precisa de:

- **Python 3.8+**
- **Conta de Bot no Telegram**: Crie um bot usando o [BotFather](https://core.telegram.org/bots#botfather) e obtenha o token.
- **ID do Chat/Grupo**: Você pode obter isso ao adicionar o bot no grupo e usar ferramentas como [RawDataBot](https://t.me/RawDataBot).

---

## ⚙️ Configurando o Projeto

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/sous4sec/BotDeSinais-Mines-Telegram.git
   cd BotDeSinais-Mines-Telegram
   ```

2. **Instale as Dependências**:

   Certifique-se de ter o `pip` configurado:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o Arquivo `.env`**:

   Crie um arquivo `.env` na raiz do projeto e preencha com suas configurações:

   ```env
   # Configurações sensíveis para o bot
   API_TOKEN=seu_api_token_aqui
   CHAT_ID=seu_chat_id_aqui

   # Caminho para imagem a ser enviada
   CAMINHO_IMAGEM=img.png

   # URLs das plataformas autorizadas
   PLATAFORMA_1_URL=https://exemplo1.com
   PLATAFORMA_2_URL=https://exemplo2.com

   # Configurações de delay (em segundos)
   DELAY_SINAL_EM_BREVE=1
   DELAY_SINAL_CAPTURADO=10
   DELAY_ENVIO_TABULEIRO=300
   DELAY_ENVIO_GREEN=10
   DELAY_ENVIO_RANKING=10

   # Configurações de tabuleiro e apostas
   MIN_BOMBAS=1
   MAX_BOMBAS=4
   MIN_ESTRELAS=2
   MAX_ESTRELAS=4
   MIN_VALOR=100
   MAX_VALOR=3000
   MIN_PORCENTAGEM=65
   MAX_PORCENTAGEM=90
   ```

4. **Execute o Bot**:

   Inicie o bot com o comando:

   ```bash
   python bot.py
   ```

---

## 🌟 Como Funciona

1. **Sinal em Preparação**:
   - O bot envia uma mensagem inicial informando que o sinal será capturado.
2. **Tabuleiro Gerado**:
   - Um tabuleiro estilo "mines" é enviado com um cronômetro de 5 minutos.
3. **Resultado Green**:
   - Após o tempo, o bot envia mensagens comemorativas com resultados positivos!
4. **Ranking Dinâmico**:
   - Rankings aleatórios de apostadores são enviados com base em nomes e valores simulados.

---

## 📸 Exemplos de Imagens

- **Mensagem Inicial**:

  ![Mensagem Inicial](https://github.com/user-attachments/assets/2e40bde2-a0bf-4836-86f4-cf158f0cb7f6)


- **Tabuleiro Gerado**:

  ![Tabuleiro Gerado](https://github.com/user-attachments/assets/3c0e9491-d24c-4020-953d-32e60b169b38)


- **Rank Gerado**:

  ![Rank Gerado](https://github.com/user-attachments/assets/3a7fc764-9c68-45ed-933c-bf2deebae299)


- **Mensagem Green**:

  ![Mensagem Green](https://github.com/user-attachments/assets/566b3263-6630-43de-ad53-ddf43a1df9dd)



---

## 🔧 Personalização

- **Configurações no `.env`**:
  - Ajuste os delays, limites de apostas e configurações do tabuleiro de acordo com sua preferência.
- **Texto e Mensagens**:
  - Modifique as mensagens no arquivo `bot.py` para personalizar o estilo do bot.

---

## 🚨 Observações

- Este projeto é apenas para fins de aprendizado e diversão.
- Não use para fins maliciosos ou fora de grupos autorizados.

---

## 💬 Dúvidas?

Entre em contato pelo Telegram ou abra uma [issue](https://github.com/sous4sec/BotDeSinais-Mines-Telegram/issues).

---

Divirta-se explorando este projeto! 😄

