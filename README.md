
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
(1) 이 저장소를 복사합니다 (복사하기전에 Window는 git config --global core.autocrlf input 명령어 실행)
```bash
git clone https://github.com/cuppaamukkaacoffee/Sidae-e-Dwicheojin-Parkwonbo.git
```

(2) docker-compose.yml 실행 (sdp_backend폴더에서 먼저 docker compose up 실행후 sdp_frontend 에서 docker compose up 실행)
```bash
cd ./Sidae-e-Dwicheojin-Parkwonbo/
docker-compose -f ./Backend/sdp_backend/docker-compose.yml up
docker-compose -f ./Frontend/sdp_frontend/docker-compose.yml up
```

(3) 모든 것이 시작되면 호스트 컴퓨터에서 http : // localhost : 3000 / 을 통해 웹 애플리케이션에 액세스 할 수 있습니다.
```bash
open http://localhost:3000/
```
  
### 설계
---------------
![image](https://user-images.githubusercontent.com/22341324/129678503-95c61c8e-f5e7-49df-8be7-911db4a350fe.png)
![스크린샷 2021-08-17 오후 3 58 38](https://user-images.githubusercontent.com/22341324/129678680-52464aa4-cf78-4a3f-80c9-5ff3de692e54.png)

### 디자인
----------------------------
![image](https://user-images.githubusercontent.com/22341324/122683525-bb76e700-d23a-11eb-8b46-f4ae2b63b375.png)
![image](https://user-images.githubusercontent.com/22341324/122683527-bdd94100-d23a-11eb-959b-408c56321bd2.png)
![image](https://user-images.githubusercontent.com/22341324/122683531-bfa30480-d23a-11eb-9cdb-7a62b34d9a22.png)    
![image](https://user-images.githubusercontent.com/22341324/122683534-c29df500-d23a-11eb-9e75-6c6a4021cad9.png)
![image](https://user-images.githubusercontent.com/22341324/122683535-c467b880-d23a-11eb-84cf-6cb6231a60d1.png)
![image](https://user-images.githubusercontent.com/22341324/122683537-c598e580-d23a-11eb-905d-543130e1def9.png)
