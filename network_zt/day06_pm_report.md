# Day 6 Docker ① · nginx 서버 · 오후 (이름 · 2026-10-19)

> **쓰는 법**
> - 문제를 하나 풀 때마다 그 문제 제목 아래를 채웁니다.
> - 질문마다 `쓸 내용:` 에 **무엇을 쓰면 되는지** 적혀 있습니다. 그 내용대로 `답:` 뒤에 씁니다.
> - 「왜 그럴까요?」 같은 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 그 교시에 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다.

---

## 5교시 · 왜 도커인가 · 이미지와 컨테이너 · 같이 설치하기

### 문제 5-1 · 설치를 확인하고 첫 컨테이너 실행하기

- (가) `docker --version` 으로 나온 값을 적어 주세요.
  - 쓸 내용: 「Docker version … build …」 한 줄
  - 답:Docker version 29.8.2, build 7fc2dff
- (나) 🔍 `docker run hello-world` 출력이 말하는 일의 순서를 5.5 그림의 번호(① ~ ④)에 맞춰 설명해 주세요.
  - 쓸 내용: ① ~ ④ 번호마다 한 일 (클라이언트 · 엔진 · Docker Hub · 컨테이너)
  - 답:
  To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
- (다) 🔍 `docker images` 에 보인 것과 `docker ps -a` 에 보인 것은 각각 이미지와 컨테이너 중 무엇이고, 어떻게 다른가요?
  - 쓸 내용: ① images 에 보인 것과 그 종류 ② ps -a 에 보인 것과 그 종류 ③ 둘의 차이
  - 답: images는 내려받은 이미지의 목록, ps -a는 실행 중이거나 종료된 컨테이너의 목록을 보여줌
- (라) 🔍 `docker images` 출력을 붙여 넣고, `hello-world` 줄의 `IMAGE` · `ID` · `EXTRA` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `IMAGE` · `ID` · `EXTRA` 의 값과 뜻
  - 답: 

IMAGE는 hello-world:latest로, 이미지 이름은 hello-world이고 태그는 latest이다. ID는 11a3eb1597e8로, 이미지를 식별하는 고유 값이다. EXTRA는 U로, 이 이미지를 사용하는 컨테이너가 존재한다는 뜻이다. 종료된 컨테이너도 포함된다.

```
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   11a3eb1597e8       25.9kB         9.49kB    U
```

- (마) 🔍 `docker ps -a` 출력을 붙여 넣고, `hello-world` 줄의 `STATUS` · `PORTS` · `NAMES` · `IMAGE` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `STATUS` · `PORTS` · `NAMES` · `IMAGE` 의 값과 뜻
  - 답:
  STATUS: 컨테이너 상태. Exited (0) ...이면 정상 실행 후 종료됐다는 뜻
PORTS: 연결된 포트.
현재는 빈칸으로, 연결한 포트가 없다는 뜻
NAMES: 컨테이너 이름. 자동 생성되거나 직접 지정한 이름 현재는 wizardly_williamson
IMAGE: 컨테이너 생성에 사용한 이미지. hello-world
```
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
3272b3dabcf1   hello-world   "/hello"   29 seconds ago   Exited (0) 28 seconds ago             wizardly_williamson
```


### 문제 5-2 · Docker Hub 에서 이미지 이름 읽고 없는 이미지 받아 보기

- (가) `nginx:1.28` 에서 `nginx` 와 `1.28` 이 각각 무엇을 정하는지 적어 주세요.
  - 쓸 내용: ① nginx 가 정하는 것 ② 1.28 이 정하는 것
  - 답: nginx는 이미지 이름을 정하고, 1.28은 사용할 이미지의 버전을 나타내는 태그이다.
- (나) 🔍 `docker pull nginxx` 를 쳤을 때 나온 오류 문구와 그 뜻을 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② 뜻 ③ 고치는 방법
  - 답:Using default tag: latest
Error response from daemon: pull access denied for nginxx, repository does not exist or may require 'docker login'
뜻: 그 repo는 존재하지 않는다 그리고 도커 로그인 필수다
고치는 방법: 정확한 문구로 검색한다?
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(도커를 쓰면 무엇이 같아지는지)
  - 답: 도커를 사용하면 같은 이미지로 프로그램과 라이브러리 등 컨테이너 내부 실행 환경을 동일하게 구성할 수 있다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 

## 6교시 · nginx 서버 켜고 접속 기록 읽기

### 문제 6-1 · 포트 없이 켜 보고, 포트를 연결해 접속하고, 기록 읽기

- (가) 포트 없이 켠 `web` 에 접속했을 때 어떻게 되었는지 적어 주세요.
  - 쓸 내용: 접속했을 때 나온 화면이나 오류와 `docker ps` 의 PORTS 열
  - 답: CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
- (나) 🔍 `-p 8080:80` 이 하는 일을 내 PC의 포트와 컨테이너의 포트로 나눠 설명해 주세요.
  - 쓸 내용: ① 내 PC 쪽 포트 ② 컨테이너 쪽 포트 ③ 연결이 하는 일
  - 답: 8080, 80, 내 PC의 8080번 포트를 컨테이너의 80번 포트에 연결한다. 브라우저에서 http://localhost:8080 으로 접속하면 컨테이너 안의 nginx로 요청이 전달된다.
- (다) 🔍 `docker logs web` 출력에서 `GET /` 줄 하나를 붙여 넣고, 접속자 주소 · 시각 · 요청 · 응답 번호를 찾아 적어 주세요.
  - 쓸 내용: ① `GET /` 줄 ② 접속자 주소 · 시각 · 요청 · 응답 번호 네 가지
  - 답:172.17.0.1 - - [19/Oct/2026:06:08:03 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://127.0.0.1:8080/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36" "-"
  접속자 주소: 172.72.0.1
  시각:19/Oct/2026:06:08:03 +0000
  요청: GET /favicon.ico HTTP/1.1
  응답 번호: 404 - 요청 파일을 찾지 못함.

### 문제 6-2 · 컨테이너 안을 들여다보고, 끄고, 지우기

- (가) 컨테이너 안에서 `ls /usr/share/nginx/html` 로 본 파일 이름을 모두 적고, 그중 브라우저의 첫 화면이 어느 파일인지 적어 주세요.
  - 쓸 내용: ① 파일 이름 모두 ② 첫 화면 파일
  - 답:50x.html  index.html, index.html
- (나) 🔍 `docker stop web` 뒤에 `docker ps` 와 `docker ps -a` 에 각각 `web` 이 보이나요? 차이를 설명해 주세요.
  - 쓸 내용: ① stop 뒤 ps 에 보이는지 ② ps -a 에 보이는지 ③ 차이의 이유
  - 답: docker stop web 실행 후 docker ps에는 web이 보이지 않고, docker ps -a에는 보인다. docker ps는 실행 중인 컨테이너만 보여 주고, docker ps -a는 종료된 컨테이너도 보여 주기 때문이다.
- (다) 🔍 같은 이름으로 다시 `run` 했을 때 나온 오류 문구와, `docker rm` 이 필요한 이유를 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② rm 이 필요한 이유
  - 답:CONTAINER ID   IMAGE         COMMAND                   CREATED          STATUS                      PORTS     NAMES
07a3d7a0d916   nginx:1.28    "/docker-entrypoint.…"   13 minutes ago   Exited (0) 20 seconds ago             web
3272b3dabcf1   hello-world   "/hello"                  43 minutes ago   Exited (0) 43 minutes ago             wizardly_williamson

같은 이름으로 다시 실행하면 Conflict. The container name "/web" is already in use…라는 오류가 발생한다. 중지된 컨테이너도 이름을 유지하므로, 같은 이름으로 새 컨테이너를 만들려면 docker rm web으로 기존 컨테이너를 삭제해야 한다.

- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(켜는 명령 · 기록 보는 명령 · 정리 방법)
  - 답: docker run -d --name web -p 8080:80 nginx:1.28로 서버를 실행하고, docker logs web으로 기록을 확인하며, docker stop web과 docker rm web으로 중지하고 삭제한다.

- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 

## 7교시 · 내 페이지 연결 · 두 서버 · 올리기

### 문제 7-1 · 컨테이너 안의 변경이 사라지는 것을 보고, 내 폴더를 연결하기

- (가) 컨테이너 안에서 바꾼 뒤 `docker rm -f web` 으로 지우고 다시 켰을 때 화면이 어떻게 되었는지 적어 주세요.
  - 쓸 내용: ① 바꾼 뒤 화면 ② 지우고 다시 켠 뒤 화면
  - 답: 교재의 실습대로 진행하면, 컨테이너 안에서 파일을 바꾼 뒤에는 `inside`가 표시된다. `docker rm -f web`으로 컨테이너를 삭제하고 같은 이미지로 새로 실행하면 수정 내용이 사라져 원래의 `Welcome to nginx!` 화면으로 돌아간다.
- (나) 🔍 컨테이너 안에서 바꾼 내용이 사라진 이유와, `-v` 로 폴더를 연결하면 무엇이 달라지는지 적어 주세요.
  - 쓸 내용: ① 사라진 이유 ② -v 로 연결하면 달라지는 점
  - 답: 
  컨테이너 안에서 수정한 파일은 그 컨테이너의 쓰기 가능한 계층에 저장되므로, 컨테이너를 삭제하면 함께 사라진다. 이미지는 바뀌지 않아 같은 이미지로 새 컨테이너를 만들면 원래 파일로 시작한다. `-v`로 내 PC 폴더를 연결하면 파일이 내 PC에 남으므로 컨테이너를 삭제해도 유지되며, 내 PC에서 수정하고 브라우저를 새로 고치면 변경 내용이 반영된다.
- (다) 🔍 `MSYS_NO_PATHCONV=1` 없이 `-v` 를 실행했을 때 화면에 무엇이 나왔고 왜 그랬는지 적어 주세요.
  - 쓸 내용: ① 화면에 나온 것 ② 그렇게 된 이유
  - 답: 
  교재의 Git Bash 실습에서는 내 페이지 대신 `Welcome to nginx!` 기본 화면이 나온다. Git Bash가 컨테이너 쪽 경로인 `/usr/share/nginx/html`을 `C:/Program Files/Git/usr/share/nginx/html` 같은 윈도 경로로 자동 변환해, 내 폴더가 nginx의 문서 폴더에 연결되지 않았기 때문이다. 명령 앞에 `MSYS_NO_PATHCONV=1`을 붙이면 경로 자동 변환을 막아 의도한 위치에 연결할 수 있다.

### 문제 7-2 · 서버 두 대를 띄워 포트로 구분하고, 파일을 고쳐 바로 반영되는지 보기

- (가) 두 주소(`8080` · `8081`)에서 보이는 화면을 각각 적어 주세요.
  - 쓸 내용: 두 주소의 화면 문구
  - 답: 
  교재의 실습 기준으로 `http://127.0.0.1:8080`에는 `site-one`과 「첫 번째 서버입니다」가, `http://127.0.0.1:8081`에는 `site-two`와 「두 번째 서버입니다」가 표시된다. 첫 번째 파일의 문구를 수정하고 새로 고치면 8080 화면에 수정한 문구가 반영되고, 8081 화면은 그대로 유지된다.
- (나) 🔍 `docker ps` 의 PORTS 열에서 두 서버를 구분해 주는 것은 무엇인가요?
  - 쓸 내용: PORTS 열에서 서버를 구분하는 값
  - 답: 내 PC 쪽 포트 번호인 `8080`과 `8081`이다. `8080->80/tcp`는 첫 번째 서버, `8081->80/tcp`는 두 번째 서버로 연결된다. 컨테이너 안의 포트는 둘 다 80번이지만 내 PC 쪽 포트가 달라 두 서버를 구분할 수 있다.
- (다) 🔍 `:ro` 는 무슨 뜻이고, 왜 읽기 전용으로 연결하나요?
  - 쓸 내용: ① :ro 의 뜻 ② 읽기 전용으로 연결하는 이유
  - 답: `:ro`는 read-only, 즉 읽기 전용이라는 뜻이다. 컨테이너가 연결된 폴더의 파일을 읽을 수 있지만 수정하거나 삭제하지 못하게 한다. 웹 페이지를 제공하는 데 필요한 읽기 권한만 주어, 컨테이너를 통한 원본 파일의 변경을 막기 위해 사용한다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(두 서버를 어떻게 띄웠는지)
  - 답: 
  같은 `nginx:1.28` 이미지로 두 컨테이너를 만들고, 각각 내 PC의 `site-one`과 `site-two` 폴더를 `-v`와 `:ro`로 읽기 전용 연결하여 8080과 8081 포트로 서비스를 제공하도록 구성한다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: 내 PC 폴더를 컨테이너에 연결하면, 내 PC에서 웹 파일을 수정한 뒤 컨테이너를 다시 만들거나 재시작하지 않아도 브라우저 새로 고침으로 변경 내용을 확인할 수 있다는 점을 알게 되었다.

### 문제 7-3 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 빨간 목록에 줄이 몇 개였는지, 그 가운데 `.env` · `.venv` 가 있었는지 적어 주세요.
  - 쓸 내용: ① 줄 수 ② .env · .venv 가 있었는지
  - 답:
