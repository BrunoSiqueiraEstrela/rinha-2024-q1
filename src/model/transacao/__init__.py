from datetime import datetime


class Transacao:
    id: int
    cliente_id: int
    valor: int
    tipo: str
    descricao: str
    realizada_em: datetime

    @classmethod
    def criar(
        cls,
        cliente_id: int,
        valor: int,
        tipo: str,
        descricao: str,
    ) -> "Transacao":
        return cls(
            cliente_id=cliente_id,
            valor=valor,
            tipo=tipo,
            descricao=descricao,
            realizada_em=datetime.now(),
        )

    def __repr__(self) -> str:
        return f"<Transacao( valor={self.valor!r}, tipo={self.tipo!r}, descricao={self.descricao!r}, realizada_em={self.realizada_em!r})>"
