FROM python:3-alpine

RUN apk add --no-cache apk-cron && apk add --no-cache docker-cli

WORKDIR /app

# copy all files to image
COPY . .

# setup cron
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# run crond as main process of container
CMD ["crond", "-f"]