from funcoes import cadastroproduto, consultarproduto, vendaproduto, comprarproduto, listarproduto, \
    cadastrocliente, procurarcliente, listarcliente

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
    usuario = input(
        "Digite uma opção\n"
        "1)Cadastrar produto\n"
        "2)Consultar produto\n"
        "3)Compra de produto\n"
        "4)Venda de produto\n"
        "5)Listar produtos\n"
        "6)Cadastrar cliente\n"
        "7)Listar clientes\n"
        "8)Sair\n"
    )
    if usuario == "1":
        # Cadastro de produto
        id = int(input("Digite o id do produto: "))
        nome = input("Digite o nome do produto: ")
        descricao = input(("Digite uma descrição do produto: "))
        tamanho = input("Digite o tamanho do produto: ")
        quantidade = int(input("Digite o quantidade do produto: "))
        # Adciona as informações dentro do dict produto
        produto = {
            "id": id,
            "nome": nome,
            "descricao": descricao,
            "tamanho": tamanho,
            "quantidade": quantidade
        }
        print(listadeprodutos)
        # chama a função de cadastro de produto para cadastrar o dict produto dentro da lista de produtos
        # todas as validações de quantidade, id duplicado é feia dentro da função cadastro de produto
        cadastroproduto(produto, listadeprodutos)

    elif usuario == "2":
        id = int(input("Digite o id do produto: "))
        consultarproduto(id, listadeprodutos)

    elif usuario == "3":
        id_compra= int(input("Digite o id do produto para compra: "))
        quantidade_compra = int(input("Digite a quantidade do produto para compra: "))
        comprarproduto(id_compra, quantidade_compra, listadeprodutos)

    elif usuario == "4":
        id_venda = int(input("Digite o id do produto para venda: "))
        quantidade_venda = int(input("Digite a quantidade do produto para venda: "))
        nome_cliente = str(input("Digite o nome do cliente: "))
        # a função procura cliente vai percorrer a lista de clientes para verificar se há clientes cadastrados

        cliente = procurarcliente(nome_cliente, listadeclientes)

        if cliente is None:
            print("Não existe esse cliente")
        else:
            vendaproduto(id_venda, listadeprodutos, quantidade_venda, cliente)


    elif usuario == "5":
       listarproduto(listadeprodutos)

    elif usuario == "6":
        nome = str(input("Digite o nome do cliente: "))
        cpf = str(input("Digite o cpf do cliente: "))
        endereco = str(input("Digite o endereço do cliente: "))
        telefone = str(input("Digite o telefone do cliente: "))
        # a função cadastro cliente é utilizada para toda vez que é necessário o cadastro
        cliente = cadastrocliente(nome, cpf, telefone, endereco)
        # depois adciona o cliente cadastrado na lista de clientes
        listadeclientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    elif usuario == "7":
        listarcliente(listadeclientes)

    elif usuario == "8":
        print("Saindo do programa")
        exit()