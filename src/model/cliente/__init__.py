class Cliente:
    id: int
    nome: str
    limite: int
    saldo: str

    def __repr__(self) -> str:
        return f"<Cliente(id={self.id!r},nome={self.nome!r})>"
