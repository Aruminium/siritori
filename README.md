# *Shiritori* program starting with word data collection

For those who want to play *Shiritori* [Click here](https://colab.research.google.com/drive/1nYIH_4tVyC2FjR6QUfMLu54MQzSM63GB?usp=sharing) (Go to google colab)

Those who want to build WEBAPI↓

### 1. download

```terminal
$ git clone https://github.com/Aruminium/siritori
$ cd siritori
```

### 2. build and run

```
$ docker compose build
$ docker compose up -d
```

### 3. Lets play

|Json Key|type|caution|
|:-|:-|:-|
|noun|string|Input only in hiragana|



```
$ curl localhost:5000/init
しりとり
$ curl -X POST -H "Content-Type: application/json" -d '{"noun": "りんご"}' http://localhost:5000/siritori
```
