FROM python:3.8

ENV DJANGO_SETTINGS_MODULE djangoprj.settings
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y unzip wget
RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1

#RUN wget https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver_linux64.zip && \
    #unzip chromedriver_linux64.zip && \
    #rm chromedriver_linux64.zip && \
    #mv chromedriver /usr/local/bin/

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_109.0.5414.74-1_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb

WORKDIR /code
COPY . /code/
RUN ls -a
RUN pip install -r requirements.txt
