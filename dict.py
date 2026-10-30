
# ==============================================================================
# PASSO 1: O Sistema de Cadastro de Produtos
# ==============================================================================


produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}


print("--- Passo 1: Dicionário Completo do Produto ---")
print(produto)
print()


print("--- Acesso Individual às Chaves ---")
print(f"Nome do Produto: {produto['nome']}")
print(f"Preço do Produto: R$ {produto['preco']:.2f}")
print("\n" + "="*50 + "\n")


# ==============================================================================
# PASSO 2: Atualização Dinâmica de Dados
# ==============================================================================

produto["preco"] = 220.0
produto["estoque"] += 6  # Equivalente a: produto["estoque"] = produto["estoque"] + 6


produto["categoria"] = "Periféricos"


print("--- Passo 2: Dicionário de Produto Atualizado ---")
print(produto)
print("\n" + "="*50 + "\n")


# ==============================================================================
# PASSO 3: O Perfil de Usuário e Métodos de Inspeção
# ==============================================================================


usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}

print("--- Passo 3: Inspeção do Perfil de Usuário ---")

chaves_usuario = usuario.keys()
print(f"Chaves cadastradas: {chaves_usuario}")

valores_usuario = usuario.values()
print(f"Valores cadastrados: {valores_usuario}")


