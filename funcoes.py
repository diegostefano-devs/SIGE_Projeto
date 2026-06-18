import ast # Biblioteca nativa para análise de estruturas de código

#FUNÇÃO PARA VERIFICAR SE A INFORMAÇÃO DIGITADA EXISTE NA LISTA
def validar_informacao (chave, valor_procurado, lista_de_dados): #KEY DO DICIONARIO, VALOR COLOCADO NO USUÁRIO, LISTA PARA PROCURAR
    #PERCORRE A LISTA COLOCADA 
    for item in lista_de_dados:
        #CASO EXISTA NA LISTA, RETORNA VERDADEIRO 
        if item[chave] == valor_procurado:
            return True
    return False

# FUNÇÃO PARA ADICIONAR OS CLIENTES DO DOCUMENTO À LISTA
def carregar_clientes ():
    listadeclientes = []
    # ELE VAI TENTAR ABRIR O DOCUMENTO 'clientes.txt'
    try:
        with open ('clientes.txt', 'r', encoding='utf-8') as arquivo:
            #VAI PERCORRER CADA LINHA DO DOCUMENTO
            for linha in arquivo:
                #AO RETIRAR OS ESPAÇOS E SEPARAR POR BASE DO ; VAI ANEXAR CADA DADO A UMA VARIAVEL
                nome, cpf, telefone, endereco, produto  = linha.strip().split(';')
                #VAI POR AS VARIAVEIS EM UM DICIONARIO
                clientes = {
                        "nome": nome,
                        "cpf": cpf,
                        "endereco": endereco,
                        "telefone": telefone,
                        "produtos": ast.literal_eval(produto) # Transforma o texto "[]" em uma lista real []
                    }
                # VAI ADICIONAR A LISTA
                listadeclientes.append(clientes)
    #CASO NÃO CONSIGA, VAI APENAS IGNORAR
    except FileNotFoundError:
        pass
    return listadeclientes

# FUNÇÃO PARA ADICIONAR OS PRODUTOS DO DOCUMENTO À LISTA
def carregar_produtos():
    listadeprodutos = []
    try:
        with open ('produtos.txt', 'r', encoding='utf-8') as arquivo:
            #VAI PERCORRER CADA LINHA DO DOCUMENTO
            for linha in arquivo:
                #AO RETIRAR OS ESPAÇOS E SEPARAR POR BASE DO ; VAI ANEXAR CADA DADO A UMA VARIAVEL
                id, nome, descricao, tamanho, quantidade = linha.strip().split(';')
                #VAI POR AS VARIAVEIS EM UM DICIONARIO
                produtos = {
                    'id': int(id),
                    'nome': nome,
                    'descricao': descricao,
                    'tamanho': tamanho,
                    'quantidade': int(quantidade)
                }
                # VAI ADICIONAR A LISTA
                listadeprodutos.append(produtos)
    #CASO NÃO CONSIGA, VAI APENAS IGNORAR       
    except FileNotFoundError:
        pass
    return listadeprodutos     

#FUNÇÃO PARA SALVAR OS CLIENTES NO DOCUMENTO
def salvarcliente (listadeclientes):
      #ABRE OU CRIA O DOCUMENTO 'clientes.txt" E RODA O BLOCO DE CÓDIGO
    with open('clientes.txt', 'w', encoding='utf-8') as arquivo:
        # PERCORRE OS CLIENTES NA LISTA listadeclientes E ESCREVE CADA DADO NO DOCUMENTO
        for cliente in listadeclientes:
            arquivo.write(
                f"{cliente['nome']};"
                f"{cliente['cpf']};"
                f"{cliente['telefone']};"
                f"{cliente['endereco']};"
                f"{cliente['produtos']}\n"
            )
#FUNÇÃO PARA SALVAR PRODUTOS NO DOCUMENTO
def salvarproduto(listadeprodutos):
    #ABRE OU CRIA O DOCUMENTO 'produtos.txt" E RODA O BLOCO DE CÓDIGO
    with open ('produtos.txt', 'w', encoding='utf-8') as arquivo:
        # PERCORRE OS PRODUTOS NA LISTA listadeprodutos E ESCREVE CADA DADO NO DOCUMENTO
        for produto in listadeprodutos:
            arquivo.write (
                f"{produto['id']};"
                f"{produto['nome']};"
                f"{produto['descricao']};"
                f"{produto['tamanho']};"
                f"{produto['quantidade']}\n"
            )

#FUNÇÃO PARA EXCLUIR CLIENTES 
def excluir_clientes(listadeclientes):

    cpf_local = input("Digite o CPF do cliente: ")
    # VERIFICA SE O DADO ESTÁ NA LISTA
    if not validar_informacao('cpf', cpf_local, listadeclientes):
        print("\nERROR: Cliente não encontrado.")

    #PERCORRE A LISTA, AO ENCONTRAR O CPF CORRESPONDENDTE, REMOVE O CLIENTE E PARA O LOOPING
    for cliente in listadeclientes:
        if cliente['cpf'] == cpf_local:
            listadeclientes.remove(cliente)
            print("\nCLIENTE REMOVIDO COM SUCESSO.\n")
            break
    # ATUALIZA O DOCUMENTO 'clientes.txt#
    salvarcliente(listadeclientes)

#FUNÇÃO PARA EXCLUIR PRODUTOS: 
def excluir_produto(listadeprodutos):

    id_local = int(input("Digite o ID do produto: "))
    # VERIFICA SE O DADO ESTÁ NA LISTA
    if not validar_informacao('id', id_local, listadeprodutos):
        print("ERROR: Produto não encontrado.")

 #PERCORRE A LISTA, AO ENCONTRAR O CPF CORRESPONDENDTE, REMOVE O CLIENTE E PARA O LOOPING   
    for produto in listadeprodutos:
        if produto['id'] == id_local:
            listadeprodutos.remove(produto)
            print("\nPRODUTO REMOVIDO COM SUCESSO!\n")
            break
    # ATUALIZA O DOCUMENTO 'produtos.txt#
    salvarproduto(listadeprodutos)


def cadastroproduto(listadeprodutos):
    print('\n############## CADASTRO DE PRODUTOS ##########\n')

    #Validação para garantir que o ID cadastrado seja único
    while True:
        id = int(input("Digite o id do produto: "))

        if validar_informacao('id', id, listadeprodutos):
            print("\nERROR: ID já cadastrado no sistema")
        else:
            break

    nome = input("Digite o nome do produto: ").strip().upper()
    descricao = input(("Digite uma descrição do produto: ")).strip().upper()
    tamanho = input("Digite o tamanho do produto: ")
    
    while True:
        quantidade = int(input("Digite a quantidade do produto: "))
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
            salvarproduto(listadeprodutos)
            return produto
        
    print("Produto não encontrado")
    # esse print está fora do if (funciona como um else), pq se o código não entrar dentro do if,
    # vai retornar o que está no print

def vendaproduto(listadeprodutos, listadeclientes):
    print('\n############## PONTO DE VENDA ##########\n')

    # VARIÁVEL VAZIA PARA PRODUTO
    produto_encontrado = None

    # LOOPING PARA ENCONTRAR PRODUTO
    while True:
        id_venda = int(input("Digite o id do produto para venda: "))
        if not validar_informacao('id', id_venda, listadeprodutos):
            print("\nERROR: Insira uma informação válida.")
        else:
            break
    # CASO O ID EXISTA, UTILZAMOS ESSE LAÇO DE REPETIÇÃO PARA DESCOBRIR A QUEM ELE PERTENCE E ASSOCIA-LO A VÁRIAVEL VAZIA DE PRODUTO
    for produto in listadeprodutos:
        if produto['id'] == id_venda:
            produto_encontrado = produto
            break

    mostrarproduto(produto_encontrado)

    # LOOPING PARA O USUÁRIO POR UMA INFORMAÇÃO DE ESTOQUE CORRETA
    while True:
        quantidade_venda = int(input("Digite a quantidade do produto para venda: "))
        if quantidade_venda <= 0:
            print("ERROR: Insira uma informação válida.")
        elif quantidade_venda > produto_encontrado['quantidade']:
            print("\nERROR: Estoque insuficiente")
        else:
            venda_avulsa(produto_encontrado, listadeclientes, quantidade_venda)
            break

        # DIMINUI O ESTOQUE
        produto_encontrado['quantidade'] -= quantidade_venda
        print("\nVenda finalizada com sucesso!")
        break
    
    produto_encontrado['quantidade'] -= quantidade_venda
    salvarproduto(listadeprodutos)

def venda_avulsa(produto_encontrado,listadeclientes, quantidade_venda):
    cliente_encontrado = None
    while True:
        venda_avulsa = input("\nAnexar essa venda à um cliente? [ S / N ] ").strip().upper()
        # VALIDAÇÃO CASO A COMPRA SEJA ASSOCIADA À UM CLIENTE
        if venda_avulsa == 'S':
            while True:
                cpf_cliente = input("Digite o CPF do cliente: ")
                if not validar_informacao('cpf', cpf_cliente, listadeclientes):
                    print("\nERROR: Insira uma informação válida.")

                else: #CASO O CPF  EXISTA, UTILZAMOS ESSE LAÇO DE REPETIÇÃO PARA DESCOBRIR A QUEM ELE PERTENCE E ASSOCIA-LO A VÁRIAVEL VAZIA DE CLIENTE
                    for cliente in listadeclientes:
                        if cliente['cpf'] == cpf_cliente:
                            cliente_encontrado = cliente
                            break
                    break
            # VALIDAÇÃO PARA ASSOCIAR A COMPRA AO CLIENTE
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

def listarproduto(listadeprodutos):
    print('\n############## PRODUTOS CADASTRADOS ##########\n')
    # se não listadeprodutos, se ela estiver vazia, não há produto cadastrado
    if not listadeprodutos:
        print("NENHUM PRODUTO CADASTRADO.\n")
        return

    for produto in listadeprodutos:
        mostrarproduto(produto)
    return listadeprodutos

def listarcliente(listadeclientes):
    print('\n############## CLIENTES CADASTRADOS ##########\n')
    if not listadeclientes:
        print("NENHUM CLIENTE ENCONTRADO.\n")
        return

    for cliente in listadeclientes:
        mostrarcliente(cliente)

def cadastrocliente(listadeclientes):
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
        if validar_informacao('cpf', cpf, listadeclientes):
            print("\nERROR: CPF já existe no banco de daods.")
            cpf = str(input("Digite o cpf do cliente: "))
        else:
            break

    #Validação de telefone
    # impedir telefone duplicado!
    while True:
        telefone = str(input("Digite o telefone do cliente: "))
        if len(telefone) != 11:
            print("\nERROR: Número inválido. Coloque uma informação válida.")
            continue
        if validar_informacao('telefone', telefone, listadeclientes):
                print("\nERROR: Telefone já existe no banco de daods.")
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

    listadeclientes.append(cliente)
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
def mostrarcliente(cliente):
    print(
        f"\nNome: {cliente['nome']}"
        f"\nCPF: {cliente['cpf'][:3]}-{cliente['cpf'][3:6]}-{cliente['cpf'][6:9]}.{cliente['cpf'][9:]}"
        f"\nTelefone: ({cliente['telefone'][:2]}) {cliente['telefone'][2:7]}-{cliente['telefone'][7:]}"
        f"\nEndereço: {cliente['endereco']}"
        f"\nProdutos: {cliente['produtos']}"
    )
def gerar_relatorio_cliente(listadeclientes):
    cpf = input("Digite o cpf do cliente: ")
    for cliente in listadeclientes:
        if cliente['cpf'] == cpf:
            nome_arquivo = (f"relatorio_{cpf}.txt")
            with open( nome_arquivo,'w',encoding='utf-8') as arquivo:
                arquivo.write(
                f"--------- SIGE ---------\n"
                f"RELATÓRIO DO CLIENTE"
                f"\nNOME: {cliente['nome']}\n")
                arquivo.write(
                    f"CPF: {cliente['cpf']}\n")

                arquivo.write(
                    f"Telefone: "
                    f"{cliente['telefone']}\n\n")

                arquivo.write(
                    "COMPRAS REALIZADAS:\n\n")

                if not cliente['produtos']:
                    arquivo.write(
                        "Nenhuma compra registrada no cliente\n")

                for compra in cliente['produtos']:
                    arquivo.write(
                        f"Produto: "
                        f"{compra['nome']}\n")
                    arquivo.write(
                        f"Quantidade: "
                        f"{compra['quantidade_comprada']}\n")
                    arquivo.write(
                        f'----------------------\n'
                    )

            print(f"Relatório salvado em {nome_arquivo}")
            return
    print("Cliente não encontrado")


def gerar_relatorio_venda(listadeclientes):
    with open('relatorio_geral.txt', 'w', encoding='utf-8') as arquivo:

        arquivo.write(
            'RELATORIO GERAL DE VENDAS\n'
        )

        for cliente in listadeclientes:

            arquivo.write(
                '---------- CLIENTE ---------- \n\n'
                f"Cliente: {cliente['nome']}\n"
                f"CPF: {cliente['cpf']}\n"
                f"ENDEREÇO: {cliente['endereco']}\n"
                f"TELFONE: {cliente['telefone']}\n"
            )
            arquivo.write(f'\n ---------- HISTÓRICO DE COMPRAS ----------\n\n')
            if not cliente['produtos']:
                arquivo.write(
                    'Nenhuma compra registrada\n'
                )

            for compra in cliente['produtos']:
                arquivo.write(
                    
                    f"Produto: {compra['nome']}\n"
                    f"Quantidade: {compra['quantidade_comprada']}\n"
                    )
        print('Relatorio gerado com sucesso!')
