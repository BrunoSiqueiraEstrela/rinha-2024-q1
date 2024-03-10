from typing import Optional
from src.model.cliente import Cliente
from src.database.manager import DBConnection


class RepositorioDeCliente:
    @classmethod
    def pesquisar_id(cls, cliente_id: str) -> Optional[Cliente]:
        with DBConnection() as database:
            try:
                usuario_achado = (
                    database.session.query(Cliente)
                    .filter(Cliente.id == cliente_id)
                    .first()
                )
                return usuario_achado
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def pegar_saldo(cls, cliente_id: int) -> Optional[int]:
        with DBConnection() as database:
            try:
                saldo = (
                    database.session.query(Cliente.saldo)
                    .filter(Cliente.id == cliente_id)
                    .first()
                )
                return saldo
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def atualizar_saldo(cls, cliente: Cliente) -> Optional[Cliente]:
        with DBConnection() as database:
            try:
                resultado_cliente = database.session.add(cliente)
                database.session.commit()
                return resultado_cliente
            except Exception as exception:
                database.session.rollback()
                raise exception
