from sqlalchemy import create_engine, MetaData
from clickhouse_sqlalchemy import make_session, get_declarative_base

db_url = 'clickhouse://backend:000000@46.243.227.152:8123/default'
engine = create_engine(db_url)

session = make_session(engine)
metadata = MetaData(bind=engine)

Base = get_declarative_base(metadata=metadata)
