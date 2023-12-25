# Лабораторная работа 3
## Цель работы:
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).
## Подготовка:
Для начала создадим репозиторий на github,куда загрузим все необходимые файлы. Для настройки GitHub Actiobs необходимо создать `yml` файл в директории `github/workflows/` 
[Репозиторий](https://github.com/Ludok1610/for_lab_3_DevOps)
## Создание github action
Внутри workflows сделаем файл Builder:
```
name: Builder

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: python:3.8

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Builder image
      run: docker build -t docker-image:latest .

    - name: Save Docker image as tar
      run: docker save -o docker-image.tar docker-image:latest

    - name: Upload Docker image
      uses: actions/upload-artifact@v2
      with:
        name: docker-image
        path: docker-image.tar
```
## Разберем код:
## Проверка:
Делаем пуш и проверим работает ли файл в репозитории на GitHub в разделе Actions. Видим, что файл успешно запустился:
![img1]()
![img2]()
Далее проверим наш образ в артефактах:
![img3]()
