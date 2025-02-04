import re

class Fornecedor :
    def __init__(self,nome,telefone,email,tipo_de_produto,produtos):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tipo_de_produto = tipo_de_produto
        self.produtos = []

    def __str__(self):
        produtos_str = ', '.join([produto.nome for produto in self.produtos]) if self.produtos else "Nenhum"
        return f"{self.nome},{self.telefone},{self.email},{self.tipo_de_produto}, Produtos: {produtos_str}"

    def from_string(data_str):
     nome,telefone,email,tipo_de_produto,produtos= data_str.strip().split(",")
     return Fornecedor(nome,telefone,email,tipo_de_produto,produtos )
    

