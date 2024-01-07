def calculadora (numero_1, numero_2, operacao_mat):
  if (operacao_mat == '+'):
    return numero_1 + numero_2
  elif (operacao_mat == '-'):
    return numero_1 - numero_2
  elif (operacao_mat == '*'):
    return numero_1 * numero_2
  elif (operacao_mat == '/'):
          if numero_1 and numero_2 != 0:
            return numero_1 / numero_2
          else:
            print("Divisão por Zero!")
            return 0
  else:
    return 0

numero1 = float(input("Insira o primeiro numeral: "))
operacao_mat = input("Escolha a operação matematica(+ - * /): ")
numero2 = float(input("Insira o segundo numeral: "))

resultado = calculadora(numero1, numero2, operacao_mat)
print("Resultado:", resultado)