- В папке "serv" находится сервер Flask. 
Запускается в командной строке: python fly_radar_locale.py
Сервер доступен по локальному адресу.
На странице http://127.0.0.1/ - приветственное сообщение
На странице http://127.0.0.1/fetch - загрузка данных с flightradar24; занесение данных в БД; отправка писем в телеграмм группу; оттадача данных в формате JSON.

- Чтобы увидеть данные в группе в телеграмме, нужно быть в неё добавленным. 
- Чтобы происходила запись в БД необходимо отредактировать доступы в файле "db.py"

- В папке "untitled" находиться QT проект, с одной формой и виджетом QListWidget. 
При запуске программы происходит запрос на страницу сервер "http://127.0.0.1/fetch".
Полученные данные парсятся и выводят в виджет QListWidget.
