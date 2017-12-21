执行Python脚本传递参数
python test_param.py param1 param2 param3
脚本内部参数的接收采用sys.argv数组形式接收
默认情况下，第一个参数是脚本文件的名称，上例中，sys.argv[0]是test_param.py
其余的参数默认都是字符串形式