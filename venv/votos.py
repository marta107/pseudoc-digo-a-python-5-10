#Nombre: Acceso_voto 
#Entrada: edad 
#Salida: edad_mínima 
#edad_mínima = edad>=18 
#Devolver: edad_mínima 
def Acceso_voto(edad):
    edad_mínima = edad >= 18
    return edad_mínima
print(Acceso_voto(20))
print(Acceso_voto(15))