#! /usr/bin/env python3

"""
1. 首选第一步:虚拟环境的安装和启动
> virtualenv venv
> . venv/bin/activate

2. 在虚拟环境下,安装fastapi和uvicorn
> pip install fastapi
> pip install uvicorn

完成后可以进行如下的代码编写,并运行第一个fastAPI程序
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello():
    return {'msg':'hello fastAPI'}


if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app,host='127.0.0.1', port=8000)
  """
  也可以使用命令 uvicorn main:app --reload 来替代
  """
