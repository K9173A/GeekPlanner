# GeekPlanner
[![Status](https://travis-ci.org/K9173A/GeekPlanner.svg?branch=andrei-dev)](https://travis-ci.org/K9173A/GeekPlanner)  
Простое и удобное приложение для заметок.
### Цель создания проекта
Данный проект создан в учебных целях - стабильность работы на текущем этапе не гарантируется! В будущем может быть
рассмотрен и коммерческий вариант его использования, если удастся достичь стадии относительной завершённости
функционала, стабильности при тестах и наличия инвесторов.
### Установка и запуск проекта
В качестве примера описан процесс утановки проекта на Ubuntu 18.04 LTS. При разработке был использован Python 3.6.
#### Установка требующиегося ПО
* Установить Python:
```
sudo apt-get install -y build-essential
sudo apt-get install -y checkinstall
sudo apt-get install -y libreadline-gplv2-dev
sudo apt-get install -y libncursesw5-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libsqlite3-dev
sudo apt-get install -y tk-dev
sudo apt-get install -y libgdbm-dev--ignore-fail
sudo apt-get install -y libc6-dev
sudo apt-get install -y libbz2-dev
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y openssl
sudo apt-get install -y libffi-dev
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-setuptools
sudo apt-get install -y wget
mkdir /tmp/Python37
cd /tmp/Python37
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xvf Python-3.7.0.tar.xz
cd /tmp/Python37/Python-3.7.0
./configure
sudo make altinstall
```
* Установить Git:
```
sudo apt-get install git
```
* Установить пакет, который отвечает за создание виртуального окружения. Важно не забыть
указать именно 3-ю версию, так как мы работаем с Python3!
```
sudo apt-get install python3-venv
```
* Установите PostgreSQL для работы с БД:
```
sudo apt-get install postgresql postgresql-contrib
```
#### Клонирование проекта и установке пакетов
* Запустите Git Bash и перейдите в директорию, в которой будет располагаться проект.
* Сделайте клон репозитория:
```
git clone https://github.com/K9173A/GeekPlanner
```
* Перейдите в корневой католог:
```
cd GeekPlanner
```
* Создайте виртуальное окружение для проекта и активируйте его.
```
python3 -m venv venv
source venv/bin/activate
```
* Установите все требующиеся пакеты в созданный `venv`:
```
pip install -r requirements.txt
```
#### Создание БД
* Проверьте работу PostgreSQL:
```
sudo systemctl status postgresql
```
* Если процесс в состоянии Active, то запустите инетрпретатор команд сервера:
```
sudo -u postgres psql
```
* Создайте БД. Сравните эти данные с данными, которые находятся в папке `settings` в файлах
`base.py`, `development.py` и `production.py`. В одном из них имеется переменная `DATABASES`, в которой
указаны данные БД. Они должны совпадать с тем, что будет вводиться в консоли!
```
/* Создание пустой БД */
CREATE DATABASE geekplanner;
/* Создание пользователя с паролем */
CREATE USER admin with PASSWORD 'admin';
/* Создание привилегий пользователя */
GRANT ALL PRIVILEGES ON DATABASE geekplanner TO admin;
/* Кодировка */
ALTER ROLE admin SET CLIENT_ENCODING TO 'UTF8';
/* Уровень изоляции транзакций */
ALTER ROLE admin SET default_transaction_isolation TO 'READ COMMITTED';
/* Временная зона */
ALTER ROLE admin SET TIME ZONE 'Europe/Moscow';
```
* Для выхода введите `\q`.
#### Алгоритм запуска
* Измените права доступа к скрипту для запуска сервера `run_server.sh`:
```
chmod u+x run_server.sh
```
* Варианты запуска сервера:
  * Development-сервер: `./run_server.sh development`
  * Production-сервер: `./run_server.sh production`