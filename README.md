# Сервис поиска

## Описание

Сервис отвечает за работу с публикациями.

## Python

```3.9.13```

## Настрока

1. ``` make setup ```
2. Скопировать и переименовать файл ```.env.example``` -> ```.env```. В файле ```.env``` сконфигурировать переменные окружения

## Запуск

``` make run ```

## Запуск тестов

``` make test ```

## Swagger API

После запуска проект swagger документацию можно посмотреть по адресу
``` /api/openapi ```

## Разработка в pycharm

Чтобы отображать линтинг flake8 в режиме реального времени необходимо
проследовать инструкции <https://tirinox.ru/flake8-pycharm/>.
На шаге 4 выбираем ```Severity: Warning```

Чтобы отображать линтинг mypy необходимо установить плагин
<https://plugins.jetbrains.com/plugin/11086-mypy> и перезапустить pycharm.
