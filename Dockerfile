FROM python:2.7
ENV PYTHONUNBUFFERED 1
#NOTE:
#if you use company proxy please configure the ENV
#else if you use your own connection just remove the ENV
ENV http_proxy 'http://192.168.8.7:3128'
ENV https_proxy 'http://192.168.8.7:3128'
ENV HTTP_PROXY 'http://192.168.8.7:3128'
ENV HTTPS_PROXY 'http://192.168.8.7:3128'
RUN mkdir /crud
WORKDIR /crud
COPY requirements.txt /crud/
COPY . /crud
RUN pip --default-timeout=60 install -r requirements.txt \
    && python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
