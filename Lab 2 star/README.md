# Лабораторная работа 2*
## Цель работы:
Запустить Kuberneter  кластер. Запустить контейнер внутри кластера.
## Ход работы:
Работа выполнялась на Virtual Box c  Ubuntu 22.04. 
### Для начала установим kubetcl:
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
### Установка minikube:
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
sudo mv minikube /usr/local/bin/
```
### Запускаем minikube:
```
minikube start --driver=docker
```
После запуска можно проверить ip кластера
![img1](https://github.com/amkutsak/cloud_technologies/blob/main/Lab%202%20star/images/img1.png)
## Работа с кластером
### Docker:
Для развертывания сервиса была выбрана стартовач страница Nginx. Для этого необходимо создать файл конфигурации yml-формата.
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      components: cloud-lab2
  template:
    metadata:
      labels:
        components: cloud-lab2
    spec:
      containers:
        - name: nginx-server
          image: nginx
          imagePullPolicy: Always
          ports:
            - containerPort: 80

---

apiVersion: v1
kind: Service
metadata:
  name: amkutsak/my-python-app-goop:latest
spec:
  type: NodePort
  ports:
    - port: 3000
      targetPort: 80
      nodePort: 31200
  selector:
    components: lab2
```
Запуск файла конфигурации `kubectl apply -f file.yml`
![img2](https://github.com/amkutsak/cloud_technologies/blob/main/Lab%202%20star/images/img2.png)
### Проверка
1. Проверяем запущенные сервисы `kubectl get services`, на которых видимо порты нашего сервиса
2. Проверяем статусы подов `kubectl get pods`
### Вывод результатов
C помощью команды: `mimkube service boba --url` получаем адресс нашей страницы
![img5](https://github.com/amkutsak/cloud_technologies/blob/main/Lab%202%20star/images/img5.png)
Открываем страницу сервиса по адресу, который мы получили: 
![img6](https://github.com/amkutsak/cloud_technologies/blob/main/Lab%202%20star/images/img6.png)

## Вывод
В результате выполнения работ изучили кластеры kubectl и mimkube для написания развертывания сервисов. Изучена платформа контейнерезации Kubernetes.
