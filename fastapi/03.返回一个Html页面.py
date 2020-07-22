from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# 设定模板所在的文件夹
templates = Jinja2Templates(directory='templates')


# 返回一个Templates页面
@app.get('/')
async def hello(req: Request):
    return templates.TemplateResponse('main.html', {'request': req})


