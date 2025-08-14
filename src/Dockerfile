FROM python:3.13.6

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y ffmpeg && \
    pip install --upgrade pip &&\ 
    pip install -r requirements.txt &&\
    rm -rf requirements.txt 

COPY . .

CMD [ "python", "bot.py" ]