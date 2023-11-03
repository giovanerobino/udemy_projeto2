"""
produto.py - Código para o projeto 2 de POO com Python
"""
from utils.helper import formata_float_str_moeda


class Produto:
    """ Classe para representar um Produto """

    contador: int = 1


    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        """Retorna o código do produto"""
        return self.__codigo

    @property
    def nome(self: object) -> str:
        """Retorna o nome do produto"""
        return self.__nome

    @property
    def preco(self: object) -> float:
        """Retorna o preço do produto"""
        return self.__preco

    def __str__(self) -> str:
        """Retorna uma representação em string do objeto"""
        return (f'Código: {self.codigo} \n'
                f'Nome: {self.nome} \n'
                f'Preço: {formata_float_str_moeda(self.preco)}')
