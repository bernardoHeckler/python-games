import os

# Função para limpar a tela
def clearScreen():
    os.system("cls")

# Função para calcular o valor do golpe
def calcularValorGolpe(ataque, defesa, bonus, level):
    valorGolpe = (ataque + defesa) / 2  # Calculando o valor do ataque
    if level % 2 == 0:  # Verificando se o nível é par
        valorGolpe += bonus  # Adicionando o bônus ao valor do ataque se o nível for par
    return valorGolpe  # Retornando o valor do ataque calculado

# Função para decidir o vencedor
def decidirVencedor(bonus, player1Ataque, player1Defesa, player1Level, player2Ataque, player2Defesa, player2Level):
    # Calculando os valores de ataque para ambos os jogadores
    valorGolpePlayer1 = calcularValorGolpe(player1Ataque, player1Defesa, bonus, player1Level)
    valorGolpePlayer2 = calcularValorGolpe(player2Ataque, player2Defesa, bonus, player2Level)
    
    # Comparando os valores de ataque para determinar o vencedor
    if valorGolpePlayer1 > valorGolpePlayer2:
        return "Player 1"  # Jogador 1 vence
    elif valorGolpePlayer2 > valorGolpePlayer1:
        return "Player 2"  # Jogador 2 vence
    else:
        return "Empate"  # É um empate

# Lendo o valor do bônus inserido pelo usuário
print("Batalha de Pokemons")
bonus = int(input("Insira o Bônus: "))

clearScreen()

# Lendo os dados do Pokemons do Jogador 1
print("Batalha de Pokemons")
print("Pokemons de Player 1 ")
player1Ataque = int(input("Ataque do Pokemon = "))
player1Defesa = int(input("Defesa do Pokemon = "))
player1Level = int(input("Level do treinador = "))

clearScreen()

# Lendo os dados do Pokemons do Jogador 2
print("Batalha de Pokemons")
print("Pokemons de Player 2 ")
player2Ataque = int(input("Ataque do Pokemons = "))
player2Defesa = int(input("Defesa do Pokemons = "))
player2Level = int(input("Level do treinador = "))

clearScreen()

# Decidindo o vencedor
vencedor = decidirVencedor(bonus, player1Ataque, player1Defesa, player1Level, player2Ataque, player2Defesa, player2Level)
print("O vencedor da batalha é:", vencedor)  # Imprimindo o vencedor
