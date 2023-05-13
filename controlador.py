import random
import time


# Função para validar o cartão
def validar_cartao(cartao, senha):
    # Combinar matrícula e data do dia para validar o cartão
    matricula = cartao[:4][::-1] # Inverter os 4 primeiros dígitos da matrícula
    data = input("Digite a data de hoje (no formato dd/mm/yyyy): ")
    # validacao da senha
    validacao = matricula + data
    # Validar a senha usando a validação
    return senha == validacao

# Definir o saldo aleatório da conta do usuário
saldo = random.randint(0, 1000)

# Interação com o caixa eletrônico
print("Bem-vindo ao caixa eletrônico!")
cartao = input("Insira o seu cartão: ")
senha = input("Digite a sua senha: ")
if validar_cartao(cartao, senha):
    print("Opções disponíveis:")
    print("a. Verificação de saldo")
    print("b. Saque")
    print("c. Depósito")
    print("d. Transferência")
    opcao = input("Escolha a opção desejada: ")
    if opcao == "b": # Saque
        valor = int(input("Digite o valor a ser sacado: "))
        if valor <= saldo:
            saldo -= valor
            print("Operação concluída com sucesso.")
            print("Novo saldo:", saldo)
        else:
            print("Saldo insuficiente.")
    else:
        print("Opção não suportada.")
else:
    print("Cartão ou senha inválidos.")
