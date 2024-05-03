def capitalizar_palabra(palabra):
    # Se valida que el parámetro ingresado sea una cadena de texto
    if not isinstance(palabra, str):
        return 'El parametro ingresado debe de ser un string'
    
    # Usa la función .capitalize() para convertir la primera letra en mayúscula y las demás en minúsculas
    resultado = palabra.capitalize()

    return resultado


print(capitalizar_palabra('python'))