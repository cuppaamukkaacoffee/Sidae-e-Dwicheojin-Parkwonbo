FROM python:3.8

RUN apt-get update 
RUN apt-get install -y dnsutils
RUN apt-get install -y masscan
RUN apt-get install -y libpcap0.8-dev

ENV DOCKERIZE_VERSION v0.2.0  
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt 
RUN chmod +x /app/start.sh  # start 파일을 실행 가능하게 합니다.
EXPOSE 8000  

ENTRYPOINT ["sh","./start.sh"]
