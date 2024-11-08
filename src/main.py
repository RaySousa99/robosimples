import os, math
from datetime import datetime

# Saudação
def saudar():
    print("Olá! Como posso ajudar você?")

# Calcular soma
def somar(a, b):
    try:
        resultado = float(a) + float(b)
        print(f"O resultado de {a} + {b} é {resultado}")
    except ValueError:
        print("Por favor, forneça números válidos para somar.")

# Calcular subtração
def subtrair(a, b):
    try:
        resultado = float(a) - float(b)
        print(f"O resultado de {a} - {b} é {resultado}")
    except ValueError:
        print("Por favor, forneça números válidos para subtrair.")

# Calcular multiplicação
def multiplicar(a, b):
    try:
        resultado = float(a) * float(b)
        print(f"O resultado de {a} x {b} é {resultado}")
    except ValueError():
        print("Por favor, forneça números válidos para multiplicar.")

# Calcular a divisão
def dividir(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            resultado = a / b
            print(f"O resultado de {a} / {b} é {resultado}")
    except ValueError:
        print("Por favor, forneça números válidos para dividir.")

# Mostra todos os comandos
def mostrar_ajuda():
    print("Comandos disponíveis:")
    print(" - 'saudar': O robô vai cumprimentar você.")
    print(" - 'somar X Y': O robô somará os números X e Y.")
    print(" - 'subtrair X Y': O robô subtrair os números X e Y.")
    print(" - 'multiplicar X Y': O robô mutiplicar os números X e Y.")
    print(" - 'dividir X Y': O robô dividir os números X e Y.")
    print(" - 'ajuda': Mostra esta mensagem de ajuda.")
    print(" - 'raiz X': O robô vai fazer a raiz quadrada do numero X.")
    print(" - 'datahora': O robô mostra as horas atuais.")
    print(" - 'sair': Encerrar o programa.")

# Calcular a raiz quadrada
def calcular_raiz(numero):
    try:
        numero = float(numero)
        if numero < 0:
            print("Não é possível calcular a raiz quadrada de {numero} negativo.")
        else:
            resultado = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é {resultado:.2f}")
    except ValueError:
        print("Por favor, forneça um numero válido.")

# Mostrar data e horas atuais
def mostrar_data_hora():
    agora = datetime.now()
    print(f"A data e hora atuais são: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# Main
def main():
    print("Olá! Eu sou seu robô de IA.")
    while True:
        comando = input("Digite um comando ou 'sair' para encerrar: ").strip().lower()
        if comando == 'sair':
            print("Encerrando... Até a próxima!")
            os.system('cls')
            break

        elif comando == 'saudar':
            saudar()

        elif comando.startswith('somar'):
            _, *numeros = comando.split()
            if len(numeros) == 2:
                somar(numeros[0], numeros[1])
            else:
                print("Use o comando 'somar' seguido de dois números, como 'somar 2 3'.")

        elif comando == 'ajuda':
            mostrar_ajuda()

        elif comando.startswith('raiz'):
            _, numero = comando.split(maxsplit=1)
            calcular_raiz(numero)

        elif comando == 'datahora':
            mostrar_data_hora()

        elif comando.startswith('subtrair'):
            _, *numeros = comando.split()
            if len(numeros) == 2:
                subtrair(numeros[0], numeros[1])
            else:
                print("Use o comando 'subtrair' seguido de dois números, como 'subtrair X Y'.")
                
        elif comando.startswith('multiplicar'):
            _, *numeros = comando.split()
            if len(numeros) == 2:
                multiplicar(numeros[0], numeros[1])
            else:
                print("Use o comando 'multiplicar' seguido de dois números, como 'multiplicar X Y'.")
        
        elif comando.startswith('dividir'):
            _, *numeros = comando.split()
            if len(numeros) == 2:
                dividir(numeros[0], numeros[1])
            else:
                print("Use o comando 'dividir' seguido de dois números, como 'dividir X Y'.")

        else:
            print(f"Você digitou: {comando}. Ainda não sei o que fazer com isso, mas estou aperndendo!")

if __name__ == "__main__":
    main()