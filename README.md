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

`fish`, `csh` 쉘을 사용하시는 분들은, 마지막 활성화 명령을

```
$ source PATH/TO/ENV_NAME/bin/activate.fish
# source PATH/TO/ENV_NAME/bin/activate.csh
```

다음과 같이 바꿔주시면 잘 동작합니다!

그 다음, 다음 명령어들로 dependency 들을 설치해주시면 됩니다.

```
$ cd minivote-api
$ pip install -r requirements.txt
```

### Authorization

Minivote api 는 authorization 을 필요로 하고, 이는 관리자 아이디/비밀번호 를 생성함으로써 이루어질 수 있습니다.  
다음 명령어로 관리자 아이디 및 비밀번호를 생성하시면 되겠습니다.

```
$ cd api
$ python manage.py createsuperuser
```

명령어를 입력하신 후에, 시키는 대로(아마 아이디, 이메일, 비밀번호를 입력하라고 나올거에요) 잘 따라 하시면 관리자 계정을 만드실 수 있습니다.

## Running the Server

다음 명령어로 서버를 실행시키세요

```
$ python manage.py runserver
```
그 후, http://127.0.0.1:8000 으로 접속하시면 됩니다!  
자세한 api 스펙은 [documentation](https://github.com/gyukebox/minivote-api/wiki/Minivote-API-Documentation) 에 친절하게 나와 있습니다.

Admin page 로 접속을 원하신다면, http://127.0.0.1:8000/admin 으로 접속하시면 됩니다.

## Documentation

[Wiki](https://github.com/gyukebox/minivote-api/wiki/Minivote-API-Documentation) 를 참조해 주세요!
