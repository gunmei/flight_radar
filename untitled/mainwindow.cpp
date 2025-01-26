#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QTimer>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    // Инициализация QNetworkAccessManager
    networkManager = new QNetworkAccessManager(this);

    // Соединяем сигнал завершения запроса с обработчиком
    connect(networkManager, &QNetworkAccessManager::finished, this, &MainWindow::onResponseReceived);

    // Запускаем запрос данных
    fetchFlightData();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::fetchFlightData() {
    QNetworkRequest request(QUrl("http://127.0.0.1:5000/fetch")); // URL Flask-сервера
    networkManager->get(request); // GET-запрос
}

void MainWindow::onResponseReceived(QNetworkReply *reply) {
    if (reply->error() != QNetworkReply::NoError) {
        qDebug() << "Ошибка запроса: " << reply->errorString();
        return;
    }

    // Парсим JSON-ответ
    QByteArray responseData = reply->readAll();
    QJsonDocument jsonDoc = QJsonDocument::fromJson(responseData);

    if (jsonDoc.isArray()) {
        QJsonArray jsonArray = jsonDoc.array();

        // Очищаем список перед добавлением новых данных
        ui->listWidget->clear();

        for (const QJsonValue &value : jsonArray) {
            if (value.isObject()) {
                QJsonObject flight = value.toObject();
                QString aircraft = flight["aircraft"].toString();
                QString registration = flight["registration"].toString();
                QString altitude = flight["altitude"].toString();
                QString groundSpeed = flight["ground_speed"].toString();
                QString heading = flight["heading"].toString();

                // Формируем строку и добавляем в список
                QString flightInfo = QString("Aircraft: %1, Registration: %2, Altitude: %3, Ground Speed: %4, Heading: %5")
                                         .arg(aircraft)
                                         .arg(registration)
                                         .arg(altitude)
                                         .arg(groundSpeed)
                                         .arg(heading);

                ui->listWidget->addItem(flightInfo);
            }
        }
    }
}
