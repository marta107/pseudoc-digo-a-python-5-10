#ALGORITMO: CLASIFICAR_IMC 

#ENTRADAS: peso, altura  

#SALIDA: categoría  

             #imc = peso / (altura ** 2)  

             #SI imc < 18.5:  

                      #categoría = "Bajo peso"  

             #SI NO:  

                       #SI imc < 25:  

                             #categoría = "Normal"  

             #SI NO:  

                             #categoría = "Sobrepeso"  

#DEVOLVER categoría 

def CLASIFICAR_IMC(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoría = "Bajo peso"
    elif imc < 25:
        categoría = "Normal"
    else:
        categoría = "Sobrepeso"
        
    return categoría

print(CLASIFICAR_IMC(70, 1.75))
print(CLASIFICAR_IMC(50, 1.75))
print(CLASIFICAR_IMC(85, 1.75))