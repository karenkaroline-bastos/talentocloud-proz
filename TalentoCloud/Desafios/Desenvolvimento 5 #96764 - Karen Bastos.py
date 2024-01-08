def calculadora (numero_1, numero_2, operacao_mat):

  print("Escolha uma opção abaixo:")

calculadora = """
[1] Soma
[2] Subtração
[3] Multiplicação
[3] Divisão
[0] Sair
=> """

if opcao == 0:
    print("Saindo da calculadora. Até logo!")
    quebrar

elif opcao == 1:
  resultado = (numero_1 + numero_2)
elif opcao == 2:
  resultado = (numero_1 - numero_2)
elif opcao == 3:
  resultado = (numero_1 * numero_2)
elif opcao == 4:
        if numero_1 and numero_2 != 0:
            resultado = numero_1 / numero_2
        else:
            print("Divisão por Zero!")
            resultado = 0
else:
  resultado = 0


numero1 = float(input("Insira o primeiro numeral: "))
operacao_mat = input("Escolha a operação matematica(+ - * /): ")
numero2 = float(input("Insira o segundo numeral: "))

resultado = calculadora(numero1, numero2, operacao_mat)
print("Resultado:", resultado)