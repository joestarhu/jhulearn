from sqlalchemy import create_engine,text
from urllib.parse import quote

# name=quote('root')
# passwd = quote('qwe321')
# host=quote('localhost')
# port='55001'
uri = 'mysql+pymysql://root:qwe321@localhost:55001/jhu?charset=utf8mb4'

engine = create_engine(uri,echo=True,future=True)

# 创建表格
stmt = text('create table some_table(id integer,name varchar(256))')
with engine.connect() as conn:
    conn.execute(stmt)

# 插入数据 单个数据
stmt=text('insert into some_table values(:id,:name)').bindparams(id=1,name='hujian')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

# 插入数据 多个数据
stmt=text('insert into some_table values(:id,:name)')
with engine.connect() as conn:
    conn.execute(stmt,[dict(id=2,name='jack'),dict(id=3,name='rose'),dict(id=4,name='eva')])
    conn.commit()

# 查询数据
stmt=text('select * from some_table')
with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())

# 删除表格
stmt=text('drop table some_table')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
