# Entrada
n = []
while len(n) < 5:
	n.append(int(input("Ingrese un num: ")))
	
# Proceso
def menor_valor(arreglo):
	menor = arreglo[0]
	
	for i in arreglo:
		if i < menor:
			menor = i
			
	return menor

menor = menor_valor(n)
	
# Salida
print(menor)