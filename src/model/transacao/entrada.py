from pydantic import BaseModel, field_validator
from enum import Enum
from src.errors.error_exception import EntradaInvalida


class TipoDeCredito(str, Enum):
    d = "d"
    c = "c"


class EntradaTransacao(BaseModel):
    valor: int
    tipo: TipoDeCredito
    descricao: str

    @field_validator("valor")
    def validate_valor(cls, value):
        if value < 0:
            raise EntradaInvalida()
        return value

    @field_validator("descricao")
    def validate_descricao(cls, value):
        if value == "":
            raise EntradaInvalida()
        if len(value) > 10:
            raise EntradaInvalida()
        return value

    @field_validator("tipo")
    def validate_tipo(cls, value):
        if value not in ["c", "d"]:
            raise EntradaInvalida()
        return value
