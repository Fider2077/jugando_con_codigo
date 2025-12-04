#Declaración de variables
Mensaje = None
rotor1 = ("q","ñ","x","g","k","z","d","a","m","c","j","r","t","v","w","y","f","b","o","i","s","n","l","e","u","p","h")
rotor2 = ("v","ñ","l","q","z","o","f","h","d","k","m","y","e","c","i","w","p","s","b","a","j","t","r","u","x","g","n")
rotor3 = ("t","ñ","w","b","e","i","k","z","r","s","l","d","x","v","f","q","y","j","h","m","u","o","c","g","p","a","n")
rotor4 = ("m","ñ","p","f","r","q","j","z","e","v","d","h","a","t","y","o","w","x","c","l","g","k","n","s","b","i","u")
rotor5 = ("z","ñ","s","c","t","u","y","m","p","a","b","v","q","i","j","x","k","h","e","w","d","l","f","r","n","g","o")
abecedario  = ()
relaciones_letras = {}
cambios_posicion_rotor1 = {
 "q":26,"ñ":25,"x":24,"g":23,"k":22,"z":21,"d":20,"a":19,"m":18,"c":17,
 "j":16,"r":15,"t":14,"v":13,"w":12,"y":11,"f":10,"b":9,"o":8,"i":7,
 "s":6,"n":5,"l":4,"e":3,"u":2,"p":1,"h":0
}
cambios_posicion_rotor2 = {
 "v":26,"ñ":25,"l":24,"q":23,"z":22,"o":21,"f":20,"h":19,"d":18,"k":17,
 "m":16,"y":15,"e":14,"c":13,"i":12,"w":11,"p":10,"s":9,"b":8,"a":7,
 "j":6,"t":5,"r":4,"u":3,"x":2,"g":1,"n":0
}
cambios_posicion_rotor3 = {
 "t":26,"ñ":25,"w":24,"b":23,"e":22,"i":21,"k":20,"z":19,"r":18,"s":17,
 "l":16,"d":15,"x":14,"v":13,"f":12,"q":11,"y":10,"j":9,"h":8,"m":7,
 "u":6,"o":5,"c":4,"g":3,"p":2,"a":1,"n":0
}
cambios_posicion_rotor4 = {
 "m":26,"ñ":25,"p":24,"f":23,"r":22,"q":21,"j":20,"z":19,"e":18,"v":17,
 "d":16,"h":15,"a":14,"t":13,"y":12,"o":11,"w":10,"x":9,"c":8,"l":7,
 "g":6,"k":5,"n":4,"s":3,"b":2,"i":1,"u":0
}
cambios_posicion_rotor5 = {
 "z":26,"ñ":25,"s":24,"c":23,"t":22,"u":21,"y":20,"m":19,"p":18,"a":17,
 "b":16,"v":15,"q":14,"i":13,"j":12,"x":11,"k":10,"h":9,"e":8,"w":7,
 "d":6,"l":5,"f":4,"r":3,"n":2,"g":1,"o":0
}
posiciones_iniciales = []
#Consultar que rotores se usarán, en que orden y cual será su posición inicial
rotores_usar = list(input("¿Qué rotores se usarán para el cifrado del mensaje? Ingrese 3 números del 1 al 5 con el formato 123, 345, 231: "))
for rotor in (1,2,3,4,5):
    if rotor in rotores_usar:
        posicion_inicial = int(input(f"Ingrese la posición incial para el rotor {rotor}: "))
        posiciones_iniciales.append(posicion_inicial)
#Definición de las relaciones entre las primeras 10 letras del abecedario
for letra in "ABCDEFGHIJ":
    relación = input(f"ingrese la relación para la letra {letra}: ")
    relaciones_letras.update({letra: relación})
#Intercambiar las letras del mensaje según las relaciones definidas
for letra in Mensaje:
    if letra in relaciones_letras:
        Mensaje = Mensaje.replace(letra, relaciones_letras[letra])
#Cifrado en los rotores
for letra in Mensaje:
    pass