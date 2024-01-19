#Sistema Bancário
# 3 funções básicas: Saque, Depósito e Extrato

# Apenas valores positivos para depósito
# 3 saques diários / R$500,00 por saque
# Caso não haja saldo deve emitir uma mesg para informar
# Extrato deve listar todas operações e valores e no final o saldo no formato R$

menu = """
*********** menu **********

  [1] Depósito
  [2] Saque
  [3] Extrato
  [4] Sair

  Por favor digite sua opção

****************************
"""

saldo = 0
saque_diario = 0
extrato = ""
LIMITE_SAQUE_DIARIO = 3
LIMITE_SAQUE = 500

while True:

  opcao = input(menu)

  if opcao == "1":
    deposito = int(input("Digite o valor desejado"))

    if deposito < 0:
      print("Valor inválido")

    else:
      saldo += deposito
      extrato += f"Depósito: R$ {deposito:.2f}\n"
      print("Depósito realizado")

  elif opcao == "2":
    if saque_diario >= LIMITE_SAQUE_DIARIO:
      print("Limite diário excedido.")
      continue

    saque = int(input("Digite o valor desejado"))

    if saque > LIMITE_SAQUE:
        print(f"Limite máximo permitido por saque é de {LIMITE_SAQUE}.")
        
    elif saque > saldo:
        print("Desculpe, saldo insuficiente para o valor desejado")

    else:
        saldo -= saque
        saque_diario += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print("Saque realizado")
    
  elif opcao == "3":
    print("\n******** EXTRATO ********")
    print("Não existem movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n*************************")

  elif opcao == "4":
    break
  else:
    print("Opção inválida. Por favor selecione novamente a opção desejada.")