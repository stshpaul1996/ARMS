FROM python:3.12.2-bullseye
COPY  ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000

# RUN  python manage.py test 
# RUN python manage.py makemigrations
# RUN python manage.py migrate

CMD python manage.py test; python manage.py makemigrations; python manage.py migrate; python manage.py runserver 0.0.0.0:8000
