import time, os

def clearScreen():
    os.system("cls")

def wait(tempo):
    time.sleep(tempo)

print("""

  _________ __                 __      ________                       
 /   _____//  |______ ________/  |_   /  _____/_____    _____   ____  
 \_____  \\   __\__  \\_  __ \   __\ /   \  ___\__  \  /     \_/ __ \ 
 /        \|  |  / __ \|  | \/|  |   \    \_\  \/ __ \|  Y Y  \  ___/ 
/_______  /|__| (____  /__|   |__|    \______  (____  /__|_|  /\___  >
        \/           \/                      \/     \/      \/     \/ 

""")

wait(2)

start = input("-- Começar --")
clearScreen()

print("-- DESAFIO 1: Desafio 1: O Guardião da Porta --")
wait(2)

print(''' Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar
pela porta e continuar sua jornada, você precisa responder a seguinte questão: "Quantos cocos o macaco
tem se eu pegar metade dos cocos que ele tem, mais dois cocos,
e depois subtrair três cocos?" ''')
wait(0.5)

print("(a) 5 ")
wait(0.5)
print("(b) 2 ")
wait(0.5)
print("(c) 0 ")
wait(0.5)
print("(d) 8 ")
wait(0.5)

resultado1 = ""
resultado1 = str(input("qual a alternativa correta? "))
while not resultado1: 
    resultado1 = input("Por favor, insira algo: ")
    if resultado1:
        break

if resultado1 != "c" and resultado1 != "C":
    clearScreen()

    print("Infelizmente você errou a alternativa!")
    wait(2)

    print("""

   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
                                                      

""")
    wait(2)
    quit()
else:
    clearScreen()

    print("Certa Resposta!")
    time.sleep(1)

    print("Você está indo bem, vamos para a próxima pergunta...")
    wait(2)

    clearScreen()

    print("-- DESAFIO 2: O Labirinto dos Crocodilos --")
    wait(2)

    print(''' Após passar pela porta, você entra em um labirinto infestado de
crocodilos famintos. Para escapar deles, você precisa resolver o seguinte
problema: "Se eu tenho uma corda de 12 metros e preciso atravessar um rio de 7 metros de largura,
quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com
segurança?"''')
    wait(0.5)

    print("(a) 10 ")
    wait(0.5)
    print("(b) 6 ")
    wait(0.5)
    print("(c) 0 ")
    wait(0.5)
    print("(d) 5 ")
    wait(0.5)

    resultado2 = ""
    resultado2 = str(input("qual a alternativa correta? "))
    while not resultado2: 
        resultado2 = input("Por favor, insira algo: ")
        if resultado2:
            break

    if resultado2 != "d" and resultado2 != "D":
        clearScreen()

        print("Infelizmente você errou a alternativa!")
        wait(2)

        print("""

       _____                         ____                 
      / ____|                       / __ \                
     | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
     | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
     | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
      \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                          
                                                          

        """)
        wait(2)
        quit()
    else:
        clearScreen()

        print("""Você está indo bem, vamos para a próxima pergunta...""")
        wait(2)

        clearScreen()

        print("-- DESAFIO 3: O Enigma Final --")
        wait(2)

        print(''' Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um
enigma final: "Se o número de tesouros enterrados na ilha é igual ao dobro do número de palmeiras,
e o número de palmeiras é igual a três vezes o número de periquitos na ilha, e o número
total de periquitos é 42, quantos tesouros tem na ilha?"''')
        wait(0.5)

        print("(a) 252 ")
        wait(0.5)
        print("(b) 0 ")
        wait(0.5)
        print("(c) 6 ")
        wait(0.5)
        print("(d) 78 ")
        wait(0.5)

        resultado3 = ""
        resultado3 = str(input("qual a alternativa correta? "))
        while not resultado3: 
            resultado3 = input("Por favor, insira algo: ")
            if resultado3:
                break

        if resultado3 != "a" and resultado3 != "A":
            clearScreen()

            print("Infelizmente você errou a alternativa!")
            wait(2)

            print("""

           _____                         ____                 
          / ____|                       / __ \                
         | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
         | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
         | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
          \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                              
                                                              

            """)
            wait(2)
            quit()
        else:
            clearScreen()
            print("Parabéns! Você venceu!")
            print("""
               _                       
              (_)                      
     __      ___ _ __  _ __   ___ _ __ 
     \ \ /\ / / | '_ \| '_ \ / _ \ '__|
      \ V  V /| | | | | | | |  __/ |   
       \_/\_/ |_|_| |_|_| |_|\___|_|   
                                       
            """)
time.sleep(5)
clearScreen()
