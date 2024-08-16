nome = "Danrlei"
menu = " Menu ".center(40,"=")
fim = "".center(41,"=")


mensagem = f'''Olá meu nome é {nome}, 
estou aprendendo Python
    Essa mensagem tem diferentes recuos.'''

print(mensagem)

print(
    f'''
    {menu}

    1- Depositar
    2 - Sacar
    0 - Sair

    {fim}
    '''
)