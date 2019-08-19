python生成可安装包步骤
1、创建一个模块（有__init__.py文件）helper
2、在helper模块中定义自己的函数库helper
3、在helper模块同级目录下创建一个setup.py
4、python3 setup.py build
5、python3 setup.py sdist就可以生成对应的压缩文件
6、将压缩包拷贝到需要安装的环境解压
7、执行命令python3 setup.py install即可