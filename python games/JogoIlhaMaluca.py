import os,time

def clearScreen():
    os.system("cls")

def wait(tempo):
    time.sleep(tempo)

print('Bem-Vindo a Ilha MIsteriosa...')
wait(3)
clearScreen()
print('''"Para desbloquear o tesouro escondido, você deve provar sua destreza. Resolva os
desafios a seguir e siga as instruções para encontrar o caminho certo"''')
wait(10)
clearScreen()
print('Desafio 1')
print('Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar pela porta e continuar sua jornada, você precisa responder a seguinte questão: \n \n')
print('''"Quantos cocos o macaco tem se eu pegar metade dos cocos que ele tem, mais dois cocos,
e depois subtrair três cocos?"''')
cocoMacaco = int(input("Quantos cocos o macaco tinha: "))
cocoResultados = cocoMacaco /2 + 2 -3
cocosJogador = float(input("Com quantos cocos o macaco ficou? "))

if cocosJogador == cocoResultados:
    print("Ótimo! Pode prosseguir...")
else:
    print("Resposta errada! Vc se ferrou...")
    quit()

# RESPOSTA DESAFIO 1: macaco tinha 4, ficou com 0!

################################

wait(5)
clearScreen()

print('Desafio 2')
print('Após passar pela porta, você entra em um labirinto infestado de crocodilos famintos. Para escapar deles, você precisa resolver o seguinte problema: \n \n')
print('''"Se eu tenho uma corda de 12 metros e preciso atravessar um rio de 7 metros de largura,
quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com
segurança?"''')
cordaSobra = 12-7
cordaJogador = int(input("Quantos metros sobra de corda: "))

if cordaJogador == cordaSobra:
    print("Ótimo! Pode prosseguir...")
else:
    print("Resposta errada! Vc se ferrou...")
    quit()

# RESPOSTA DESAFIO 2: sobram 5 metros!

################################

wait(5)
clearScreen()

print('Desafio 3')
print('Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um enigma final: \n \n')
print('''"Se o número de tesouros enterrados na ilha é igual ao dobro do número de palmeiras,
e o número de palmeiras é igual a três vezes o número de periquitos na ilha, e o número
total de periquitos é 42, quantos tesouros tem na ilha?"''')
palmeiras = 42 * 3
tesouros = palmeiras * 2
tesourosJogador = int(input("Quantos tesouros tem a ilha: "))


if tesourosJogador == tesouros:
    print("Ótimo! Pode prosseguir...")
else:
    print("Resposta errada! Vc se ferrou...")
    quit()

# RESPOSTA DESAFIO 3: tem 252 tesouros na ilha!