#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

# while validacio
vocal = input("Ingrese vocal:")
while vocal not in('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("Vocal:")
print('Su vocal o punto   es:{}'.format(vocal))
