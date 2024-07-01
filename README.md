# Виджет финансовых операций
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. 
Это виджет, который показывает несколько последних успешных банковских 
операций клиента. 

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/VasyaAndSova/homework.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Проверьте свои банковские операции.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

## Тестирование:

В pytest для анализа покрытия кода надо поставить библиотеку pytest-cov:
``` 
poetry add --group dev pytest-cov
```

Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:
1. при активированном виртуальном окружении:
```
pytest --cov
```
2. через poetry:
``` 
poetry run pytest --cov
```
3. чтобы сгенерировать отчет о покрытии в HTML-формате, 
где src — пакет c модулями, которые тестируем. Отчет будет сгенерирован 
в папке htmlcov и храниться в файле с названием index.html:
```
pytest --cov=src --cov-report=html
```

## Генераторы:
В проекте была выполнена задача по реализации генераторов 
для обработки массивов транзакций. Эти генераторы должны позволять 
финансовым аналитикам быстро и удобно находить нужную информацию о 
транзакциях и проводить анализ данных.

## Декораторы:

В проекте был написан декоратор ``` log ```, который будет логировать вызов 
функций-обработчиков и результаты их работы. Это поможет отслеживать работу 
системы и быстро реагировать на возможные ошибки.