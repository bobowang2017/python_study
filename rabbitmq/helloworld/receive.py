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

# channel.basic_ack(delivery_tag=method.delivery_tag)
# 加上这句，通知给RabbitMQ说这个消息已经处理完了，可以从队列里删了，如果no_ack=False这里必须要写，为True可以不写
channel.basic_consume('hello', callback, True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
