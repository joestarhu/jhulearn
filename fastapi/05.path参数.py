from fastapi import FastAPI

app = FastAPI()



# 参数位置:Path
"""
参数位置:Path
Path不可设置默认值

path在url中的表现为: id为1
127.0.0.1:8000/1

get/post/put/patch/delete 都支持path参数

"""
@app.get('/{id}')
async  def get_func(id:int=100):
    return f'get is {id}'

@app.post('/{id}/detail')
async def post_func(id:int=100):
    return f'post is {id}'

@app.put('/{id}')
async def put_func(id:int):
    return f'put is {id}'

@app.patch('/{id}')
async def patch_func(id:int):
    return f'patch is {id}'

@app.delete('/{id}')
async def del_func(id:int):
    return f'del is {id}'
