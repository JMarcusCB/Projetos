from colorama import Fore, Style

# Definição de cores
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
end = Style.RESET_ALL

# Menu de opções
menu = f"""
{blue}[d]{end} Depositar
{blue}[s]{end} Sacar
{blue}[e]{end} Extrato
{blue}[q]{end} Sair

=> """

# Variáveis de conta
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    opcao = input(menu)

    # Opção: Depositar
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Ação: {green}depósito{end} | Valor {green}{valor:.2f}{end} /"
            
            print(f"O valor de {green}{valor} foi depositado{end} com sucesso! Seu saldo foi atualizado para {blue}{saldo}{end}")
            
        else:
            print(f"{red}Algo de estranho aconteceu...{end} por favor, verifique e insira um valor válido. Obrigado!")


    # Opção: Sacar
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        if valor > 0 and valor <= 500 and valor <= saldo and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            extrato += f"Ação: {yellow}saque{end} | Valor: {yellow}{valor:.2f}{end} /"
            
            print(f"O valor de {yellow}{valor} foi sacado{end} com sucesso! Seu saldo foi atualizado para {blue}{saldo}")
            print(f"Saques restantes hoje: {LIMITE_SAQUES - numero_saques}")

        elif valor > 500:
            print(f"O valor máximo de saque para sua conta é de {yellow}R$500.00{end}")

        elif valor >= saldo:
            print(f"{red}O valor pedido extrapola o saldo em conta.{end} Por favor, insira um valor válido. Obrigado!")
            print(f"Saldo: {blue}R$ {saldo:.2f}{end}")

        elif numero_saques >= LIMITE_SAQUES:
            print(f"{red}Limite de saque diário já foi atingido.{end} Atualize sua conta para Black e tenha saques ilimitados!")
        
        else:
            print(f"{red}Algo de estranho aconteceu...{end} por favor, verifique e insira um valor válido. Obrigado!")


    # Opção: Extrato
    elif opcao == "e":
        print(f"{blue}==================== EXTRATO ===================={end}")
        
        if extrato == "":
            print("Nenhuma ação foi realizada nesta conta.")
        else:
            for e in extrato.split("/"): 
                print(e.replace("/", ""))
            print(f"Saldo: {blue}R$ {saldo:.2f}{end}")

        print(f"{blue}================================================={end}")


    # Opção: Sair
    elif opcao == "q":
        break
    
    
    # Opção inválida
    else:
        print(f"{red}Opção inválida...{end} Por favor, insira sua opção desejada novamente.")
