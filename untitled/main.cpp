#include "mainwindow.h"

#include <QApplication>
#include <QSqlDatabase>
#include <QSqlError>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    // подключение к БД
    QApplication::addLibraryPath("C:\\Qt\\bin\\plugins\\sqldrivers");
    QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");

    db.setDatabaseName("postgres");
    db.setPort(5432);
    db.setHostName("localhost");
    db.setUserName("postgres");
    db.setPassword("123456");

    if (db.open()) {
        qDebug() << "Connected!";
    } else {
        qDebug() << "Error:" << db.lastError().text();
    }

    w.show();


    return a.exec();
}
