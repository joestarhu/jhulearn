from sqlalchemy import create_engine
from urllib.parse import quote

"""
注意点在拼接URI的时候，要进行urlencode的转义， 主要是为了应对出现：和@的情况 
比如 密码为1：123    不进行转移字符串就变成了 username：1：123，造成连接的URI不正确
下面以mysql为例子
"""
name = quote('username')
passwd = quote('passwd')
host = quote('localhost')
port = '3306'
database = 'mysqldemo'

# 注意charset也要设置，未设置charset有时候会导致一些中文字符无法插入数据，和Mysql的database要保持一致。
uri = 'mysql+pymysql://{name}:{passwd}@{host}:{port}/{database}?charset=utf8mb4'

"""
echo:打印Log，在生产环境中可用
future：使用sqlalchemy2.0的特性
"""
engine = create_engine(uri,echo=True,future=True)
