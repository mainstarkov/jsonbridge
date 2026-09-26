# JSON Bridge

Конвертирует массивы объектов JSON в CSV и таблицы CSV обратно в JSON. Работает локально и не отправляет данные в интернет.

```bash
python3 jsonbridge.py data.json data.csv
python3 jsonbridge.py data.csv data.json
```

Поддерживает UTF-8, объединяет все встреченные поля и использует только стандартную библиотеку Python.

