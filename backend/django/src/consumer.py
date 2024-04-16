import django
from django.conf import settings

import os
import pika
import logging

from ai_app.tasks import print_message

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

connection_params = pika.ConnectionParameters(
    host=settings.RABBITMQ['HOST'], port=settings.RABBITMQ['PORT'])

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='test')


def message_callback(chanel, method, properties, body):
    logging.info('Received message from test')
    print_message.delay(body)


channel.basic_consume(on_message_callback=message_callback, queue='test')

channel.start_consuming()
