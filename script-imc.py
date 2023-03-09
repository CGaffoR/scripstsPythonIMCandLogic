# SCRIPT PARA O CALCULA DO IMC
nome = input('Qual o seu nome: ');
altura = float(input('Qual a sua altura: '));
peso = float(input('Qual o seu peso: '));

imc = peso / (altura * altura);

if(imc < 18.5):
    print(f'{nome}!, Você está com baixo peso...');
elif(imc > 18.5 and imc < 24.9):
    print(f'{nome}!!!, você eh eutrofico(peso adequado)...');
elif(imc > 24.9 and imc < 30.0):
    print(f'{nome}!!, você está sobreopreso...');
elif(imc > 30.0 and imc < 34.9):
    print(f'{nome}!!!, você está com obesidade grau1...');
elif(imc > 34.9 and imc < 39.9):
    print(f"{nome}!!!!, você está com obesidade grau 2...");
else:
    print(f'{nome}!!!!!!!, Está com obesidade extrema... ')



