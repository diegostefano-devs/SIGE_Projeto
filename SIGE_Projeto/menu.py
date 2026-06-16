from funcoes import (cadastroproduto, vendaproduto, comprarproduto, listarproduto, \
                     cadastrocliente, salvarcliente, excluir_clientes, excluir_produto, salvarproduto,
                     carregar_clientes, carregar_produtos, listarcliente, gerar_relatorio_venda,
                     gerar_relatorio_cliente)
from time import sleep
import os

listadeclientes = carregar_clientes()
listadeprodutos = carregar_produtos()
while True:

    print('''[1] - CADASTRAR PRODUTO      
[2] - EXCLUIR PRODUTO        [7] - EXCLUIR CLIENTE
[3] - COMPRA DE PRODUTO      [8] - LISTAR CLIENTES
[4] - VENDA DE PRODUTOS      [9] - GERAR RELATÓRIO DE CLIENTES
[5] - LISTAR PRODUTOS        [10] - GERAR RELATÓRIO DE VENDAS
[6] - CADASTRAR CLIENTE      [11] - SAIR
      ''')
    

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
            gerar_relatorio_cliente(listadeclientes)
        case '10':
            gerar_relatorio_venda()
        case '11':
            print("ENCERRANDO...")
            exit()
        case _:
            print("OPÇÃO INVÁLIDA")


  