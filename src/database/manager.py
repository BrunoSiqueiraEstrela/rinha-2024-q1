from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import NullPool
from src.database.settings.entities import load_tables
from src.configs.variaveis.gerenciador import env


class DBConnection:
    __connection_string: str = None
    session: Session = None
    commited: bool = False

    def __init__(self, connection_string: str = None):
        load_tables()
        if connection_string is not None:
            self.__connection_string = connection_string
        else:
            self.__connection_string = env.DB_STRING_CONNECTION

        self.session = None

    def get_engine(self):
        """
        Returns the SQLAlchemy engine for the database connection.
        """
        return create_engine(
            self.__connection_string,
            poolclass=NullPool,
            echo=False,
        )

    def __enter__(self):
        self.commited = False

        engine = self.get_engine()
        session_maker = sessionmaker(
            autoflush=True,
            expire_on_commit=False,
        )
        self.session = session_maker(bind=engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_session()

    def add(self, entity):
        self.session.add(entity)

    def update(self, entity):
        self.session.merge(entity)

    def commit(self):
        self.session.commit()
        self.session.expunge_all()
        self.commited = True

    def rollback(self):
        if hasattr(self, "session"):
            self.session.rollback()

    def close_session(self):
        if hasattr(self, "session"):
            self.session.close()
