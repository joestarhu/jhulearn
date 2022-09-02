"""
create_engine的配置请参考创建连接
"""

from sqlalchemy import create_engine,text
from datetime import datetime

engine = create_engine(uri,echo=True,future=True)

# 建表语句
stmt = text('create table demo (id int, val varchar(255), ope_time datetime)')
with engine.connect() as conn:
  conn.execute(text('select "hello sqllachemy" from dual'))
