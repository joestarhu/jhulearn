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
## 一个基本结构的列子
建立一个app.py文件，内容如下：
``` python
#!/usr/bin/env python3
# 加入shebang可以直接运行py文件
# 引入Flask类
from flask import Flask

# 初始化
app = Flask(__name__)

@app.route('/')   # 这个装饰器在flask中称为路由
def index():      # 这个函数在flask中称为视图函数
  return 'hello flask',200 # 这个返回被称为响应, 200是HTTP的响应码，可以省略
  # return 'hello flask' 这个和上面那句Return是同样的效果

if __name__ == '__main__':
  # 启动Flask服务，其中debug=True代表为调试模式
  app.run(debug = True)
```

运行./app.py（如果没有这个，看看是否没有执行权限，chmod 766 app.py设文件可运行）  
输入localhost:5000(127.0.0.1:5000也可以) 即可访问到你的flask应用了

