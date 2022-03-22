FROM andrianovartemii/opencv-container:latest

RUN mkdir /ppt-task-4
WORKDIR /ppt-task-4
COPY . . 
EXPOSE 80/udp

# host - динамический ip адрес машины, на которой запускается решение
ENV host=127.0.0.1
ENV port=80

# добавить, если используются какие-либо библиотеки при сборке решения 
# RUN pip3 install -r requirements.txt

CMD [ "python", "/ppt-task-4/main.py"]