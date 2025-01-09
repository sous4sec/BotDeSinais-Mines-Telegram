# BotDeSinais-Mines-Telegram

Bem-vindo ao **BotDeSinais-Mines-Telegram**! 🤖✨

Este projeto implementa um bot para o Telegram que envia sinais de apostas no estilo *minesweeper*, ideal para plataformas de cassino online. Acompanhe sinais ao vivo, receba notificações de "Green" (sucesso) e interaja com tabuleiros dinâmicos diretamente no Telegram!

---

## 🚀 Funcionalidades

- **Sinais automatizados:** Captura, analisa e envia sinais em tempo real.
- **Tabuleiros interativos:** Mensagens com tabuleiros do jogo, simulando uma experiência única.
- **Atualizações em tempo real:** Cronômetro dinâmico com validade de 5 minutos.
- **Rankings personalizados:** Exibe os melhores apostadores com nomes e valores gerados aleatoriamente.
- **Integração com links:** Botões clicáveis para acessar plataformas autorizadas.

---

## 📋 Pré-requisitos

Antes de começar, você precisará:

1. **Python 3.7 ou superior** instalado no seu ambiente.
2. Uma conta de bot no Telegram e o **Token do Bot** (obtenha em [BotFather](https://t.me/botfather)).
3. O **ID do Grupo ou Chat** onde o bot irá operar.
4. Instale as bibliotecas necessárias:
   ```bash
   pip install pytelegrambotapi
   ```

---

## 🚧 Instalação

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/sous4sec/BotDeSinais-Mines-Telegram.git
   cd BotDeSinais-Mines-Telegram
   ```

2. **Configure o bot:**
   - Abra o arquivo `bot.py`.
   - Substitua `API_TOKEN` pelo Token do Bot.
   - Substitua `CHAT_ID` pelo ID do seu grupo ou chat.

3. **Adicione sua imagem personalizada:**
   - Substitua o arquivo `img.png` pelo seu tabuleiro de jogo personalizado.

4. **Execute o bot:**
   ```bash
   python bot.py
   ```

---

## 📝 Uso

Após iniciar o bot, ele executará automaticamente um ciclo contínuo de envio de sinais:

1. **Aguarde o sinal:**
   O bot enviará uma mensagem inicial indicando que o sinal está sendo preparado.

2. **Sinal capturado:**
   Uma mensagem com o tabuleiro do jogo e o cronômetro será enviada, incluindo as tentativas e minas ativadas.

3. **Resultado:**
   Quando o cronômetro expirar, o bot notificará o sucesso (*Green*) e exibirá o ranking.

### Exemplo de fluxo:

1. `🔵 SINAL EM PREPARAÇÃO!`
2. `📡 SINAL CAPTURADO!`
3. Envio do tabuleiro com cronômetro dinâmico.
4. `🟢 GREEN DETECTADO!`
5. Exibição do ranking de apostas.

### Capturas de Tela 📸

Adicione imagens para demonstrar o funcionamento do bot:

- Mensagem inicial:
  ![Sinal em Preparação](images/sinal_preparacao.png)

- Tabuleiro interativo:
  ![Tabuleiro Capturado](images/tabuleiro_capturado.png)

- Resultado Green:
  ![Green Detectado](images/green_detectado.png)

Crie uma pasta `images/` no repositório e insira as imagens para garantir que sejam exibidas corretamente.

---

## 🛠️ Personalização

Você pode modificar o comportamento do bot:

- Alterando os **delays** no início do código.
- Ajustando os nomes e valores gerados aleatoriamente no ranking.
- Modificando o tamanho do tabuleiro e o número de estrelas com a função `criar_tabuleiro`.

---

## 💡 Contribuições

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Faça suas alterações e adicione commits:
   ```bash
   git commit -m 'Nova funcionalidade adicionada'
   ```
4. Envie as alterações para sua fork:
   ```bash
   git push origin minha-contribuicao
   ```
5. Abra um **Pull Request** para o repositório principal.

---

## 📜 Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📧 Contato

Este projeto foi criado por um estudante apaixonado por programação e automação. Para dúvidas ou sugestões, entre em contato pelo GitHub: [sous4sec](https://github.com/sous4sec)

---

Agradecemos por usar o **BotDeSinais-Mines-Telegram**! 🚀💼 Que seus sinais sejam sempre *Green*! 🟢

