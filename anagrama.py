def anagrama():
    print("Te invito a probar si 2 palabras/oraciones son anagramas (usar las letras de una palabra para escribir otra).")
    anagrama1 = input("Escribe una palabra u oración: ")
    anagrama2 = input("Escribe otra palabra u oración: ")
    
    lista_anagrama1 = []
    for caracter in anagrama1:
        if caracter.isalnum():
            lista_anagrama1.append(caracter.lower())
    lista_anagrama2 = []
    for caracter in anagrama2:
        if caracter.isalnum():
            lista_anagrama2.append(caracter.lower())
    lista_anagrama1.sort()
    lista_anagrama2.sort()
    
    if lista_anagrama1 == lista_anagrama2:
        print("Es un anagrama")
    else:
        print("No es un anagrama")

anagrama()
