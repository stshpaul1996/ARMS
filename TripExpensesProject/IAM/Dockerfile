FROM python:3.12.2-bullseye
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python3 manage.py test
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000