from fastapi import FastAPI

app = FastAPI()

"""
常见的HTTP请求类型:
GET
POST
PUT/PATCH
DELETE
"""

@app.get('/')
async def hello_fastapi():
    return '这是Get方法'

@app.post('/')
async def post_fastapi():
    return '这是post方法'


@app.put('/')
async def put_fastapi():
    return '这是put方法'

@app.patch('/')
async def patch_fastapi():
    return '这是patch方法'

@app.delete('/')
async def del_fastapi():
    return '这是delete方法'


