FROM python:latest

RUN mkdir /ppt-task-2
WORKDIR /ppt-task-2
COPY . . 
EXPOSE 80/udp

# host - динамический ip адрес машины, на которой запускается решение
ENV host=127.0.0.1
ENV port=80
ENV mode=test
CMD [ "python", "/ppt-task-2/main.py"]