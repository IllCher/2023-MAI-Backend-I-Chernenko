FROM python:3.8

ENV DJANGO_SETTINGS_MODULE djangoprj.settings
RUN pip install --upgrade pip
WORKDIR /code
COPY . /code/
RUN ls -a
RUN pip install -r requirements.txt
