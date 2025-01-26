import telebot

BOT_TOKEN = "7568478589:AAFcwo-CNP9eZU9Gky980s6cL0PkmKr8rKo"
CHAT_ID = -1002366546230  # Убедитесь, что это правильный ID чата

# Инициализация синхронного бота
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Отправляет данные о рейсах в Telegram, накапливая сообщения до лимита в 4096 символов
def send_to_telegram(flights):
    message_buffer = ""  # Буфер для накопления сообщений
    message_limit = 4096  # Лимит длины сообщения Telegram (4096 символов)

    for flight in flights:
        # Формируем сообщение для одного рейса
        flight_message = (
            f"Aircraft: {flight['aircraft']}\n"
            f"Registration: {flight['registration']}\n"
            f"Altitude: {flight['altitude']}\n"
            f"Ground Speed: {flight['ground_speed']}\n"
            f"Heading: {flight['heading']}\n\n"
        )

        # Проверяем, поместится ли новое сообщение в буфер
        if len(message_buffer) + len(flight_message) > message_limit - 10:
            # Отправляем накопленный буфер, если лимит превышен
            bot.send_message(CHAT_ID, message_buffer)
            print(f"Сообщение отправлено:\n{message_buffer}")
            message_buffer = ""  # Очищаем буфер

        # Добавляем сообщение в буфер
        message_buffer += flight_message

    # Отправляем оставшийся буфер, если он не пуст
    if message_buffer:
        bot.send_message(CHAT_ID, message_buffer)
        print(f"Сообщение отправлено:\n{message_buffer}")