# 开发整备
## 虚拟环境安装和激活
```
virtualenv venv
source /venv/bin/active
```
## 安装Flask文件
```
pip install flask
```

# Flask的基础
## 1-app.py
这个文件介绍了最简单,也是最基础的Flask的文件构成.

运行./app.py（如果没有这个，看看是否没有执行权限，chmod 766 app.py设文件可运行）  
输入localhost:5000(127.0.0.1:5000也可以) 即可访问到你的flask应用了

## 2-app.py
这个文件介绍了 使用flask-script插件来运行程序.

现在可以通过如下命令来运行程序了.
* ./app.py runserver
* ./app.py runserver -d
* ./app.py runserver --host 0.0.0.0

