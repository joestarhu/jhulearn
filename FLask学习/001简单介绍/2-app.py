from flask import Flask
from flask_script import Manager

app = Flask(__name__)

"""
使用Manager来管理和运行程序.
原来我们需要通过 app.run(debug=True) 这种方式来配置一些参数,那么
每次运行不同的参数的时候,就需要修改代码,通过flask-script插件后,
可以直接在运行的时候来指定输入比如:
* app.py runserver -d               使用debug模式
* app.py runserver --host 0.0.0.0   指定host地址
"""
manager = Manager(app)

@app.route('/')
def hello():
    return 'Hello'

if __name__ == '__main__':
    manager.run()
