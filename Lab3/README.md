# Лабораторная работа 3
## Цель работы:
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).
## Создание github action
```
name: Docker Image CI

on: 
  push:
    branches:
      - 'main'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repository
        uses: actions/checkout@v4
      
      - name: log in to docker hub 
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.LOGIN_DOCKER }}
          password: ${{ secrets.TOKEN_DOCKER }}

      - name: build image and push
        uses: docker/build-push-action@v5
        with:
          context: ./lab3
          push: true
          tags: cloud_technologies/docker3:latest
```
