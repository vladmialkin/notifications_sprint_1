FROM python:3.12

RUN apt-get update && apt-get install -y cron

WORKDIR /src

COPY src/app ./app
COPY ./crontab /etc/cron.d/my-cronjob

RUN chmod 0644 /etc/cron.d/my-cronjob
RUN crontab /etc/cron.d/my-cronjob
RUN chmod +x /src/app/main.py
RUN touch /var/log/cron.log && chmod 664 /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
