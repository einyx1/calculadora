import webbrowser

VIDEO = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"

print("=== Calculadora ===")
print("Exemplo: 10 + 5")
print("Operações: +  -  *  /")
print("Digite 'sair' para fechar.\n")

while True:
    conta = input(">>> ").strip()

    if conta.lower() == "sair":
        break

    try:
        partes = conta.split()

        if len(partes) != 3:
            print("Use o formato: número operador número")
            continue

        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("Não dá pra dividir por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Operador inválido.")
            continue

        print("Resultado:", resultado)

        # Se a pessoa digitou 67 ou o resultado for 67
        if num1 == 67 or num2 == 67 or resultado == 67:
            print("67?! 💀")
            webbrowser.open(VIDEO)

    except ValueError:
        print("Digite números válidos.")
