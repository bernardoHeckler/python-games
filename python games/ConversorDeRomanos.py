def romanoParaInt(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0 
    ultimoValor = 0
    for numeral in reversed(romano):
        valor = valores[numeral]
        if valor < ultimoValor:
            total -= valor
        else:
            total += valor
        ultimoValor = valor
    return total
print("----------------------------------CONVERSOR DE NÚMEROS ROMANOS----------------------------------")
numeroRomano = input("Digite algum número romano para Converter: ")
numeroInteiro = romanoParaInt(numeroRomano.upper())
print(f"O número romano {numeroRomano} corresponde ao número inteiro {numeroInteiro}.")


#TESTE...
#CM = 900
#CD = 400
#XVII = 17
#CMCDXVII = 1316


