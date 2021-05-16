
### Prerequisities
----------------------------
### Docker

* [Windows](https://docs.docker.com/windows/started)
* [macOS](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Docker Compose

### Windows and macOS

Docker Compose is included in
[Docker Desktop](https://www.docker.com/products/docker-desktop)
for Windows and macOS.

### Linux

[release page](https://github.com/docker/compose/releases)

### Using pip

```console
pip install docker-compose
```
### 사용방법
----------------------------
(1) 이 저장소를 복사합니다\n
복사하기전에 Window는 git config --global core.autocrlf input 명령어 실행
```bash
git clone https://github.com/cuppaamukkaacoffee/Sidae-e-Dwicheojin-Parkwonbo.git
```

(2) docker-compose.yml 실행
```bash
cd .\Sidae-e-Dwicheojin-Parkwonbo\ 
docker compose -f ./Backend/sdp_backend/docker-compose.yml -f ./Frontend/sdp_frontend/docker-compose.yml up
```

(3) 모든 것이 시작되면 호스트 컴퓨터에서 http : // localhost : 3000 / 을 통해 웹 애플리케이션에 액세스 할 수 있습니다.
```bash
open http://localhost:8000/
```

###배포
https://sdp-test.sdp-scanner.site/
