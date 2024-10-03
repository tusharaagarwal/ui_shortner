from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#engine
#session

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/url_shortner"
engine = create_engine(
DATABASE_URL,connect_args={}
)
sessionlocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()