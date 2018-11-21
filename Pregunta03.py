# Entrada
while True:
	o = int(input("Ingrese la orden de la matriz: "))
	if o >= 2:
		break

m = []
for i in range(o):
	a = []
	for j in range(o):
		a.append(int(input("Ingrese un num: ")))
	m.append(a)

# Proceso
d = 0
for i in range(len(m)):
	d = d + m[i][i]

# Salida
print(m)
print(d)