from kombu import Connection  # noqa

with Connection('redis://localhost:6379/') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')
    message = simple_queue.get(block=True, timeout=1)
    print('Received: {0}'.format(message.payload))
    message.ack()
    # simple_queue.close()
