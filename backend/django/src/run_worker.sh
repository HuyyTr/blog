#!bin/sh

# wait for RabbitMQ server to start
sleep 10

celery -A core worker -l info