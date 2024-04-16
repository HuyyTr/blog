from flask import Flask
import os
import pika

application = Flask(__name__)

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")

connection_params = pika.ConnectionParameters(
    host=RABBITMQ_HOST, port=RABBITMQ_PORT)
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue="test")


@application.route("/send")
def send():
    try:
        channel.basic_publish(
            exchange='', routing_key='test', body='Hello RabbitMQ!')
    except Exception as e1:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        channel = connection.channel()
        channel.basic_publish(
            exchange='', routing_key='test', body='Hello RabbitMQ!')
    return "Message sent to RabbitMQ"


if __name__ == "__main__":
    port = os.environ.get("PORT")
    application.run(debug=True, host="0.0.0.0", port=port)
