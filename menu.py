from funcoes import cadastroproduto, consultarproduto, vendaproduto, comprarproduto, listarproduto, \
    cadastrocliente, procurarcliente, infovalida, salvarcliente, excluir_clientes, excluir_produto, salvarproduto, carregar_clientes, carregar_produtos, listarcliente
from time import sleep
import os

listadeclientes = carregar_clientes()
listadeprodutos = carregar_produtos()
while True:

    print('''[1] - CADASTRAR PRODUTO      [6] - CADASTRAR CLIENTE
[2] - EXCLUIR PRODUTO        [7] - EXCLUIR CLIENTE
[3] - COMPRA DE PRODUTO      [8] - LISTAR CLIENTES
[4] - VENDA DE PRODUTOS      [9] - SAIR
[5] - LISTAR PRODUTOS       ''')
    

    usuario = input('\nDIGITE UMA OÇÃO: ')
    match usuario:
        case '1':
            cadastroproduto(listadeprodutos)
            salvarproduto(listadeprodutos)
        case '2':
            excluir_produto(listadeprodutos)
        case '3':
            id_compra= int(input("Digite o id do produto para compra: "))
            quantidade_compra = int(input("Digite a quantidade do produto para compra: "))
            comprarproduto(id_compra, quantidade_compra, listadeprodutos)
        case '4':
            vendaproduto(listadeprodutos, listadeclientes)
            salvarcliente(listadeclientes)
        case '5':
            listarproduto(listadeprodutos)
        case '6':
            cadastrocliente(listadeclientes)
            salvarcliente(listadeclientes)
        case '7':
            excluir_clientes(listadeclientes)
        case '8':
           listarcliente(listadeclientes)
        case '9':
            print("ENCERRANDO...")
            exit()
        case _:
            print("OPÇÃO INVÁLIDA")


  