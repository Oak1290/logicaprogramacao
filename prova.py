#1
def exercicio_1():
  print("Introduza três notas:")
  nota_1 = float(input())
  nota_2 = float(input())
  nota_3 = float(input())
  return (F"Média do aluno é {(nota_1 + nota_2 + nota_3) / 3}")
exercicio_1()

#2
def exercicio2():
  num_elementos = int(input("Insira o número de "))
  lista = []

  for num in range (num_elementos):
    lista.append(input())
  return lista

#3
def exercicio_3():
  entrada = input("Introduza 'a' para Globo, 'b' para SBT e 'z' ou 'Z' para finalizar: ")
  while entrada != 'z':    
    if entrada == 'Z':
      break
    elif entrada == 'a':
      print("Globo")
    elif entrada == 'b':
      print("SBT")
    else:
      print("Inválido")
    entrada = input()
exercicio_3()

#4
def exercicio_4():
  i = 0
  lista = input("Insira as médias dos alunos: ")
  list = lista.split()
  media_inferior = []
  while i < len(list):
    if int(list[i]) < 7:
      media_inferior.append(list[i])
    i += 1
    if len(media_inferior) < 0.25 * len(list):
      return "Professor Coxa"
    else:
     return "Professor Padrão"
exercicio_4()
