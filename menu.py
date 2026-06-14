from funcoes import cadastroproduto, consultarproduto, vendaproduto, comprarproduto, listarproduto, \
    cadastrocliente, procurarcliente, listarcliente, infovalida, salvarcliente
from time import sleep
import os

listadeprodutos = [
    {
        "id": 1,
        "nome": "VESTIDO FLORAl",
        "descricao": "VESTIDO INFANTIL ESTAMPADO FLORAL",
        "tamanho": "P",
        "quantidade": 12
    },
    {
        "id": 2,
        "nome": "CONJUNTO VERÃO",
        "descricao": "CONJUNTO CAMISETA E SHORT",
        "tamanho": "M",
        "quantidade": 20
    },
    {
        "id": 3,
        "nome": "MACACÃO JEANS",
        "descricao": "MACACÃO INFANTIL JEANS",
        "tamanho": "G",
        "quantidade": 8
    },
    {
        "id": 4,
        "nome": "CAMISETA DINO",
        "descricao": "CAMISETA ESTAMPADA DINOSSAURO",
        "tamanho": "6",
        "quantidade": 15
    },
    {
        "id": 5,
        "nome": "SHORT JEANS",
        "descricao": "SHORT JEANS INFANTIL",
        "tamanho": "4",
        "quantidade": 18
    },
    {
        "id": 6,
        "nome": "PIJAMA ESTRELAS",
        "descricao": "PIJAMA INFANTIL CONFORTÁVEL",
        "tamanho": "8",
        "quantidade": 10
    },
    {
        "id": 7,
        "nome": "VESTIDO FESTA",
        "descricao": "VESTIDO INFANTIL PARA FESTA",
        "tamanho": "2",
        "quantidade": 6
    },
    {
        "id": 8,
        "nome": "JAQUETA INFANTIL",
        "descricao": "JAQUETA DE FRIO INFANTIL",
        "tamanho": "10",
        "quantidade": 5
    },
    {
        "id": 9,
        "nome": "BODY BEBÊ",
        "descricao": "BODY MANGA CURTA BEBÊ",
        "tamanho": "RN",
        "quantidade": 25
    },
    {
        "id": 10,
        "nome": "TÊNIS INFANTIL",
        "descricao": "TÊNIS CASUAL INFANTIL",
        "tamanho": "28",
        "quantidade": 9
    }
]
listadeclientes = [
    {
        "nome": "MARIA SILVA",
        "cpf": "11111111111",
        "telefone": "74999990001",
        "endereco": "RUA DAS FLORES, 101",
        "produtos": []
    },
    {
        "nome": "JOÃO SOUZA",
        "cpf": "22222222222",
        "telefone": "74999990002",
        "endereco": "RUA CENTRAL, 45",
        "produtos": []
    },
    {
        "nome": "ANA OLIVEIRA",
        "cpf": "33333333333",
        "telefone": "74999990003",
        "endereco": "AV. BAHIA, 200",
        "produtos": []
    },
    {
        "nome": "CARLOS SANTOS",
        "cpf": "44444444444",
        "telefone": "74999990004",
        "endereco": "RUA PRIMAVERA, 78",
        "produtos": []
    },
    {
        "nome": "FERNANDA LIMA",
        "cpf": "55555555555",
        "telefone": "74999990005",
        "endereco": "RUA DO COMÉRCIO, 90",
        "produtos": []
    },
    {
        "nome": "PEDRO ROCHA",
        "cpf": "66666666666",
        "telefone": "74999990006",
        "endereco": "RUA SÃO JOSÉ, 300",
        "produtos": []
    },
    {
        "nome": "JULIANA ALVES",
        "cpf": "77777777777",
        "telefone": "74999990007",
        "endereco": "RUA NOVA, 55",
        "produtos": []
    },
    {
        "nome": "LUCAS PEREIRA",
        "cpf": "88888888888",
        "telefone": "74999990008",
        "endereco": "RUA DAS PALMEIRAS, 18",
        "produtos": []
    },
    {
        "nome": "CAMILA COSTA",
        "cpf": "99999999999",
        "telefone": "74999990009",
        "endereco": "RUA HORIZONTE, 410",
        "produtos": []
    },
    {
        "nome": "RAFAEL MARTINS",
        "cpf": "10101010101",
        "telefone": "74999990010",
        "endereco": "RUA ESPERANÇA, 77",
        "produtos": []
    }
]

while True:
    # Menu de opções
    print(
        "\n1)Cadastrar produto\n"
        "2)Consultar produto\n"
        "3)Compra de produto\n"
        "4)Venda de produto\n"
        "5)Listar produtos\n"
        "6)Cadastrar cliente\n"
        "7)Listar clientes\n"
        "8)Sair\n"
    )

    usuario = input('Digite uma opção: ')
    match usuario:
        case '1':
            cadastroproduto(listadeprodutos)
        case '2':
            id = int(input("Digite o id do produto: "))
            consultarproduto(id, listadeprodutos)
        case '3':
            id_compra= int(input("Digite o id do produto para compra: "))
            quantidade_compra = int(input("Digite a quantidade do produto para compra: "))
            comprarproduto(id_compra, quantidade_compra, listadeprodutos)
        case '4':
            vendaproduto(listadeprodutos, listadeclientes)
        case '5':
            listarproduto(listadeprodutos)
        case '6':
            cadastrocliente(listadeclientes)
            salvarcliente(listadeclientes)
        case '7':
            with open('clientes.txt', 'r', encoding=('utf-8')) as arquivo:
                contador = 0
                for ler in arquivo:
                    print(ler, end='')
                    contador += 1

                    if contador == 4:
                        print("------------------------------------\n")
                        contador = 0

        case '8':
            print("ENCERRANDO...")
            exit()
        case _:
            print("OPÇÃO INVÁLIDA")


  