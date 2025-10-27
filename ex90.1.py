escola = { }

escola ['nome'] = str(input("Nome: "))
escola ['media'] = float(input("Media do aluno: "))

print ('-=' * 25)
print (f"- Nome do aluno é {(escola['nome'])}")
print (f"- Média é igual a {(escola['media'])}")

if (escola['media']) >= 7:
    print ("- Situação atual é Aprovado!")
else:
    print ("-Situação atual é Reprovado!")