# Лабораторная работа 3
## Цель работы:
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).
## Подготовка:
Для начала создадим репозиторий на github,куда загрузим все необходимые файлы. Для настройки GitHub Actiobs необходимо создать `yml` файл в директории `github/workflows/`  
[Репозиторий](https://github.com/Ludok1610/for_lab_3_DevOps)
## Создание github action
Внутри workflows сделаем файл Builder:
```
name: Docker Build

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

    - name: Docker Build image
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
```
on:
  push:
    branches:
      - main
```
`on` : определяет события, при которых будет выполняться workflow. В данном случае запускается при каждом пуше.  
`jobs`: определяет список действий, которые должны выполниться в рамках workflow. В нашем случае у нас есть одно действие: `bild`  
`runs on`: указывает на операционную систему, в которой выполняется наш job.  
`steps`: определяет последовательность шагов, которые выполняются внутри действий.  
```
    steps:
    - name: Checkout repository #шаг, который использует дейтсвие
      uses: actions/checkout@v2 #клонирование рабочего репозитория

    - name: Docker Build image #шаг для сборки докер образа
      run: docker build -t docker-image:latest . 

    - name: Save Docker image as tar #шаг для сохранения докер образа
      run: docker save -o docker-image.tar docker-image:latest #команда для сохранения

    - name: Upload Docker image
      uses: actions/upload-artifact@v2 #загрузка архива докер образа в качестве артефакта
```
`with`: имя артефакта и путь к архиву, куда загружать.

## Проверка:
Делаем пуш и проверим работает ли файл в репозитории на GitHub в разделе Actions. Видим, что файл успешно запустился:
![img1](https://github.com/amkutsak/cloud_technologies/blob/main/Lab3/images/1.jpg)
Можем просмотреть все этапы сборки, все прошло успешно.
![img2](https://github.com/amkutsak/cloud_technologies/blob/main/Lab3/images/2.jpg)
Далее проверим наш образ в артефактах:
![img3](https://github.com/amkutsak/cloud_technologies/blob/main/Lab3/images/3.jpg)

## Вывод:
С помощью github actions была настроена автоматическую сборку и выгрузку docker образа в артефакты.
