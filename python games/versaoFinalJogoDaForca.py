import os, time

def clearScreen():
    os.system("cls")

def aparecer(tempo):
    time.sleep(tempo)

def bonecoNaForca(erros):
    if erros == 0:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    
|    
|   
|   
|
========""")
    elif erros == 1:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    |
|    O
|   
|   
|
========""")
    elif erros == 2:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    |
|    O
|    |
|   
|
========""")
    elif erros == 3:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    |
|    O
|   /|
|   
|
========""")
    elif erros == 4:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    |
|    O
|   /|\\
|   
|
========""")
    elif erros == 5:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    |
|    O
|   /|\\
|   /
|
========""")
    elif erros == 6:
        clearScreen()
        print(f"""+----+ Erros {erros}/6
|    |
|    O
|   /|\\
|   / \\
|
========""")


titulo = "JOGO DA FORCA"


def inicioJogo():
    clearScreen()

    print("SEJA BEM-VINDO!!")
    print("Por favor, preencha as informações abaixo!!!")
    aparecer(1)
    
    while True:
        nomeDoDesafiante = str(input("Nome do Desafiante: "))
        if nomeDoDesafiante.strip() == "" or not nomeDoDesafiante.isalpha():
            print("Por favor, preencha o campo corretamente.")
        else:
            break

    while True:
        nomeDoCompetidor = str(input("Nome do Competidor: "))
        if nomeDoCompetidor.strip() == "" or not nomeDoCompetidor.isalpha():
            print("Por favor, preencha o campo corretamente.")
        else:
            break

    clearScreen()
    print("REDIRECIONANDO PARA O JOGO...")
    aparecer(2)

    clearScreen()
    print(titulo)
    print("CARREGANDO...")
    aparecer(1.5)
    clearScreen()

    print(titulo)
    print(f"O(a) DESAFIANTE {nomeDoDesafiante}, deve colocar a Palavra-Chave e até 3 dicas obrigatórias para iniciar o jogo!")
    while True:
        palavraChave = str(input("Por favor, insira a Palavra-Chave: "))
        if palavraChave.strip() == "" or not palavraChave.isalpha():
            print("Por favor, preencha o campo corretamente.")
        else:
            break

    while True:
        dica1 = str(input("Dica 1: "))
        if dica1.strip() == "":
            print("Por favor, preencha o campo corretamente.")
        else:
            break

    while True:
        dica2 = str(input("Dica 2: "))
        if dica2.strip() == "":
            print("Por favor, preencha o campo corretamente.")
        else:
            break

    while True:
        dica3 = str(input("Dica 3: "))
        if dica3.strip() == "":
            print("Por favor, preencha o campo corretamente.")
        else:
            break
        
    comprimento = len(palavraChave)
    comprimentoAsteriscosLetras = '*' * comprimento
    executarDica1 = True
    executarDica2 = True
    executarDica3 = True
    erros = 0
    letrasTentadas = set()

    perdeuJogo = False
    ganhouJogo = False

    while erros < 6:
        dicas = [dica1, dica2, dica3]

        while True:
            clearScreen()
            bonecoNaForca(erros)
            print(comprimentoAsteriscosLetras)
            print(f"A Palavra-Chave contém {comprimento} letras!")
            print("Letras que já foram: ", ' '.join(sorted(list(letrasTentadas - set(palavraChave)))))
            print("(0) Solicitar dica")
            print("(1) Adivinhar uma letra")
            vez = input("Escolha uma opção: ")

            if vez == "0":
                if executarDica1:
                    clearScreen()
                    bonecoNaForca(erros)
                    print(comprimentoAsteriscosLetras)
                    print(f"A Palavra-Chave contém {comprimento} letras!")
                    print("Letras erradas: ", ' '.join(sorted(list(letrasTentadas - set(palavraChave)))))
                    print("VOCÊ ESCOLHEU UMA DICA")
                    print(f"DICA 1: {dicas[0]}")
                    letra = input("Insira uma letra para arriscar: ")
                    if letra.isalpha() and len(letra) == 1:
                        letrasTentadas.add(letra)
                        if letra in palavraChave:
                            for i in range(len(palavraChave)):
                                if palavraChave[i] == letra:
                                    comprimentoAsteriscosLetras = comprimentoAsteriscosLetras[:i] + letra + comprimentoAsteriscosLetras[i+1:]
                                if '*' not in comprimentoAsteriscosLetras:
                                    print("Você acertou a palavra-chave!")
                                    ganhouJogo = True
                                    if ganhouJogo:
                                        while True:
                                            opcao = input("Deseja jogar novamente? (S/N): ").upper()
                                            if opcao == "S":
                                                inicioJogo()
                                                break
                                            elif opcao == "N":
                                                print("Obrigado por jogar!")
                                                quit()
                                            else:
                                                print("Opção inválida. Por favor, escolha S para jogar novamente ou N para sair.")

                        else:
                            erros += 1
                            if erros >= 6:
                                perdeuJogo = True
                                return
                        aparecer(1)
                        executarDica1 = False
                elif executarDica2:
                    clearScreen()
                    bonecoNaForca(erros)
                    print(comprimentoAsteriscosLetras)
                    print("Letras erradas: ", ' '.join(sorted(list(letrasTentadas - set(palavraChave)))))
                    print("VOCÊ ESCOLHEU MAIS UMA DICA")
                    print(f"DICA 2: {dicas[1]}")
                    letra = input("Insira uma letra para arriscar: ")
                    if letra.isalpha() and len(letra) == 1:
                        letrasTentadas.add(letra)
                        if letra in palavraChave:
                            for i in range(len(palavraChave)):
                                if palavraChave[i] == letra:
                                    comprimentoAsteriscosLetras = comprimentoAsteriscosLetras[:i] + letra + comprimentoAsteriscosLetras[i+1:]
                                if '*' not in comprimentoAsteriscosLetras:
                                    print("Você acertou a palavra-chave!")
                                    ganhouJogo = True
                                    if ganhouJogo:
                                        while True:
                                            opcao = input("Deseja jogar novamente? (S/N): ").upper()
                                            if opcao == "S":
                                                inicioJogo()
                                                break
                                            elif opcao == "N":
                                                print("Obrigado por jogar!")
                                                quit()
                                            else:
                                                print("Opção inválida. Por favor, escolha S para jogar novamente ou N para sair.")
                        else:
                            erros += 1
                            if erros >= 6:
                                perdeuJogo = True
                                return
                            print("Erros:", erros)
                        aparecer(1)
                    executarDica2 = False
                elif executarDica3:
                    clearScreen()
                    bonecoNaForca(erros)
                    print(comprimentoAsteriscosLetras)
                    print("Letras erradas: ", ' '.join(sorted(list(letrasTentadas - set(palavraChave)))))
                    print("ATENÇÃO ESTA É A SUA ÚLTIMA DICA!")
                    print(f"DICA 3: {dicas[2]}")
                    letra = input("Insira uma letra para arriscar: ")
                    if letra.isalpha() and len(letra) == 1:
                        letrasTentadas.add(letra)
                        if letra in palavraChave:
                            for i in range(len(palavraChave)):
                                if palavraChave[i] == letra:
                                    comprimentoAsteriscosLetras = comprimentoAsteriscosLetras[:i] + letra + comprimentoAsteriscosLetras[i+1:]
                            if '*' not in comprimentoAsteriscosLetras:
                                print("Você acertou a palavra-chave!")
                                ganhouJogo = True
                                if ganhouJogo:
                                        while True:
                                            opcao = input("Deseja jogar novamente? (S/N): ").upper()
                                            if opcao == "S":
                                                inicioJogo()
                                                break
                                            elif opcao == "N":
                                                print("Obrigado por jogar!")
                                                quit()
                                            else:
                                                print("Opção inválida. Por favor, escolha S para jogar novamente ou N para sair.")
                        else:
                            erros += 1
                            if erros >= 6:
                                perdeuJogo = True
                                return
                            print("Erros:", erros)
                        aparecer(1)
                    executarDica3 = False
                else:
                    clearScreen()
                    print(f"DICA 1: {dicas[0]}")
                    print(f"DICA 2: {dicas[1]}")
                    print(f"DICA 3: {dicas[2]}")
                    print("Você já usou todas as dicas.")
                    aparecer(10)
                    print("REDIRECIONANDO...")
                    aparecer(3)
                    break
            elif vez == "1":
                clearScreen()
                bonecoNaForca(erros)
                print(comprimentoAsteriscosLetras)
                print(f"A Palavra-Chave contém {comprimento} letras!")
                print("Letras erradas: ", ' '.join(sorted(list(letrasTentadas - set(palavraChave)))))
                letra = input("Insira uma letra para arriscar: ")
                if letra.isalpha() and len(letra) == 1:
                    letrasTentadas.add(letra)
                    if letra in palavraChave:
                        for i in range(len(palavraChave)):
                            if palavraChave[i] == letra:
                                comprimentoAsteriscosLetras = comprimentoAsteriscosLetras[:i] + letra + comprimentoAsteriscosLetras[i+1:]
                        if '*' not in comprimentoAsteriscosLetras:
                            clearScreen()
                            print(f"Parabéns {nomeDoCompetidor}!! Você ganhou do {nomeDoDesafiante} e acertou a palavra-chave que era: {palavraChave}")
                            ganhouJogo = True
                            if ganhouJogo:
                                while True:
                                    opcao = input("Deseja jogar novamente? (S/N): ").upper()
                                    if opcao == "S":
                                        inicioJogo()
                                        break
                                    elif opcao == "N":
                                        clearScreen()
                                        print(f"Aos amigos {nomeDoCompetidor} e {nomeDoDesafiante}, Ótimo Jogo!")
                                        print("A todos que jogaram! Seu apoio foi incrível e espero que tenha se divertido tanto quanto nós ao criar o jogo.")
                                        print("Obrigado a todos por jogarem! Vocês são incríveis!")
                                        aparecer(15)
                                        clearScreen()
                                        print("FIM")
                                        aparecer(3)
                                        quit()
                                    else:
                                        print("Opção inválida. Por favor, escolha S para jogar novamente ou N para sair.")
                                        
                            
                    else:
                        erros += 1
                        if erros >= 6:
                            clearScreen()
                            print(f"{nomeDoCompetidor} perdeu o jogo para {nomeDoDesafiante}!")
                            print(f"A Palavra-Chave era: {palavraChave}")
                            perdeuJogo = True
                            if perdeuJogo:
                                while True:
                                    opcao = input("Deseja jogar novamente? (S/N): ").upper()
                                    if opcao == "S":
                                        inicioJogo()
                                        break
                                    elif opcao == "N":
                                        clearScreen()
                                        print(f"Aos amigos {nomeDoCompetidor} e {nomeDoDesafiante}, Ótimo Jogo!")
                                        print("A todos que jogaram! Seu apoio foi incrível e espero que tenha se divertido tanto quanto nós ao criar o jogo.")
                                        print("Obrigado a todos por jogarem! Vocês são incríveis!")
                                        aparecer(10)
                                        clearScreen()
                                        print("FIM")
                                        aparecer(3)
                                        quit()
                                    else:
                                        print("Opção inválida. Por favor, escolha S para jogar novamente ou N para sair.")
                            
                        print("Erros:", erros)
                    aparecer(1)
                else:
                    print("Por favor, insira uma única letra.")


    

    

inicioJogo()
