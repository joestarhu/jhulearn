from sqlalchemy import create_engine,text

uri = 'mysql+pymysql://root:qwe321@localhost:55001/jhu?charset=utf8mb4'
engine = create_engine(uri,echo=True,future=True)

# 创建表格
stmt = text('create table demo_user(id integer, name varchar(256))')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

# 插入单行数据
stmt = text("insert into demo_user values(:id,:name)").bindparams(id=1,name='jack')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

# 插入多行数据
stmt = text("insert into demo_user values(:id,:name)")
with engine.connect() as conn:
    conn.execute(stmt,[dict(id=2,name='rose'),dict(id=3,name='eva')])
    conn.commit()a

# 查询数据
stmt = text('select * from demo_user')
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row.id,row.name)
        print(row['id'],row['name'])
    for row in result.mappings():
        print(row['id'])

# 单行更新&批量更新
stmt = text('update demo_user set name=:name where id=:id').bindparams(id=1,name='jack-1')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

stmt = text('update demo_user set name=:name where id=:id')
with engine.connect() as conn:
    conn.execute(stmt,[dict(id=2,name='rose-2'),dict(id=3,name='eva-3')])
    conn.commit()

# 移除表格
stmt = text('drop table demo_user')
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
