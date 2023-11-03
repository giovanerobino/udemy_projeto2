"""
mercado.py - Código principal para o projeto 2 Mercado
"""
from typing import List, Dict
from time import sleep
from utils.helper import formata_float_str_moeda
from models.produto import Produto


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    """Função principal do projeto com menus"""
    menu()


def menu() -> None:
    """Função para mostrar o menu principal"""
    pass


def cadastrar_produto() -> None:
    """Função para cadastrar um novo produto"""
    pass


def listar_produtos() -> None:
    """Função para mostrar todos os produtos"""
    pass


def comprar_produto() -> None:
    """Função para comprar um novo produto"""
    pass


def visualizar_carrinho() -> None:
    """Função para mostrar o carrinho de compras"""
    pass


def fehar_pedido() -> None:
    """Função para fechar o pedido"""
    pass


def pega_produto_id(codigo: int) -> Produto:
    """Função para pegar um produto pelo seu código"""
    pass




if __name__ == '__main__':
    main()
