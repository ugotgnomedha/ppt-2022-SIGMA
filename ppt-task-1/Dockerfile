FROM python:latest

RUN mkdir /ppt-task-1
WORKDIR /ppt-task-1
COPY . . 
EXPOSE 80/udp

# host - динамический ip адрес машины, на которой запускается решение
ENV host=127.0.0.1
ENV port=80

CMD [ "python", "/ppt-task-1/main.py"]