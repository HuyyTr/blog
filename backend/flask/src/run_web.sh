#!bin/sh

# wait for RabbitMQ server to start
sleep 10
gunicorn -w 4 --bind 0.0.0.0:5000 wsgi