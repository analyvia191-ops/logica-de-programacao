
nome_bruto = "  joão pedro da silva  "
email_bruto = " JOAO.SILVA@Escola.COM "
nome_higienizado = nome_bruto.strip().upper()
email_higienizado = email_bruto.strip().lower()
print(f"Nome higienizado: {nome_higienizado}")
print(f"E-mail higienizado: {email_higienizado}")


cpf_bruto = " 123.456.789-00 "
telefone_bruto = "(11) 99999-8888"
cpf_limpo = cpf_bruto.strip().replace(".", "").replace("-", "")


telefone_limpo = (
    telefone_bruto.strip()
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
    .replace(" ", "")
)
print(f"CPF limpo: {cpf_limpo}")
print(f"Telefone limpo: {telefone_limpo}")


codigo_bruto = "  prod-1024-br-sp  "
codigo_formatado = codigo_bruto.strip().upper().replace("-", "_")
print(f"Código formatado: {codigo_formatado}")
