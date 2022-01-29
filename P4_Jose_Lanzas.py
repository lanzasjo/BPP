import pdb

# ACTIVIDAD 1

Lista1 = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

print(f"\n La Lista 1 es: {Lista1}\n")

#pdb.set_trace()
Max_Vector = [max(i) for i in Lista1]
print(f" El máximo de cada vector de la Lista 1 es: {Max_Vector}\n")


# ACTIVIDAD 2

Lista2 = [3, 4, 8, 5, 5, 22, 13]
print(f"\n \n La Lista 2 es: {Lista2}\n")

def es_primo(n):
    pdb.set_trace()
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

primos = list(filter(es_primo, Lista2))

print(f" Los numeros primos de la Lista 2 son: {primos}\n")