from dataclasses import dataclass
from typing import Optional

from fastapi import HTTPException


@dataclass
class FastException(HTTPException):
    detail: str
    status_code: int
    description: Optional[str] = None

    def _str_(self):
        return self.detail


@dataclass
class EntradaInvalida(FastException):
    detail: str = "Entrada inválida"
    status_code: int = 422


@dataclass
class NaoEncontrado(FastException):
    detail: str = "Não encontrado"
    status_code: int = 404
