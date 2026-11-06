# 4과목 Day 5 도커 컴포즈로 서버 두 대 켜기 · 웹 서버 로그 만들기 · 오후 (이름 · 2026-11-06(금))

> **쓰는 법**
> - 문제를 풀 때마다 그 문제 제목 아래 질문에 답합니다.
> - 질문마다 `쓸 내용:` 에 무엇을 쓰면 되는지 적혀 있습니다. 그대로 `답:` 뒤에 씁니다.
> - 출력이나 코드를 붙여 넣는 질문은 `답:` 아래 빈 코드 상자에 붙여 넣고, 설명은 `답:` 뒤에 씁니다.
> - 「왜」를 묻는 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 이 교시에서 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다. 🔍 가 없는 질문도 못 적으면 같은 말을 씁니다.

---

## 5교시 · 도커 복습 · 컴포즈로 서버 두 대 한 번에 켜기

### 문제 5-1 · 서버 한 대를 복습하고 컴포즈로 두 대 켜기

- (가) 5교시 순서의 서버 켜기 · 확인 명령(`docker images` 부터 `curl` 까지)과 그 결과를 친 순서대로 붙여 넣고, 서비스 이름 두 개와 각 서비스의 포트를 적어 주세요.
  - 쓸 내용: ① 명령과 결과를 친 순서대로(코드 상자에 붙여 넣기): `docker images` · `docker run` · `docker ps` · `docker stop` · `docker compose up -d` · `docker compose ps` · `curl` 두 개 (`docker pull` 은 받았을 때만, `pwd` · `touch` · `ls` 는 붙이지 않아도 됩니다) ② 서비스 이름 두 개 ③ 각 서비스의 포트
  - 답: 서비스 이름은 web1과 web2이다. web1은 내 PC의 8080번 포트를 컨테이너의 80번 포트에 연결하고, web2는 내 PC의 8081번 포트를 컨테이너의 80번 포트에 연결한다. 기록한 출력에서 두 서비스 모두 Up 상태이고, 두 주소에 보낸 curl 요청은 모두 200으로 응답했다.

```
$ docker images nginx:1.28
IMAGE        ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:1.28   146adea4768b        258MB         64.1MB   U
$ docker run -d --rm -p 8080:80 --name web-run nginx:1.28
e1a2ad01c5441866eae9a81e97aa28caabf3a1efdd4c12bf66817887c63237a4
$ docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED                  STATUS                  PORTS                                     NAMES
e1a2ad01c544   nginx:1.28   "/docker-entrypoint.…"   Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-run
$ docker stop web-run
web-run
$ docker compose up -d
 Network anomaly_detection_default Creating
 Network anomaly_detection_default Created
 Container anomaly_detection-web1-1 Creating
 Container anomaly_detection-web2-1 Creating
 Container anomaly_detection-web1-1 Created
 Container anomaly_detection-web2-1 Created
 Container anomaly_detection-web2-1 Starting
 Container anomaly_detection-web1-1 Starting
 Container anomaly_detection-web2-1 Started
 Container anomaly_detection-web1-1 Started
$ docker compose ps
NAME                       IMAGE        COMMAND                  SERVICE   CREATED                  STATUS                  PORTS
anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      Less than a second ago   Up Less than a second   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
$ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
200
$ curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
200
```

- (나) 🔍 서버 두 대를 `docker run` 으로 켜는 것과 `compose.yaml` 과 `docker compose up -d` 로 켜는 것을 비교해, 컴포즈가 더 나은 점을 두 가지 적어 주세요.
  - 쓸 내용: ① 컴포즈가 더 나은 점 두 가지
  - 답: 첫째, 서버마다 긴 docker run 명령을 따로 입력하는 대신 docker compose up -d 한 줄로 파일에 정의한 두 서비스를 함께 켤 수 있다. 둘째, 이미지와 포트 같은 설정을 compose.yaml에 남겨 공유하고 깃허브에서 변경 이력을 관리할 수 있어, 팀원이 설정을 빠뜨리지 않고 같은 구성으로 실행하기 쉽다.

- (다) 🔍 보안 사고가 난 뒤 감사팀이 「사고 당시와 같은 구성으로 서버를 다시 켜 보라」고 요청했습니다. 팀원 한 명은 3주 전에 긴 `docker run` 명령을 직접 쳐서 서버를 켰는데 그 명령을 기억하지 못합니다. 다른 팀은 `compose.yaml` 을 깃허브에 올려 두었습니다. 두 팀이 같은 구성을 다시 켤 수 있는지 비교하고, 파일에 `nginx:1.28` 처럼 버전을 적어 두는 것이 이런 재현에 왜 중요한지 적어 주세요.
  - 쓸 내용: ① 두 팀의 차이 ② 버전을 적어 두는 것이 재현에 중요한 이유
  - 답: docker run 명령을 기억하지 못하는 팀은 별도의 기록이 없으면 당시 사용한 이미지와 포트 등의 설정을 정확히 재현하기 어렵다. compose.yaml을 깃허브에 남긴 팀은 사고 당시의 파일을 찾아 docker compose up -d로 그 파일에 정의된 구성을 다시 실행할 수 있다. nginx:1.28처럼 버전을 적으면 버전을 생략해 latest 태그를 사용할 때보다 이미지 버전이 달라질 가능성을 줄일 수 있다. 다만 버전 태그도 같은 이름으로 갱신될 수 있으므로 이미지까지 정확히 고정해야 한다면 이미지 내용의 식별자인 digest도 기록해야 한다.

- (라) 🔍 팀원 세 명이 같은 `compose.yaml` 로 서버를 켰는데 한 명의 PC 에서만 `8081` 번 포트를 다른 프로그램이 쓰고 있어서 `web2` 가 켜지지 않았습니다. 이 사람이 파일의 어느 줄을 어떻게 바꾸면 되는지 적고, 바꿔도 서버 안에서는 여전히 `80` 번 포트로 동작하는 이유를 적어 주세요. 이 사람이 `curl` 로 확인할 때 달라지는 점도 적어 주세요.
  - 쓸 내용: ① 바꿀 줄과 바꾼 모양 ② 서버 안은 그대로 80 인 이유 ③ curl 주소의 달라지는 점
  - 답: web2의 ports 아래에 있는 "8081:80"을, 예를 들어 내 PC에서 사용하지 않는 포트가 8082라면 "8082:80"으로 바꾸고 docker compose up -d로 적용한다. 콜론 왼쪽은 내 PC에서 받는 포트이고 오른쪽은 컨테이너 안의 포트이므로, 오른쪽을 바꾸지 않으면 nginx는 계속 80번 포트로 동작한다. 확인할 curl 주소는 http://localhost:8081에서 http://localhost:8082로 바뀐다.

## 6교시 · 서버마다 접속 범위 정하기 · 설정 바꿔 적용하기

### 문제 6-1 · 서버마다 접속 범위를 정해 컴포즈 파일로 적용하기

- (가) 1번과 5번의 `docker compose ps` 출력을 붙여 넣고, 접속 범위가 바뀐 기존 서비스와 새로 추가된 서비스를 따로 적어 주세요.
  - 쓸 내용: ① 1번 출력(코드 상자에 붙여 넣기) ② 5번 출력(코드 상자에 붙여 넣기) ③ 접속 범위가 바뀐 기존 서비스 ④ 새로 추가된 서비스
  - 답: 접속 범위가 바뀐 기존 서비스는 web2이다. 내 PC의 모든 네트워크 인터페이스로 받던 8081번 포트를 127.0.0.1에서만 받도록 제한했다. 새로 추가된 서비스는 web3으로, 127.0.0.1:8082로 접속하고 ./logs 폴더에 nginx 로그를 남긴다. web1의 8080번 포트 설정은 그대로이다. 적용 전 출력은 5교시에서 기록한 내용을 옮겼고, 적용 후 출력은 현재 상태를 다시 조회한 결과이다.

```
적용 전 (5교시에서 기록한 출력)
$ docker compose ps
NAME                       IMAGE        COMMAND                  SERVICE   CREATED                  STATUS                  PORTS
anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      Less than a second ago   Up Less than a second   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      Less than a second ago   Up Less than a second   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp

적용 후 (현재 상태 재조회)
$ docker compose -f compose.secure.yaml ps
NAME                       IMAGE        COMMAND                  SERVICE   CREATED          STATUS          PORTS
anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      45 minutes ago   Up 45 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      13 minutes ago   Up 13 minutes   127.0.0.1:8081->80/tcp
anomaly_detection-web3-1   nginx:1.28   "/docker-entrypoint.…"   web3      13 minutes ago   Up 13 minutes   127.0.0.1:8082->80/tcp
```

- (나) 🔍 `"8081:80"` 과 `"127.0.0.1:8081:80"` 은 누가 접속할 수 있는지가 어떻게 다른가요? 관리 화면이나 데이터베이스 서버를 이렇게 설정하는 이유도 적어 주세요.
  - 쓸 내용: ① 두 포트 줄에서 누가 접속할 수 있는지의 차이 ② 관리 화면 · 데이터베이스를 이렇게 설정하는 이유
  - 답: "8081:80"은 내 PC의 모든 네트워크 인터페이스에 포트를 열어, 방화벽과 네트워크가 허용하면 같은 네트워크의 다른 PC에서도 접속할 수 있다. "127.0.0.1:8081:80"은 호스트에 공개하는 포트를 루프백 주소에만 연결하므로 다른 PC에서 내 PC의 네트워크 주소로 직접 접속할 수 없고 내 PC에서 접속한다. 관리 화면이나 데이터베이스처럼 외부에 공개할 필요가 없는 서비스의 접속 범위를 줄여 불필요한 접근과 공격 시도를 줄이기 위해 이렇게 설정한다.

- (다) 🔍 `up -d` 의 출력에서 `web1` 은 `Running`, `web2` 는 `Recreated`, `web3` 은 `Created` 였습니다. 서버마다 출력이 다른 이유와, 운영 중인 서비스의 설정을 바꿀 때 이것이 왜 도움이 되는지 적어 주세요.
  - 쓸 내용: ① 서버마다 출력이 다른 이유 ② 서버를 끊지 않고 바꿀 수 있는 것의 쓸모
  - 답: web1은 설정이 바뀌지 않아 기존 컨테이너가 계속 실행되어 Running으로 표시된다. web2는 포트의 접속 범위가 바뀌어 기존 컨테이너를 새 설정으로 다시 만들었으므로 Recreated이고, web3은 새로 추가되어 Created이다. 바뀐 서비스만 다시 만들기 때문에 web1처럼 설정이 그대로인 서비스는 중단하지 않고 다른 서비스의 보안 설정을 적용할 수 있다. 다만 다시 만드는 web2 자체에는 잠깐의 중단이 생길 수 있다.

### 마무리 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
  - 쓸 내용: ① `.env` · `.venv` 가 보였는지 ② 보였다면 한 조치
  - 답:
