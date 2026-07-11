import random
from random import sample
import string

#Números
def Números ():
    #Colunas
    Colunas=[]
    while len(Colunas)!=5:
        Resultado=random.randint(1,7)
        if Resultado not in Colunas:
            Colunas.append(Resultado)
    #Fileiras
    Fileiras=[]
    Contador=0
    while len(Fileiras)!=5:
        Resultado=random.randrange(1,7)
        Alfabeto=str(string.ascii_uppercase[Resultado])
        Contador=Contador+1
        if Resultado not in Fileiras:
            Fileiras.append(Resultado)
    #Agrupamento
    Posições=[]
    for I in range(5):
        Letra=string.ascii_uppercase[Fileiras[I]]
        Posições.append(str(Colunas[I])+Letra)

    return Posições

#Bombas
Bombas=Números()
print(Bombas)

#Posição de jogadores:
def PosiçãoDoJogador (Questão1,Questão2):
      Posição_do_Jogador=str(Questão1+Questão2)
      if Posição_do_Jogador in Bombas:
            print()
            print('Casa com bomba. Você perdeu!')
            print()
            return True
      else:
            print()
            print('Casa sem bomba. Continue!')
            print()
            return False

#Organização de tabuleiros:
def Tabuleiro (Resposta):
      print()
      if Resposta==1:
            Contador=0
            while Contador<44:
                  print ('     1  2  3  4  5  6  7')
                  Fileiras=f' A   |  |  |  |  |  |  | \n B   |  |  |  |  |  |  | \n C   |  |  |  |  |  |  | \n D   |  |  |  |  |  |  | \n E   |  |  |  |  |  |  | \n F   |  |  |  |  |  |  | \n G   |  |  |  |  |  |  | '
                  print(Fileiras)
                  Questão1=input('Insira a coluna: ')
                  Questão2=input('Insira a fileira: ')
                  if PosiçãoDoJogador(Questão1, Questão2):
                        break
            Contador=Contador+1


#Título e apresentação:
print('2º Trimestre - Campo Minado\
      Docente: Alisson Zanetti - Programação I\
      Discente: Lauren Manica Conceição\
      Turma: 1F')
#Criação da tabela (construção com base de sintaxes):
print()
print('Bem vindo ao Campo Minado!\nPara sair do jogo (parar o programa), escreva: "EXIT"!')
print("Modos de jogo:\n 1) Fácil (Individual)\n 2) Médio (Individual)\n 3) Fácil (Multiplayer)\n 4) Médio (Multplayer)")
print()
Resposta=int(input(f'Selecione uma opção (em números): '))
Tabuleiro(Resposta)
print()