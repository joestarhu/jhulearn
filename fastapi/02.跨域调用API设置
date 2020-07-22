#! /usr/bin/env python3


# 中间件的导入.
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

# 中间件的设定
# 这些配置完成后,服务端这边是可以进行跨域的请求的了
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

