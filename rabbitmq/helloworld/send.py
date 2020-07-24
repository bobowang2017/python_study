import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='10.176.139.8',
    port=5672,
    virtual_host="/devops",
    credentials=pika.PlainCredentials("devops", "q9wCFiEti7UuxYFPr3q0Xw")
))
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True, passive=True)
channel.queue_declare(queue='hello', durable=True, passive=True)
channel.exchange_declare(exchange="task.rec.tt", durable=True, exchange_type="direct", passive=True)
# 交换机和队列绑定:生产者发布消息时无需绑定，消费者消费消息时需要绑定
channel.queue_bind(exchange="task.rec.tt", queue="hello", routing_key="world1")
channel.queue_bind(exchange="task.rec.tt", queue="world", routing_key="world2")
channel.basic_qos(prefetch_count=1)
for i in range(10):
    channel.basic_publish(exchange='task.rec.tt', routing_key='world1', body=f'Hello World--{i}')
connection.close()