FROM python:3

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt 
RUN chmod +x /app/start.sh  # start 파일을 실행 가능하게 합니다.
EXPOSE 8000  

ENTRYPOINT ["sh","./start.sh"]
