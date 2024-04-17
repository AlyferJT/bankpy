OPTIONS_MESSAGE = '''
 ____________________
| Bem vindo ao BanPy |
|                    |
| [1] Sacar          |
| [2] Depositar      |
| [3] Extrato        |
|                    |
| [0] Fechar         |
|____________________|
'''

WITHDRAWAL_MESSAGE = '''
 _________________________________
|                                 |
| Digite o valor que deseja sacar |
|_________________________________|
'''

DEPOSIT_MESSAGE = '''
 _____________________________________
|                                     |
| Digite o valor que deseja depositar |
|_____________________________________|
'''

balance = 1200.00
available_withdrawal = 3

withdrawl_limit = 500.00
deposit_limit = 1000.00

EXTRACT = []

while True:
    print(OPTIONS_MESSAGE)
    user_select = int(input('Escolha a sua opção! -> ').strip(' '))
    
    ######### FECHAR #########
    ##########################
    if user_select == 0:
        break

    ######### SAQUE #########
    #########################
    elif user_select == 1: 
        if available_withdrawal:
            print(WITHDRAWAL_MESSAGE)
            withdrawl_value = float(input('-> '))
            print(withdrawl_value)
        
            if withdrawl_value <= withdrawl_limit:
                if withdrawl_value < balance:
                    if withdrawl_limit > 0:
                        balance -= withdrawl_value
                        available_withdrawal -= 1

                        print(f"Saque de R$ {withdrawl_value:.2f} efetuado com sucesso!")
                        print(f"O novo saldo da sua conta é R$ {balance:.2f}")

                        EXTRACT.append(f"{len(EXTRACT) + 1}. Saque de R$ {withdrawl_value:.2f} efetuado.")

                        input('\nPressione enter para continuar...')

                    else:
                        print("\nVocê selecionou um valor inválido!")
                        input('\nPressione enter para continuar...')

                else:
                    print(f"\nSaldo insuficiente... Seu saldo: R$ {balance:.2f}")
                    input('\nPressione enter para continuar...')
                    
            else:
                print(f"Sua tentativa de saque ultrapassa o limite de R$ {withdrawl_limit:.2f}")
                print(f"Tente sacar novamente com um valor menor ou igual ao limite de saque.")
                input('\nPressione enter para continuar...')
        else:
            print(f"Você está sem limite de saque, tente novamente no próximo dia...")
            input('\nPressione enter para continuar...')

    ######### DEPOSITO #########
    ############################
    elif user_select == 2: 
        print(DEPOSIT_MESSAGE)
        deposit_value = float(input('-> '))
        
        if (deposit_value > 0 and deposit_value <= deposit_limit):
            balance += deposit_value
            print(f"Depósito de R$ {deposit_value:.2f} efetuado com sucesso!")
            print(f"O novo saldo da sua conta é R$ {balance:.2f}.")

            EXTRACT.append(f"{len(EXTRACT) + 1}. Depósito de R$ {deposit_value:.2f} efetuado.")

            input('\nPressione enter para continuar...')
        else:
            if deposit_value < 0:
                print("\nVocê digitou um valor inválido")
                print("\nPor favor, digite um valor maior que 0...")
                input('\nPressione enter para continuar...')

            elif deposit_value > deposit_limit:
                print(f"\nVocê não pode depositar mais de R$ {deposit_limit:.2f}")
                print(f"Por favor, digite um valor menor que R$ {deposit_limit:.2f}")
                input('\nPressione enter para continuar...')

    ######### EXTRATO #########
    ###########################
    elif user_select == 3: 
        print('\n')
        print('\n'.join(EXTRACT))
        print(f'\nSeu saldo atual é: R$ {balance:.2f}')
        input('\nPressione enter para continuar...')
    else:
        print('\nOpa... Essa operação não existe :P')
        input('\nPressione enter para continuar...')