class Produto:
    def __init__(self, nome, preco, quantidade, tipo, fornecedor):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo
        self.fornecedores = []

    def __str__(self):
        fornecedores_str = ', '.join(
            [fornecedor.nome for fornecedor in self.fornecedores]) if self.fornecedores else "Nenhum"
        return f"{self.nome},{self.preco},{self.quantidade},{self.tipo}, Fornecedores: {fornecedores_str}"

    def from_string(data_str):
        def from_string(data_str):
            nome, preco,quantidade,tipo,fornecedores = data_str.strip().split(",")
            return Produto(nome,float(preco), quantidade, tipo,fornecedores)
#Associar Fornecedor
def associar_fornecedor(self, fornecedor):
        if fornecedor not in self.fornecedores:
            self.fornecedores.append(fornecedor)
            print(f"Fornecedor {fornecedor.nome} associado ao produto {self.nome} com sucesso!")
        else:
            print("Este fornecedor já está associado a este produto.")
#Listar fornecedores associados
    def listar_fornecedores(self):
        if not self.fornecedores:
            print("Nenhum fornecedor associado a este produto.")
        else:
            print(f"Fornecedores do produto {self.nome}:")
            for fornecedor in self.fornecedores:
                print(f"- {fornecedor.nome} ({fornecedor.telefone}, {fornecedor.email})")
