def get_dia(dia):
    dias = {
        (1, 7): 'fim de semana',
        tuple(range(2, 7)): 'dia da semana',
    }
    escolhido = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(escolhido, '** dia invalido**')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia(dia)}')
