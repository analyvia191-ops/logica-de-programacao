# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Brian Samuel de Souza Dantas
# Data: 18/09/2026
# Link do Repositório: 
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Deve receber uma string.
   - Deve remover espaços extras das pontas (.strip()).
   - Deve converter o texto para letras MAIÚSCULAS (.upper()).
   - Retorna o texto devidamente formatado.
   """
   texto_limpo = texto.strip().upper()
   return texto_limpo


def extrair_codigo_ou_ddd(dado):
   """
   FUNÇÃO 2:
   - Deve receber um dado em formato de string (ex: telefone ou CPF).
   - Deve remover espaços das pontas.
   - Deve utilizar FATIAMENTO DE STRING [x:y] para extrair os 2 primeiros dígitos (ex: DDD).
   - Retorna apenas os dígitos extraídos.
   """
   dado_limpo = dado.strip()
   ddd = dado_limpo[0:2]  # Pega os caracteres do índice 0 ao 2 (não inclusivo)
   return ddd


def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Deve receber a lista de cadastros brutos como parâmetro.
   - Deve utilizar um laço FOR para percorrer cada item da lista.
   - Em cada iteração do for:
       1. Separar as partes usando .split(";")
       2. Chamar a Função 1 para formatar o Nome e o Cargo.
       3. Chamar a Função 2 para extrair o DDD/Código do telefone.
       4. Exibir o resultado final formatado na tela com f-string.
   - Retorna a quantidade total de registros processados.
   """
   contador = 0
   
   for item in lista_dados:
      # 1. Separar as partes usando .split(";")
      partes = item.split(";")
      
      nome_bruto = partes[0]
      cargo_bruto = partes[1]
      telefone_bruto = partes[2]
      
      # 2. Chamar a Função 1 para formatar o Nome e o Cargo
      nome_formatado = limpar_e_formatar_texto(nome_bruto)
      cargo_formatado = limpar_e_formatar_texto(cargo_bruto)
      
      # 3. Chamar a Função 2 para extrair o DDD do telefone
      ddd_extraido = extrair_codigo_ou_ddd(telefone_bruto)
      
      # 4. Exibir o resultado final formatado com f-string
      print(f"Nome: {nome_formatado} | Cargo: {cargo_formatado} | DDD: {ddd_extraido}")
      
      # Incrementa o total de registros processados
      contador += 1
      
   return contador


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   # Chamada da Função 3 passando a lista 'dados_brutos' e guardando o retorno
   total_processado = processar_e_exibir_cadastros(dados_brutos)
   
   # Mensagem final mostrando a quantidade total de registros processados
   print(f"\nSucesso: {total_processado} registros foram processados com êxito.")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")


# Execução do programa
if __name__ == "__main__":
   main()
