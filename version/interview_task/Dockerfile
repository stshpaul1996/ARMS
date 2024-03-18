FROM python:3.12.2-bullseye
#FROM directive is used to take the base image either it is python or django
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*
# if we want to run any command while creating an image then we have to use RUN directive.
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . . 
# it will copy all this code into the docker image
RUN python3 manage.py migrate
# RUN python3 manage.py test
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000

