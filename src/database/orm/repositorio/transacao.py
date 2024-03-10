from typing import Optional
from src.model.transacao import Transacao
from src.model.extrato import TransacaoDoExtrato
from src.database.manager import DBConnection
from sqlalchemy import text


class RepositorioDeTransacao:
    @classmethod
    def registrar_transacao(cls, transacao: Transacao) -> Optional[Transacao]:
        with DBConnection() as database:
            with database.session.begin():
                database.session.add(transacao)
                database.session.commit()

    @classmethod
    def pegar_extrato(cls, cliente_id: int) -> list[TransacaoDoExtrato]:
        with DBConnection() as database:
            with database.session.begin():
                query = "SELECT valor, tipo, descricao, realizada_em FROM transacoes WHERE cliente_id = :cliente_id ORDER BY realizada_em DESC LIMIT 10 FOR UPDATE;"
                resultado: list[TransacaoDoExtrato] = database.session.execute(
                    text(query), {"cliente_id": cliente_id}
                ).all()

                return resultado
