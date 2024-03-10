from pydantic import BaseModel


class SaidaTransacao(BaseModel):
    limite: int
    saldo: int
