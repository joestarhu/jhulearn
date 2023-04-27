"""
创建一个FastApi程序
Author:J.Hu
Date:2023-04-27
"""

"""
构建虚拟环境并安装fastapi相关包

# 虚拟环境的构建命令:
python3 -m venv venv

# 进入虚拟环境
. venv/bin/activate

# 安装fastapi
pip install fastapi

# 安装uvicorn作为服务器
pip install "uvicorn[standard]"
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_fastapi():
    return '你好,FastAPI'
