# Автотест API заказов

## Что делает проект

* Создаёт заказ через API
* Получает заказ по треку
* Проверяет, что код ответа — 200 и заказ найден

## Как запустить

1. Установи зависимости:

```bash
pip install requests
```

2. Укажи базовый URL вручную в файле `configuration.py`, например:

```python
URL_SERVICE = "https://<твой-адрес>.serverhub.praktikum-services.ru"
```

3. Запусти тест:

```bash
python3 order_test.py
```

## Структура проекта

* `order_test.py` — основной автотест
* `sender_stand_request.py` — функции для запросов
* `configuration.py` — базовые настройки
* `.gitignore` — игнорируемые файлы
