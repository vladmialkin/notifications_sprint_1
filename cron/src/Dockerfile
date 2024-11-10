FROM python:3.12

WORKDIR /opt/app/
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt update && pip install --upgrade pip && apt-get install -y cron
COPY ./requirements/main.txt requirements.txt
COPY ./crontab /etc/cron.d/my-cronjob
RUN chmod 0644 /etc/cron.d/my-cronjob
RUN crontab /etc/cron.d/my-cronjob
RUN touch /var/log/cron.log && chmod 664 /var/log/cron.log
RUN pip install -r requirements.txt

COPY . .

CMD cron && tail -f /var/log/cron.log






