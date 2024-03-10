from sqlalchemy.orm import registry, DeclarativeBase
from sqlalchemy import MetaData

Base = DeclarativeBase()
metadata = MetaData()

registry = registry()
