from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de base de datos SQLite:
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Crea el motor de base de datos:
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crea una sesión de base de datos:
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una clase base para declarar clases de modelo SQLAlchemy:
Base = declarative_base()
