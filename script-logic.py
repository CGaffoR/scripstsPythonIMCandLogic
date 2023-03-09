# SCRIPT IN PYTHON MAIOR VALOR

n1 = int(input('Digite um numero: '));
maior = n1;
n2 = int(input('Digite um numero: '));

def maiores(n1, n2):
    return f'{n1} e {n2}, são iguais'

if(n2 > n1):
    maior = n2;
elif(n2 == n1):
    maior = maiores(n1, n2);

print(f"o maior numero eh: {maior}")