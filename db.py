from sqlmodel import create_engine

sqlite_url = "sqlite:///./db.sqlite"
engine = create_engine(sqlite_url, echo=True)
