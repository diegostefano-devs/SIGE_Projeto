from funcoes import cadastroproduto, consultarproduto, vendaproduto, comprarproduto, listarproduto, \
    cadastrocliente, procurarcliente, listarcliente, infovalida
from time import sleep
import os

listadeprodutos = [
    {
        "id": 1,
        "nome": "Vestido Floral",
        "descricao": "Vestido infantil estampado floral",
        "tamanho": "P",
        "quantidade": 12
    },
    {
        "id": 2,
        "nome": "Conjunto Verão",
        "descricao": "Conjunto camiseta e short",
        "tamanho": "M",
        "quantidade": 20
    },
    {
        "id": 3,
        "nome": "Macacão Jeans",
        "descricao": "Macacão infantil jeans",
        "tamanho": "G",
        "quantidade": 8
    },
    {
        "id": 4,
        "nome": "Camiseta Dino",
        "descricao": "Camiseta estampada dinossauro",
        "tamanho": "6",
        "quantidade": 15
    },
    {
        "id": 5,
        "nome": "Short Jeans",
        "descricao": "Short jeans infantil",
        "tamanho": "4",
        "quantidade": 18
    },
    {
        "id": 6,
        "nome": "Pijama Estrelas",
        "descricao": "Pijama infantil confortável",
        "tamanho": "8",
        "quantidade": 10
    },
    {
        "id": 7,
        "nome": "Vestido Festa",
        "descricao": "Vestido infantil para festa",
        "tamanho": "2",
        "quantidade": 6
    },
    {
        "id": 8,
        "nome": "Jaqueta Infantil",
        "descricao": "Jaqueta de frio infantil",
        "tamanho": "10",
        "quantidade": 5
    },
    {
        "id": 9,
        "nome": "Body Bebê",
        "descricao": "Body manga curta bebê",
        "tamanho": "RN",
        "quantidade": 25
    },
    {
        "id": 10,
        "nome": "Tênis Infantil",
        "descricao": "Tênis casual infantil",
        "tamanho": "28",
        "quantidade": 9
    }
]
listadeclientes = [
    {
        "nome": "Maria Silva",
        "cpf": "11111111111",
        "telefone": "74999990001",
        "endereco": "Rua das Flores, 101",
        "produtos": []
    },
    {
        "nome": "João Souza",
        "cpf": "22222222222",
        "telefone": "74999990002",
        "endereco": "Rua Central, 45",
        "produtos": []
    },
    {
        "nome": "Ana Oliveira",
        "cpf": "33333333333",
        "telefone": "74999990003",
        "endereco": "Av. Bahia, 200",
        "produtos": []
    },
    {
        "nome": "Carlos Santos",
        "cpf": "44444444444",
        "telefone": "74999990004",
        "endereco": "Rua Primavera, 78",
        "produtos": []
    },
    {
        "nome": "Fernanda Lima",
        "cpf": "55555555555",
        "telefone": "74999990005",
        "endereco": "Rua do Comércio, 90",
        "produtos": []
    },
    {
        "nome": "Pedro Rocha",
        "cpf": "66666666666",
        "telefone": "74999990006",
        "endereco": "Rua São José, 300",
        "produtos": []
    },
    {
        "nome": "Juliana Alves",
        "cpf": "77777777777",
        "telefone": "74999990007",
        "endereco": "Rua Nova, 55",
        "produtos": []
    },
    {
        "nome": "Lucas Pereira",
        "cpf": "88888888888",
        "telefone": "74999990008",
        "endereco": "Rua das Palmeiras, 18",
        "produtos": []
    },
    {
        "nome": "Camila Costa",
        "cpf": "99999999999",
        "telefone": "74999990009",
        "endereco": "Rua Horizonte, 410",
        "produtos": []
    },
    {
        "nome": "Rafael Martins",
        "cpf": "10101010101",
        "telefone": "74999990010",
        "endereco": "Rua Esperança, 77",
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
            id_venda = int(input("Digite o id do produto para venda: "))
            quantidade_venda = int(input("Digite a quantidade do produto para venda: "))
            nome_cliente = str(input("Digite o nome do cliente: "))
            # a função procura cliente vai percorrer a lista de clientes para verificar se há clientes cadastrados

            cliente = procurarcliente(nome_cliente, listadeclientes)

            if cliente is None:
                print("Não existe esse cliente")
            else:
                vendaproduto(id_venda, listadeprodutos, quantidade_venda, cliente)

        case '5':
            listarproduto(listadeprodutos)
        case '6':
            cadastrocliente(listadeclientes)
        case '7':
            listarcliente(listadeclientes)
        case '8':
            print("ENCERRANDO...")
            exit()
        case _:
            print("OPÇÃO INVÁLIDA")


  