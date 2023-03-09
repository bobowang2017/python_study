import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='10.176.139.8',
    port=5672,
    virtual_host="/devops",
    credentials=pika.PlainCredentials("devops", "q9wCFiEti7UuxYFPr3q0Xw")
))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# channel.basic_qos(prefetch_count=1)
channel.basic_consume('world', callback, False)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
