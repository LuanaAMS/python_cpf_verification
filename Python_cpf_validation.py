CPF=str(input('digite o número do CPF que deseja consultar: \n'))

soma1 = 0
soma2 = 0

#Digito verificador 1
  #Faz a multiplicação e soma
for i in range (9):
  temp = int(CPF[i])*(10-i)
  soma1 = soma1+temp

  #Define o resto da função
resto1=soma1%11

  #Define o digito com base nas regras de restrição
if (resto1 == 1 or 0):
  dig1 = 0
else:
  dig1 = 11-resto1

#Digito verificador 2
  #Faz a multiplicação e soma
for i in range (10):
  temp = int(CPF[i])*(11-i)
  soma2 = soma2+temp

  #Define o resto da função
resto2 = soma2%11

  #Define o digito com base nas regras de restrição
if (resto2 == 1 or resto2 == 0):
  dig2 = 0
else:
  dig2 = 11-resto2

#Validação
if (int(CPF[9]) == dig1 and int(CPF[10]) == dig2):
  print("CPF Válido")
else:
  print("CPF inválido")
