def cabecalho():
    print(10 * '-' + 'PROGRAMA EM PYTHON' + 10 * '-')


def validaCPF(cpf):
    cabecalho()
    if len(cpf) == 11:
        print('cpf válido')
    else:
        print('cpf invalido')

cp = str(input('Digite seu CPF: '))

validaCPF(cp)