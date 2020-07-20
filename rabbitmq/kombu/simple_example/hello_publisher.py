import datetime

from kombu import Connection

with Connection('redis://localhost:6379/') as conn:
    simple_queue = conn.SimpleQueue('simple_queue')
    message = 'helloworld, sent at {0}'.format(datetime.datetime.today())
    simple_queue.put(message)
    print('Sent: {0}'.format(message))
    # simple_queue.close()
