  
def infovalida (chave, valor_procurado, lista_de_dados):
    for item in lista_de_dados:
        if item[chave] == valor_procurado:
            return True
    return False
            

def cadastroproduto(listadeprodutos):
    print('\n############## CADASTRO DE PRODUTOS ##########\n')

    #Validação para garantir que o ID cadastrado seja único
    while True:
        id = int(input("Digite o id do produto: "))

        if infovalida('id', id, listadeprodutos):
            print("\nERROR: ID já cadastrado no sistema")
        else:
            break

    nome = input("Digite o nome do produto: ").strip().upper()
    descricao = input(("Digite uma descrição do produto: ")).strip().upper()
    tamanho = input("Digite o tamanho do produto: ")
    
    while True:
        quantidade = int(input("Digite o quantidade do produto: "))
        if quantidade < 0:
            print("\nERROR: Não é possível cadastrar quantidade negativa")
        else: 
            break    

    produto = {
            "id": id,
            "nome": nome,
            "descricao": descricao,
            "tamanho": tamanho,
            "quantidade": quantidade
        }
    
    listadeprodutos.append(produto)
    print("PRODUTO CADASTRADO COM SUCESSO!\n")
    
    
def consultarproduto(id,listadeprodutos ):
    # o for vai percorrer todos os id dentro da lista listadeprodutos
    for produto in listadeprodutos:
        if produto["id"] == id:
                mostrarproduto(produto)

                return
    # esse print está fora do if (funciona como um else), pq se o código não entrar dentro do if,
    # vai retornar o que está no print
    print("ERROR: Produto não encontrado")

def comprarproduto(id,quantidade_compra, listadeprodutos):
    # Verifica se a quantidade de compra é menor ou igual a zero
    if quantidade_compra <= 0:
        print("ERROR: Quantidade inválida.")
        return

    # O for procura o produto pelo id e depois aumenta a quantidade do produto
    for produto in listadeprodutos:
        if produto["id"] == id:
            produto["quantidade"] += quantidade_compra
            print("Compra realizada com sucesso")
            mostrarproduto(produto)

            return produto
    print("Produto não encontrado")
    # esse print está fora do if (funciona como um else), pq se o código não entrar dentro do if,
    # vai retornar o que está no print

def vendaproduto(id, listadeprodutos, quantidade_venda, cliente):
    # percore a listra de produto
    for produto in listadeprodutos:
        # verifica se há um id igual ao procurado pelo cliente
        if produto["id"] == id:
            if quantidade_venda > produto["quantidade"]:
                # verifica se a quantidade de venda é maior do que a quant de estoque
                print("Estoque insuficiente.")
                return None
                print("Produto adcionado com sucesso!")
            # está fora da identação do if de quantidade, funciona como um else
            produto["quantidade"] -= quantidade_venda
            # dimimui a quantidade de produto que foi vendido
            # cadastra produto vendido no cliente
            cliente["produtos"].append({
                "id": produto["id"],
                "nome": produto["nome"],
                "descricao": produto["descricao"],
                "tamanho": produto["tamanho"],
                "quantidade": quantidade_venda
            })

            print("Venda realizada com sucesso!")
            print("Produto adicionado ao cliente.")

            mostrarproduto(produto)

            return produto
    print("Produto não encontrado")
    # se não entrar em nenhum bloco de código, então o produto não existe

def listarproduto(listadeprodutos):
    # se não listadeprodutos, se ela estiver vazia, não há produto cadastrado
    if not listadeprodutos:
        print("Nenhum produto cadastrado.")
        return

    for produto in listadeprodutos:
        mostrarproduto(produto)
    return listadeprodutos

def listarcliente(listadeclientes):
    if not listadeclientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in listadeclientes:
        print(
            f"\nNome: {cliente['nome']}"
            f"\nCPF: {cliente['cpf'][:3]}-{cliente['cpf'][3:6]}-{cliente['cpf'][6:9]}.{cliente['cpf'][9:]}"
            f"\nTelefone: ({cliente['telefone'][:2]}) {cliente['telefone'][2:7]}-{cliente['telefone'][7:]}"
            f"\nEndereço: {cliente['endereco']}"
            f"\nProdutos: {cliente['produtos']}"
        )

def cadastrocliente(listadecliente):
    nome = str(input("Digite o nome do cliente: ")).strip().upper()

    #Validação de CPF
    while True:
        cpf = str(input("Digite o cpf do cliente: "))
        if len(cpf) != 11:
            print("\nERROR: CPF inválido. Coloque uma informação válida.")
        else:
            break

    while True:
        if infovalida('cpf', cpf, listadecliente):
            print("\nERROR: CPF já existe no banco de daods.")
            cpf = str(input("Digite o cpf do cliente: "))
        else:
            break

    #Validação de telefone
    while True:
        telefone = str(input("Digite o telefone do cliente: "))
        if len(telefone) != 11:
            print("\nERROR: Número inválido. Coloque uma informação válida.")
        else:
            break

    endereco = str(input("Digite o endereço do cliente: ")).strip().upper()

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "telefone": telefone,
        "produtos": []
    }

    listadecliente.append(cliente)
    print("Cliente cadastrado com sucesso!")

def procurarcliente(nome_cliente, listadeclientes):
    # Procurar na base de dados se existe o cliente para cadastro de venda
    for cliente in listadeclientes:
        if cliente["nome"] == nome_cliente:
            return cliente

def mostrarproduto(produto):

    print(
        f"ID: {produto['id']}\n"
        f"Nome: {produto['nome']}\n"
        f"Descrição: {produto['descricao']}\n"
        f"Tamanho: {produto['tamanho']}\n"
        f"Quantidade: {produto['quantidade']}\n"
    )