# Como usuario de la aplicación quiero que se clasifique cualquier número entero según 
# sea múltiplo de 3, de 5, de ambos o de ninguno para que el juego muestre 
# la respuesta correcta.
# multiplo de 3 -> fizz
# multiplo de 5 -> buzz
# multiplo de 3 y multiplo de 5 -> fizzbuzz
# ninguno -> valor del numero entero (ejemplo: 2)

def es_multiplo(num):
    if (num%3==0) and (num%5==0):
        return"fizzbuzz"
    if (num%3==0):
        return "fizz"
    if (num%5==0):
        return"buzz"

    return(num)

print(es_multiplo(15))