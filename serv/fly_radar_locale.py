from flask import Flask, jsonify
from fetch_flights import get_flights
from db import save_to_db
from telegram_bot import send_to_telegram

app = Flask(__name__)

@app.route("/")
def hello():
    return "Здравствуйте, здесь можно получить данные о китайских самолетах, находящихся в воздухе."

# Маршрут для проверки получения данных вручную
@app.route('/fetch', methods=['GET'])
def fetch():
    data = get_flights()    # получение с flightradar24
    save_to_db(data)        # сохранение в БД
    send_to_telegram(data) # отправка писем в телеграмм
    print("Данные логируются в консоль:", data)

    if data:
        return jsonify(data)
    return jsonify({"error": "Не удалось получить данные"}), 500
    

if __name__ == "__main__":
    app.run()
    