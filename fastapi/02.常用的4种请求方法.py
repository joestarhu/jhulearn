"""
创建一个FastApi程序
Author:J.Hu
Date:2023-04-27
"""

from fastapi import FastAPI

app = FastAPI()

"""
根据Restful api 常用的4种方法:
POST: 新增
GET:  查询
PUT:  修改
DELETE: 删除
"""

@app.post('/')
async def post_func():
    return "Post方法,常用于新增数据"

@app.get('/')
async def get_func():
    return 'Get方法,常用于获取数据'

@app.put('/')
async def put_func():
    return 'Put方法,常用于更新数据'

@app.delete('/')
async def delete_func():
    return 'Delete方法,常用于删除数据'
