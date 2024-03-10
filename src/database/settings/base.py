from sqlalchemy.orm import registry, DeclarativeBase, declarative_base
from sqlalchemy import MetaData

Base = declarative_base()
metadata = MetaData()

registry_base = registry()
