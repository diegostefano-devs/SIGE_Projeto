  
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
    print('\n############## CONSULTA DE PRODUTOS ##########\n')
    # o for vai percorrer todos os id dentro da lista listadeprodutos
    for produto in listadeprodutos:
        if produto["id"] == id:
                mostrarproduto(produto)

                return
    # esse print está fora do if (funciona como um else), pq se o código não entrar dentro do if,
    # vai retornar o que está no print
    print("ERROR: Produto não encontrado")

def comprarproduto(id,quantidade_compra, listadeprodutos):
    print('\n############## COMPRA DE PRODUTOS ##########\n')
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

def vendaproduto(listadeprodutos, listadeclientes):
    print('\n############## PONTO DE VENDA ##########\n')

    # VARIAVEIS VAZIAS PARA PRODUTO E CLIENTE
    produto_encontrado = None
    cliente_encontrado = None

    # LOOPING PARA ENCONTRAR PRODUTO
    while True:
        id_venda = int(input("Digite o id do produto para venda: "))
        if not infovalida('id', id_venda, listadeprodutos):
            print("\nERROR: Insira uma informação válida.")
        else:
            break
    # CASO O ID EXISTA, UTILZAMOS ESSE LAÇO DE REPETIÇÃO PARA DESCOBRIR A QUEM ELE PERTENCE E ASSOCIA-LO A VÁRIAVEL VAZIA DE PRODUTO
    for produto in listadeprodutos:
        if produto['id'] == id_venda:
            produto_encontrado = produto
            break
    
    # MOSTRA O AS INFORMAÇÕES DO PRODUTO
    print('\nPRODUTO ENCONTRADO:')
    print(f'''
        ID: {produto_encontrado['id']}
        NOME: {produto_encontrado['nome']}
        QUANTIDADE: {produto_encontrado['quantidade']}
 ''')
    
    # LOOPING PARA O USUÁRIO POR UMA INFORMAÇÃO DE ESTOQUE CORRETA
    while True:
        quantidade_venda = int(input("Digite a quantidade do produto para venda: "))
        if quantidade_venda <= 0:
            print("ERROR: Insira uma informação válida.")
        elif quantidade_venda > produto_encontrado['quantidade']:
            print("\nERROR: Estoque insuficiente")
        else: 
            break
    
    # LOOPING PARA FINALIZAR A VENDA
    while True:
        venda_avulsa = input("\nAnexar essa venda à um cliente? [ S / N ] ").strip().upper()
        # VALIDAÇÃO CASO A COMPRA SEJA ASSOCIADA À UM CLIENTE
        if venda_avulsa == 'S':
            while True:
                cpf_cliente = input("Digite o CPF do cliente: ")
                if not infovalida('cpf', cpf_cliente, listadeclientes):
                    print("\nERROR: Insira uma informação válida.")

                else: #CASO O CPF  EXISTA, UTILZAMOS ESSE LAÇO DE REPETIÇÃO PARA DESCOBRIR A QUEM ELE PERTENCE E ASSOCIA-LO A VÁRIAVEL VAZIA DE CLIENTE
                    for cliente in listadeclientes:
                        if cliente['cpf'] == cpf_cliente:
                            cliente_encontrado = cliente
                            break
                    break
            # VALIDAÇÃO PARA ASSOCIAR A COMBRA AO CLIENTE
            if cliente_encontrado:
                compra = { 
                    "id": produto_encontrado['id'],
                    "nome": produto_encontrado['nome'],
                    "quantidade_comprada": quantidade_venda
                    }
                cliente_encontrado['produtos'].append(compra)
                print(f"\nVenda anexada ao cliente {cliente_encontrado['nome']}")
            break


        elif venda_avulsa == 'N':
            print("\nVenda finalizada")
            break
        else:
            print("\nERROR: Insira uma informação válida.")
    # DIMINUI O ESTOQUE
    produto_encontrado['quantidade'] -= quantidade_venda
    

def listarproduto(listadeprodutos):
    print('\n############## PRODUTOS CADASTRADOS ##########\n')
    # se não listadeprodutos, se ela estiver vazia, não há produto cadastrado
    if not listadeprodutos:
        print("Nenhum produto cadastrado.")
        return

    for produto in listadeprodutos:
        mostrarproduto(produto)
    return listadeprodutos

def listarcliente(listadeclientes):
    print('\n############## CLIENTES CADASTRADOS ##########\n')
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
    print('\n############## CADASTRO DE CLIENTES ##########\n')
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
    print('\n############## PROCURAR CLIENTE ##########\n')
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