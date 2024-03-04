FROM python:3.12.2-bullseye 
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt 
COPY . . 
RUN python manage.py migrate
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
