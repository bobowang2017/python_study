## 启动参数配置
celery -A celery_study.celery_task.celery_app.cel_app worker -l info -P eventlet

#### 1、建议在外层目录下启动
#### 2、启动参数中app可以是对应app的类文件也可以是定义app中的名称
#### 3、-P eventlet 是为了解决windows环境下任务调用失败的问题，Linux没有此问题
#### 4、task的定义最好一个task对应一个类文件

