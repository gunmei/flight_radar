#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QListWidget>
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include <QDebug>


QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void fetchFlightData();              // Метод для запроса данных
    void onResponseReceived(QNetworkReply *reply); // Обработка ответа от сервера

private:
    Ui::MainWindow *ui;
    QNetworkAccessManager *networkManager; // Менеджер HTTP-запросов
};
#endif // MAINWINDOW_H
