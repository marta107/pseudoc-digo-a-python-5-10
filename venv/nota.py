#ALGORITMO CLASIFICAR_NOTA
    #ENTRADA: nota
    #SALIDA: calificacion

    #SI nota >= 9 ENTONCES
        #calificacion ← "Sobresaliente"
    #SINO SI nota >= 7 ENTONCES
        #calificacion ← "Notable"
    #SINO SI nota >= 5 ENTONCES
        #calificacion ← "Aprobado"
    #SINO
        #calificacion ← "Suspenso"
    #FIN SI

    #DEVOLVER calificacion
#FIN ALGORITMO

#IMPRIMIR CLASIFICAR_NOTA(8)   // Notable

def clasificar_nota(nota):

 if nota >= 9:
  calificacion = "Sobresaliente"
 elif nota >= 7:
  calificacion = "Notable"
 elif nota >= 5:
  calificacion = "Aprobado"
 else:
  calificacion = "Suspenso"
 return calificacion
print(clasificar_nota(8))
print(clasificar_nota(6))
print(clasificar_nota(3))