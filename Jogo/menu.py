"""
Universidade de Brasilia
Instituto de Ciencias Exatas
Departamento de Ciencia da Computacao
Algoritmos e Programação de Computadores 2/2023
Turma: Prof. Carla Castanho e Prof. Frank Ned
Aluno(a): Pedro Henrique Silva de Sousa (Monitor)
Matricula: 222001411
Projeto Final - Parte 1
Descricao: < breve descricao do programa >
"""

def joguinho():
     print('jogando')


def menu_jogo():
    
    print('1 - Jogar')
    print('2 - Configurações')
    print('3 - Ranking')
    print('4 - Instrucoes')
    print('5 - Sair')
    escolha = int(input('Digite a escolha: '))
    
    match escolha:
        case 1: joguinho()
        case 2: menu_jogo()
        case 3: menu_jogo()
        case 4: menu_jogo()
        case 5: exit()


    # if escolha == 1:
    #     joguinho()

    # elif escolha == 5:
    #     jogando = False

    # else:
    #     menu_jogo()

menu_jogo()
