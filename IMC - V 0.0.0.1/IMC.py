peso = eval(input("Informe seu peso em KG's: "))
altura = eval(input("Informe sua altura em Metros: "))
r=peso/(altura**2)
print(f"Seu IMC é: {r:.2f}")
if(r<16.9):
    r="Muito Abaixo do Peso."
elif(r<=24.9):
    r="Peso Normal"
elif(r<=29.9):
    r="Acima do Peso"
elif(r<=34.9):
    r="Obesidade Grau I"
elif(r<=40):
    r="Obesidade Grau II"
elif(r>40):
    r="Obesidade Grau III"
print(f"É Considerado como: {r}")