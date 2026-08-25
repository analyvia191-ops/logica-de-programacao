def formatar_citacao(nome_completo):
  partes = nome_completo.strip().split()

  sobrenome = partes[-1].upper()
  primeiro_nome = " ".join(partes[:1])
  return sobrenome +", "+primeiro_nome

def gerar_codigo(ano,cpf):

  cpf_limpo = cpf.strip()

  tres_digitos = cpf_limpo[0:3]
  return "ALU-" + str(ano) + "-" + tres_digitos
autor = "carlos eduardo Andrade" 
citacao_formatada = formatar_citacao(autor)
print("citacao bibliografica:",citacao_formatada)


