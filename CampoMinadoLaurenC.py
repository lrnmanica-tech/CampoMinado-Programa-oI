import random
import string
import os


def PosiçãoDeBombas1():
    Posições=[]
    while len(Posições)<10:
        NúmerosPosição=random.randint(1, 7)
        LetraPosição=random.randint(0, 6)
        Letra=string.ascii_uppercase[LetraPosição]
        Final=str(NúmerosPosição)+Letra
        if Final not in Posições:
            Posições.append(Final)
    return Posições


def PosiçãoDeBombas2():
    Posições=[]
    while len(Posições)<20:
        NúmerosPosição=random.randint(1, 7)
        LetraPosição=random.randint(0, 6)
        Letra=string.ascii_uppercase[LetraPosição]
        Final=str(NúmerosPosição)+Letra
        if Final not in Posições:
            Posições.append(Final)
    return Posições


def BombasMultiplayer2():
    ListaMultiplayer=[]
    ContadorMultiplayer=0
    while ContadorMultiplayer<15:
        print(f"Palpites restantes: {15-ContadorMultiplayer}")
        PalpitesMultiplayerINT=input("Insira a coluna (entre 1 e 7): ")
        PalpitesMultiplayerSTR=input("Insira a fileira (entre A a G): ").upper()
        PalpitesMultiplayer=str(PalpitesMultiplayerINT)+PalpitesMultiplayerSTR
        if len(PalpitesMultiplayer)!=2:
            print("\n \nInsira conforme o modelo 5C.\n ")
            continue
        if not PalpitesMultiplayer[0].isdigit():
            print("\n \nA coluna deve ser um número.\n ")
            continue
        if int(PalpitesMultiplayer[0]) not in range(1, 8):
            print("\n \nNúmero inválido.\n ")
            continue
        if PalpitesMultiplayer[1] not in "ABCDEFG":
            print("\n \nLetra inválida.\n ")
            continue
        if PalpitesMultiplayer in ListaMultiplayer:
            print("\n \nCoordenada já cadastrada!\n ")
            continue
        ListaMultiplayer.append(PalpitesMultiplayer)
        ContadorMultiplayer=ContadorMultiplayer+1
        print()
        print(ListaMultiplayer)
        os.system("clear")
    return ListaMultiplayer


def BombasMultiplayer1():
    ListaMultiplayer=[]
    ContadorMultiplayer=0
    while ContadorMultiplayer<10:
        print(f"Palpites restantes: {10-ContadorMultiplayer}")
        PalpitesMultiplayerINT=input("Insira a coluna (entre 1 e 7): ")
        PalpitesMultiplayerSTR=input("Insira a fileira (entre A a G): ").upper()
        PalpitesMultiplayer=str(PalpitesMultiplayerINT)+PalpitesMultiplayerSTR
        if len(PalpitesMultiplayer) != 2:
            print("\n \nInsira conforme o modelo 5C.\n ")
            continue
        if not PalpitesMultiplayer[0].isdigit():
            print("\n \nA coluna deve ser um número.\n ")
            continue
        if int(PalpitesMultiplayer[0]) not in range(1, 8):
            print("\n \nNúmero inválido.\n ")
            continue
        if PalpitesMultiplayer[1] not in "ABCDEFG":
            print("\n \nLetra inválida.\n ")
            continue
        if PalpitesMultiplayer in ListaMultiplayer:
            print("\n \nCoordenada já cadastrada!\n ")
            continue
        ListaMultiplayer.append(PalpitesMultiplayer)
        ContadorMultiplayer=ContadorMultiplayer+1
        print()
        print(ListaMultiplayer)
        os.system("clear")
    return ListaMultiplayer


def PosiçãoDoJogador(Questão1, Questão2, Fileiras, Bombas):
    Posição_do_Jogador=str(Questão1)+Questão2
    if Posição_do_Jogador in Bombas:
        print()
        Linha=ord(Questão2)-ord("A")
        Coluna=Questão1-1
        Fileiras[Linha][Coluna]="✸"
        for Número in range(7):
            print(string.ascii_uppercase[Número], Fileiras[Número])
        print()
        print("=================== Casa com bomba. Você perdeu! ===================")
        print()
        return True
    elif Posição_do_Jogador not in Bombas:
        print()
        print("Casa sem bomba. Continue!")
        print()
        return False


def Marcação(Questão1, Questão2, Fileiras, Bombas):
    Posição_do_Jogador=str(Questão1)+Questão2
    if Posição_do_Jogador not in Bombas:
        Linha = ord(Questão2)-ord("A")
        Coluna=Questão1
        Contador=0
        NúmerosBombas=0
        if Coluna<6:
            ProximidadeDireita=str((Coluna)+1)+string.ascii_uppercase[Linha]
            if ProximidadeDireita in Bombas:
                Contador=Contador+1
        if Coluna!=0:
            ProximidadeEsquerda=str((Coluna)-1)+string.ascii_uppercase[Linha]
            if ProximidadeEsquerda in Bombas:
                Contador=Contador+1
        if Linha>0:
            ProximidadeAcima=str(Coluna)+(string.ascii_uppercase[Linha - 1])
            if ProximidadeAcima in Bombas:
                Contador=Contador+1
        if Linha<6:
            ProximidadeAbaixo=str(Coluna)+(string.ascii_uppercase[Linha + 1])
            if ProximidadeAbaixo in Bombas:
                Contador=Contador+1
        if Coluna<6 and Linha<6:
            ProximidadeDiagonalDAb=str((Coluna)+1)+(string.ascii_uppercase[Linha + 1])
            if ProximidadeDiagonalDAb in Bombas:
                Contador=Contador+1
        if Coluna<6 and Linha>0:
            ProximidadeDiagonalDAc=str((Coluna)-1)+(string.ascii_uppercase[Linha-1])
            if ProximidadeDiagonalDAc in Bombas:
                Contador=Contador+1
        if Coluna!=0 and Linha<6:
            ProximidadeDiagonalEAb=str(Coluna-1)+string.ascii_uppercase[Linha+1]
            if ProximidadeDiagonalEAb in Bombas:
                Contador=Contador+1
        if Coluna!=0 and Linha>0:
            ProximidadeDiagonalEAc=str((Coluna)-1)+(string.ascii_uppercase[Linha-1])
            if ProximidadeDiagonalEAc in Bombas:
                Contador=Contador+1
        Fileiras[Linha][Coluna-1]=f"{Contador}"
    return Fileiras


def Jogar(PosiçãoDeBombas):
    PalpitesRealizados=[]
    Contador=0
    Bombas=PosiçãoDeBombas()
    Fileiras=[
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•"],
    ]
    while Contador < 44:
        print(f"Jogadas restantes: {44-Contador}")
        print()
        print("    1    2    3    4    5    6    7")
        for Números in range(7):
            print(string.ascii_uppercase[Números], Fileiras[Números])
        Questão1=int(input("Insira a coluna: "))
        Questão2=str(input("Insira a fileira: ")).upper()
        if Questão1 not in range(1, 8):
            print("\n--------------Coluna inválida! Repita o palpite.---------------\n")
            continue
        if Questão2 not in "ABCDEFG":
            print("\n--------------Linha inválida! Repita o palpite.--------------\n")
            continue
        if len(str(Questão1))!=1:
            print("--------------A fileira deve ter um único valor em string!--------------")
            print()
            continue
        if PosiçãoDoJogador(Questão1, Questão2, Fileiras, Bombas):
            break
        Palpite=str(Questão1)+Questão2
        if Palpite in PalpitesRealizados:
            print("--------------Palpite já realizado. Por favor, dê uma nova coordenada.--------------\n")
            continue
        if Palpite not in PalpitesRealizados:
            PalpitesRealizados.append(Palpite)
            Fileiras=Marcação(Questão1, Questão2, Fileiras, Bombas)
            Contador=Contador + 1
        if Contador==44:
            print()
            print("=================== Parabéns! Você venceu!===================")
            print()


def Tabuleiro(Resposta):
    print()
    Contador = 0
    if Resposta=="EXIT":
        print("Saindo...")
    elif Resposta=="1":
        print("- Escolha o modo no qual deseja jogar:\n1) Fácil\n2) Difícil")
        print()
        Modo=int(input("Escolha uma opção (números): "))
        if Modo==1:
            os.system("clear")
            Jogar(PosiçãoDeBombas1)
        elif Modo==2:
            os.system("clear")
            Jogar(PosiçãoDeBombas2)
    elif Resposta=="2":
        print("- Escolha o modo no qual deseja jogar:\n1) Fácil\n2) Difícil")
        print()
        Modo=int(input("Escolha uma opção (números): "))
        if Modo==1:
            os.system("clear")
            Jogar(BombasMultiplayer1)
        elif Modo==2:
            os.system("clear")
            Jogar(BombasMultiplayer2)


print("2º Trimestre - Campo Minado   Docente: Alisson Zanetti - Programação I   Discente: Lauren Manica Conceição   Turma: 1F")
print()
print("Bem-vindo(a) ao Campo Minado!")
print('Para sair do jogo (parar o programa), escreva: "EXIT"!')
print()
print("Modos de jogo:\n 1)Individual\n 2)Multiplayer")
print()
Resposta=input(f"Selecione uma opção: ")
os.system("clear")
Tabuleiro(Resposta)
