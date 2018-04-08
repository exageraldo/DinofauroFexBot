# DinofauroFexBot
O _Dinofauro Fex_ é um meme brasileiro bastante conhecido. É um personagem de plástico, na qual veio com um "defeito" de fabricação: com a parte de baixo da boca voltada para dentro. Com isso, veio a brincadeira de imaginar como esse dinossauro falaria, e a ideia é mais ou menos assim:

> **Texto normal**: Estou muito bem, e você?
> **Dinossauro**: Eftou muito bem, e focê?

Então, em linhas gerais, a ideia do bot é "traduzir" os textos para _dinofaurês_.

## O Bot

O bot funciona de duas maneiras:

- **Modo eco**: Tudo que for enviado em formato de mensagem de texto para ele, será traduzido e enviado de volta para o usuário. Caso tenha mais de uma possibilidade de tradução (com um ou fois **f's**), será enviado as duas.
- **Modo inline**: Ao chamar o bot dentro da conversa (@DinofauroFexBot), você digita a mensagem em seguida e vai aparecer os botões para tradução (1F ou +F). Ao selecionar, a mensagem será enviada para o chat.

Além das funcionalidades de tradução, tem também outra opção, que é o **Lorem Ipsum** em dinofaurês. Ao digitar o comando **/ipsum**, no chat do bot, será retornado uma mensagem aleatória, entre 1 e 6 parágrafos para popular campos te textos. Ao clicar no botão da mensagem, irá gerar outra mensagem nas mesmas condições.

Os outros comandos disponíveis são:

- **/start**: É utilizado para iniciar a conversa com o bot.
- **/about**: Traz mais informações sobre o bot e sobre os desenvolvedores.
- **/help**: Traz informações de como usar cada comando do bot.
- **/feedback**: Envia uma avaliação (1 à 5 estrelas) para os desenvolvedores (permitido um feedback por mês).

## Desenvolvimento

Tecnologias usadas para o desenvolvimento do bot:
- Python 3.6 
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- MongoDB