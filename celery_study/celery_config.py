from kombu import Queue

CELERY_QUEUES = (
    Queue('activity', routing_key='task.mytask'),
)
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'task.mytask'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ROUTES = {
    'celery_study.tasks.add': {
        'queue': 'activity',
        'routing_key': 'task.mytask',
    }
}
