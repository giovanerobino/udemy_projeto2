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
    print('================================')
    print('========= Bem Vindo(a) =========')
    print('======= Mercado Central ========')
    print('================================')

    print('Selecione uma das opções abaixo: ')
    print('1 - Cadastrar Novo Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Novo Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Finalizar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fehar_pedido()
    elif opcao == 6:
        print('Saindo do sistema...')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida. Tente novamente.')
        sleep(1)
        menu()



def cadastrar_produto() -> None:
    """Função para cadastrar um novo produto"""
    print('Cadastro de Produtos')
    print('====================')

    nome: str = input('Nome do Produto: ')
    preco: float = float(input('Preço do Produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    """Função para mostrar todos os produtos"""
    if len(produtos) > 0:
        print('Produtos Cadastrados:')
        print('---------------------')

        for produto in produtos:
            print(produto)
            print('---------------------')
            sleep(1)
    else:
        print('Não há produtos cadastrados.')
    sleep(1)
    menu()


def comprar_produto() -> None:
    """Função para comprar um novo produto"""
    if len(produtos) > 0:
        print('Informe o nome do produto que deseja adicionar ao carrinho: ')
        print('-----------------------------------------------------------')
        print('================== Produtos Disponíveis ===================')

        for produto in produtos:
            print(produto)
            print('-----------------------------------------------------------')
            sleep(1)
        
        codigo: int = int(input())
        produto: Produto = pega_produto_id(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)

                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora tem {quant + 1} unidade(s) no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Não há produtos desse tipo para vender.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    """Função para mostrar o carrinho de compras"""
    if len(carrinho) > 0:
        print('Produtos no Carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------')
                sleep(1)
    else:
        print('O carrinho esta vazio.')
    sleep(2)
    menu()


def fehar_pedido() -> None:
    """Função para fechar o pedido"""
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Resumo do pedido:')
        print('-----------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')

                valor_total += dados[0].preco * dados[1]

                print('-----------------')
                sleep(1)
        print(f"Valor Total: {formata_float_str_moeda(valor_total)} \nVolte Sempre!")
        carrinho.clear()
        sleep(5)
    else:
        print('Não há produtos no carrinho.')
    sleep(2)
    menu()


def pega_produto_id(codigo: int) -> Produto:
    """Função para pegar um produto pelo seu código"""
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p




if __name__ == '__main__':
    main()
