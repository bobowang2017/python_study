import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('47.105.104.233', 5672, "/", credentials))

channel = connection.channel()
channel.queue_declare(queue='logstash', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume('logstash', callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
