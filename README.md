# Модуль фитнес-трекера <img src="https://filearchive.cnews.ru/img/book/2022/05/26/490-4906665_fitness-icon-png-emblem-clipart.png" width=32>

Реализация функционала фитнес-трекера на Python. Обработка данных с датчиков и возврат сообщений о пройденных тренировках.
Код задокументирован, реализованы аннотации типов данных (type hints).
Главная функция представляет собой чтение запрограммированных пакетов данных и вывод в консоль инфо сообщений о пройденных тренировках.

Проект разрабатывался на версии <b>Python 3.7</b> и для запуска потребуется установить все необходимые зависимости <b>requirements.txt</b>

Чтобы запустить проект локально:

1. Клонируйте репозиторий себе на компьютер, находясь в директории, откуда вы хотите в будущем запускать проект (в примере испоьзуется ссылка для подключения с помощью протокола SSH в консоли BASH для WINDOWS)

```BASH
git clone git@github.com:Ferdinand-I/fitness_tracker_oop.git
```

2. Создайте и активируйте виртуальное окружение (в примере используется утилита venv)

```BASH
python -m venv venv
source venv/Scripts/activate
```

3. Обновите PIP и установите зависимости requirements.txt

```BASH
python - m pip install --upgrade pip
pip install -r requirements.txt
```

4. Запустите проект 

```BASH
python homework.py
```
