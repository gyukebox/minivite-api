# Minivote API
API server for minivote

## 로컬 세팅

우선 코드를 다운로드 받으세요!

```
$ git clone https://github.com/gyukebox/minivote-api
```

### Dependencies

Minivote api 가 로컬에서 동작하기 위해서는 다음과 같은 dependency 들이 필요합니다.

- 파이썬 3
- 그 외 `requirements.txt` 에 나열되어 있는 모든 파이썬 패키지

따라서, 가상환경을 사용하시는 것을 추천드립니다. 가상환경을 만드시려면, `virtualenv` 패키지를 설치하시고 다음과 같은 명령어들을 입력해주시면 됩니다. (차례대로 설치, 생성, 활성화 입니다.)  

```
$ pip3 install virtualenv
$ python3 -m venv PATH/TO/ENV_NAME
$ source PATH/TO/ENV_NAME/bin/activate
```

`fish` 쉘을 사용하시는 분들은, 마지막 활성화 명령을

```
$ source PATH/TO/ENV_NAME/bin/activate.fish
```

다음과 같이 바꿔주시면 잘 동작합니다!

그 다음, 다음 명령어들로 dependency 들을 설치해주시면 됩니다.

```
$ pip install -r requirements.txt
```



## Documentation

[Wiki](https://github.com/gyukebox/minivote-api/wiki/Minivote-API-Documentation) 를 참조해 주세요!