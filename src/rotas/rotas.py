import datetime
from fastapi import APIRouter
from src.model.transacao.entrada import EntradaTransacao
from src.model.transacao.saida import SaidaTransacao
from src.model.extrato import SaidaExtrato, SaidaSaldo, TransacaoDoExtrato
from src.errors.error_exception import EntradaInvalida, NaoEncontrado
from src.database.orm.repositorio.transacao import RepositorioDeTransacao
from src.database.orm.repositorio.cliente import RepositorioDeCliente
from src.model.transacao import Transacao


rotas = APIRouter()


@rotas.post("/clientes/{id}/transacoes")
async def transacao_do_cliente(id: int, transacao: EntradaTransacao):
    resposta = None

    repo_transacao = RepositorioDeTransacao()
    repo_cliente = RepositorioDeCliente()

    cliente = repo_cliente.pesquisar_id(id)

    if cliente is None:
        raise NaoEncontrado()

    if transacao.descricao == "danada":
        print("danada")

    if transacao.descricao == "vlCXZpQSkm":
        print("vlCXZpQSkm")

    if transacao.descricao == "JHjuVcPUjC":
        print("JHjuVcPUjC")

    nova_transacao = Transacao.criar(
        cliente_id=id,
        valor=transacao.valor,
        tipo=transacao.tipo,
        descricao=transacao.descricao,
    )

    match transacao.tipo:

        case "d":

            if (cliente.saldo - transacao.valor) >= (cliente.limite * -1):

                cliente.saldo -= transacao.valor
                repo_transacao.registrar_transacao(nova_transacao)
                repo_cliente.atualizar_saldo(cliente)
                resposta = {"limite": cliente.limite, "saldo": cliente.saldo}

        case "c":
            cliente.saldo += transacao.valor
            repo_transacao.registrar_transacao(nova_transacao)
            repo_cliente.atualizar_saldo(cliente)
            resposta = {"limite": cliente.limite, "saldo": cliente.saldo}

    resposta = {"limite": cliente.limite, "saldo": cliente.saldo}

    return SaidaTransacao(**resposta)


@rotas.get("/clientes/{id}/extrato")
async def extrato_do_cliente(id: int):

    cliente = None
    repo_cliente = RepositorioDeCliente()
    repo_transacao = RepositorioDeTransacao()
    cliente = repo_cliente.pesquisar_id(id)
    if cliente is None:

        raise NaoEncontrado()

    lista_de_transacao = repo_transacao.pegar_extrato(id)

    lista_de_transacoes = []

    for transacao in lista_de_transacao:
        lista_de_transacoes.append(
            TransacaoDoExtrato(
                valor=transacao.valor,
                tipo=transacao.tipo,
                descricao=transacao.descricao,
                realizada_em=transacao.realizada_em,
            )
        )
    saida = SaidaSaldo(
        total=cliente.saldo,
        data_extrato=datetime.datetime.now().isoformat(),
        limite=cliente.limite,
    )

    return SaidaExtrato(saldo=saida, ultimas_transacoes=lista_de_transacoes)
