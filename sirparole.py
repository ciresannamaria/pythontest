import telebot

# создаем объект бота
bot = telebot.TeleBot("ваш_токен")

# обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот! Чем могу помочь?")

# обработчик сообщения "Привет"
@bot.message_handler(func=lambda message: message.text == "Привет")
    def send_hello(message):
    bot.reply_to(message, "Привет!")

# обработчик сообщения "Пока"
    @bot.message_handler(func=lambda message: message.text == "Пока")
    def send_goodbye(message):
    bot.reply_to(message, "Пока!")

# запускаем бота
    bot.polling()
