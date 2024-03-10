from src.model.transacao import Transacao as TransacaoModel
from sqlalchemy import Column, Table, Integer, String, DateTime, ForeignKey, func
from src.database.settings.base import registry_base

tabela_transacao = Table(
    "transacoes",
    registry_base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("cliente_id", Integer, ForeignKey("clientes.id")),
    Column("valor", Integer, nullable=False),
    Column("tipo", String(1), nullable=False),
    Column("descricao", String(10), nullable=False),
    Column("realizada_em", DateTime, nullable=False, default=func.now()),
)

mapper_transacao = registry_base.map_imperatively(TransacaoModel, tabela_transacao)
