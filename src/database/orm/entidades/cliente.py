from src.model.cliente import Cliente
from sqlalchemy import Column, Table, Integer, String
from src.database.settings.base import registry_base

tabela_cliente = Table(
    "clientes",
    registry_base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nome", String(50), nullable=False),
    Column("limite", Integer, nullable=False),
    Column("saldo", Integer, nullable=False, default=0),
)

mapper_cliente = registry_base.map_imperatively(Cliente, tabela_cliente)
