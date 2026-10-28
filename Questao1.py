
def primeira_questao():
    porta_destravada = False
    nivel_acesso = int(input('Informe seu nível de acesso: '))

    if nivel_acesso > 5:
        print('Acesso liberado.')
        porta_destravada = True
    else:
        print('Acesso negado: Permissão insuficiente.')
        porta_destravada = False

    print(f'Porta destravada: {porta_destravada}')


if __name__ == '__main__':
    primeira_questao()
