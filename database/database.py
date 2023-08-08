from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:9cwpqlb93HBNPQJi@db.infiaecuahtfowgmqjoq.supabase.co:6543/postgres"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()