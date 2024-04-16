from __future__ import absolute_import, unicode_literals
from celery import shared_task

import time
import logging


@shared_task()
def add(x, y):
    return x+y


@shared_task
def print_message(message):
    time.sleep(5.0)
    logging.info(f"Print message task: {message}")
    return message
