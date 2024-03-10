from datetime import datetime
from pydantic import BaseModel


class TransacaoDoExtrato(BaseModel):
    valor: int
    tipo: str
    descricao: str
    realizada_em: datetime


class SaidaSaldo(BaseModel):
    total: int
    limite: int
    data_extrato: datetime


class SaidaExtrato(BaseModel):
    saldo: SaidaSaldo
    ultimas_transacoes: list[TransacaoDoExtrato]
