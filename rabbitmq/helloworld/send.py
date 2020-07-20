import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='10.176.139.8',
    port=5672,
    virtual_host="/devops",
    credentials=pika.PlainCredentials("devops", "q9wCFiEti7UuxYFPr3q0Xw")
))
channel = connection.channel()
channel.queue_declare(queue='hello')
for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
connection.close()