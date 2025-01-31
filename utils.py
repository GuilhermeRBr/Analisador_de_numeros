def leiaint(msg):
    print('-'*40)

    while True:
        try:
            n = int(input(msg))

        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um número Inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return int(n) 


def leiafloat(msg):
    print('-'*40)
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um número Real valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m ')
            return 0
        else:
            return float(n)
