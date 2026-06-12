
def cadastroproduto(produto, listadeprodutos):
    # verifica se a quantiade cadastrada é menor que 0
    if produto["quantidade"] < 0:
        print("Não é possível cadastrar quantidade negativa")
        return None
    # Verifica se há algum produto com esse id cadastrado
    for itens in listadeprodutos:
        if itens["id"] == produto["id"]:
            print("ID já cadastrado.")
            return None
    if produto:
        listadeprodutos.append(produto)
        print("Produto cadastrado com sucesso")
        mostrarproduto(produto)

def consultarproduto(id,listadeprodutos ):
    # o for vai percorrer todos os id dentro da lista listadeprodutos
    for produto in listadeprodutos:
        if produto["id"] == id:
                mostrarproduto(produto)

                return
    # esse print está fora do if (funciona como um else), pq se o código não entrar dentro do if,
    # vai retornar o que está no print
    print("Produto não encontrado")

def comprarproduto(id,quantidade_compra, listadeprodutos):
    # Verifica se a quantidade de compra é menor ou igual a zero
    if quantidade_compra <= 0:
        print("Quantidade inválida.")
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
            f"\nCPF: {cliente['cpf']}"
            f"\nTelefone: {cliente['telefone']}"
            f"\nEndereço: {cliente['endereco']}"
            f"\nProdutos: {cliente['produtos']}"
        )

def cadastrocliente(nome, cpf, telefone, endereco):
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "telefone": telefone,
        "produtos": []
    }

    return cliente

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